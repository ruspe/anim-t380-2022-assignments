'''
asset exporter
'''
import sys
import maya.cmds as cmds
import os
import json
from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance 

#get settings from program files - user needs to copy file here
f = open("C:/Program Files/settings.json")
settings = json.load(f)

#asset information for naming - should be inputted by user through UI
assetInfo = {
"asset": "testAsset",
"location": "basement", #location is either basement, groundFloor, or secondFloor
"version": 1,
"projectDirectory": settings.get("projectDirectory")
} #temp values

location = ["basement","groundFloor","secondFloor"]

#file path
filePathFormat = "{projectDirectory}/ShadyCreekLodge/Content/ShadyCreekLodge/Assets/Environment/{location}/{asset}_{location}_V{version}.fbx"

selected = cmds.ls(selection=True)

# Get a reference to the main Maya application window
def maya_main_window():	
	mayaMainWindowPtr = omui.MQtUtil.mainWindow()

	if sys.version_info.major >= 3:
		return wrapInstance(int(mayaMainWindowPtr),QWidget )

	else:  
		return wrapInstance(long(mayaMainWindowPtr), QWidget)

#Main Maya class for UI
class MyMayaWidget(QMainWindow):    
	def __init__(self, *args, **kwargs):        
		super(MyMayaWidget, self).__init__(*args, **kwargs)
		
		self.setWindowTitle("Model Clean Up/Export Tool")
		self.setGeometry(500, 300, 400, 100)


		#asset input widget
		assetLabel = QLabel(self)
		assetLabel.setText("Asset:")

		self.assetInput = QLineEdit(self)
		self.assetInput.setPlaceholderText("Enter asset name")

		selectButton = QPushButton("Confirm Selection") 
	
		selectLayout = QHBoxLayout()
		selectLayout.addWidget(assetLabel)
		selectLayout.addWidget(self.assetInput)

		#location input widget
		locationLabel = QLabel(self)
		locationLabel.setText("Location:")
		self.locationCombo = QComboBox(self)
		self.locationCombo.addItems(location)

		locationLayout = QHBoxLayout()
		locationLayout.addWidget(locationLabel)
		locationLayout.addWidget(self.locationCombo)

		#version input widget
		versionLabel = QLabel(self)
		versionLabel.setText("Version:")
		self.versionInput = QLineEdit(self)
		
		versionLayout = QHBoxLayout()
		versionLayout.addWidget(versionLabel)
		versionLayout.addWidget(self.versionInput)

		#button widgets
		exportButton = QPushButton("Export Model")
		checkUV = QPushButton("Check UVs")

		#Layout of the widgets
		hBoxLayout = QHBoxLayout()
		hBoxLayout.addWidget(exportButton)

		vBoxLayout = QVBoxLayout()
		vBoxLayout.addStretch(1)
		vBoxLayout.addLayout(selectLayout)
		vBoxLayout.addLayout(locationLayout)
		vBoxLayout.addLayout(versionLayout)
		vBoxLayout.addWidget(selectButton)
		vBoxLayout.addWidget(checkUV)
		vBoxLayout.addLayout(hBoxLayout)
		
		widget = QWidget(self)
		widget.setLayout(vBoxLayout)
		self.setCentralWidget(widget)

		#Connects buttons to actions
		selectButton.clicked.connect(self.renameAsset)
		checkUV.clicked.connect(self.UVcheck)
		exportButton.clicked.connect(self.exportFile)
		self.locationCombo.currentTextChanged.connect(self.locationChange)

		#Additional UI trigger Messages
		self.confirmation = QMessageBox()
		self.confirmation.setWindowTitle("Export Status")
		self.confirmation.setText("Your model has been exported")

		#UV history found message
		self.UVConfirmationTrue = QMessageBox()
		self.UVConfirmationTrue.setWindowTitle("UV Confirmation")
		self.UVConfirmationTrue.setText("Object has UV history - you may continue export")

		#No UV History message
		self.UVConfirmationFalse = QMessageBox()
		self.UVConfirmationFalse.setWindowTitle("UV Confirmation")
		self.UVConfirmationFalse.setText("Object does not have UV History - did you remember to UV this model??")
		


	#Changes directory of location
	def locationChange(self):
		assetInfo["location"]= self.locationCombo.currentText()

		#print(assetInfo)

	#Changes directory of asset name and version 	
	def renameAsset(self):
		assetInfo["asset"] = self.assetInput.text()
		assetInfo["version"] = self.versionInput.text()
		print(assetInfo)
		
	
	#function for checking UVs
	#works by checking the history of the object for anything UV related that has been done - does not work if history has already been deleted
	def checkUVs(self):
		UVHistory = ["polyTweak", "polyMapSewMove", "polyAutoProjection"] #should be a list of all UV related commands

		objHistory = cmds.listHistory()
		print(objHistory)

		uvHist = []
	
		for ele in UVHistory:
			if any(ele in s for s in objHistory):
				uvHist.append(True)
			else:
				uvHist.append(False)

		if all(item is False for item in uvHist):
			self.UVConfirmationFalse.exec_()
		else:
			self.UVConfirmationTrue.exec_()

	#function for reselecting the selected objects after cycling through them
	def reselectList(self):
		for obj in selected:
			cmds.select(obj, add=True)


	#check UVs for each object
	#this has to be done before history is deleted for any object in case user wants to interrupt
	def UVcheck(self):
		for obj in selected:
			cmds.select(obj)
			self.checkUVs()

		self.reselectList()

	
	def exportFile(self, i):
		#Freeze transforms
		cmds.makeIdentity(a=True)
		#delete history
		cmds.delete(constructionHistory = True)
		#export file
		cmds.file(filePathFormat.format(**assetInfo), force=True, exportSelected = True, type = 'FBX export')
		
		self.confirmation.exec_()
		

	#ui confirmation of exported asset


#UI initialization loop
if __name__ == "__main__":	

	my_widget = MyMayaWidget()     
	my_widget.show()
   