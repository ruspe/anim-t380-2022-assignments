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
		assetInput = QLineEdit(self)
		assetInput.setMaxLength(10)
		assetInput.setPlaceholderText("Enter asset name")

	
		selectButton = QPushButton("Select Object") 

		selectLayout = QHBoxLayout()
		selectLayout.addWidget(assetInput)
		selectLayout.addWidget(selectButton)

		#location input widget

		locationLabel = QLabel(self)
		locationLabel.setText("Location:")
		locationCombo = QComboBox(self)
		locationCombo.addItems(assetInfo["location"])

		locationLayout = QHBoxLayout()
		locationLayout.addWidget(locationLabel)
		locationLayout.addWidget(locationCombo)

		#version input widget
		versionLabel = QLabel(self)
		versionLabel.setText("Version:")
		versionInput = QLineEdit(self)
		

		versionLayout = QHBoxLayout()
		versionLayout.addWidget(versionLabel)
		versionLayout.addWidget(versionInput)

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
		vBoxLayout.addWidget(checkUV)
		vBoxLayout.addLayout(hBoxLayout)
		

		widget = QWidget(self)
		widget.setLayout(vBoxLayout)
		self.setCentralWidget(widget)

		#Connects buttons to actions
		selectButton.clicked.connect(self.selectObject)
		checkUV.clicked.connect(self.checkUVs)
		exportButton.clicked.connect(self.exportFile)

		

	def selectObject(self):
		cmds.select(self.assetInput.text)
		


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
			print("no UVS") #replace with pop up - "[obj name] has no UV history. Please check to make sure proper UVs have been applied"
			#Check now -> opens UV window, Continue exporting -> keeps the script going
		else:
			print("Object has UVs") #script continues

	#function for reselecting the selected objects after cycling through them
	def reselectList(self):
		for obj in selected:
			cmds.select(obj, add=True)


	#check UVs for each object
	#this has to be done before history is deleted for any object in case user wants to interrupt
	
	# for obj in selected:
	# 	cmds.select(obj)
	# 	checkUVs(self)

	# reselectList()

	
	def exportFile(self):
		#Freeze transforms
		cmds.makeIdentity(a=True)
		#delete history
		cmds.delete(constructionHistory = True)
		#export file
		cmds.file(filePathFormat.format(**assetInfo), force=True, exportSelected = True, type = 'FBX export')
		

	#ui confirmation of exported asset


#UI initialization loop
if __name__ == "__main__":	

	my_widget = MyMayaWidget()     
	my_widget.show()
   