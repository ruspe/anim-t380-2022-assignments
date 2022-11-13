from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance 
import maya.cmds as cmds

"""
This is a tool for mirroring objects across any axis in both local and global space in maya.
It creates a popup window with six buttons.

It works by creating a group with selected objects and mirroring that group. For global mirroring, it sets the group pivot to the origin.

"""

#function for mirroring objects in world space
def globalMirrorGeo(scaleX, scaleY, scaleZ):
    
    #add selected objects to group with pivot at 0 global
    selected = cmds.ls(sl=True)
    mirrorGroup = cmds.group(selected, n='mirrored',r=True)
    cmds.xform(objectSpace=True, pivots=(0, 0, 0))
    
    #scale
    cmds.scale(scaleX,scaleY,scaleZ)
    cmds.ungroup()
  
#function for mirroring in local space
def localMirrorGeo(scaleX, scaleY, scaleZ):
    selected = cmds.ls(sl=True)
    mirrorGroup = cmds.group(selected, n='mirrored',r=True)
   
    cmds.scale(scaleX,scaleY,scaleZ)
    cmds.ungroup() 
  
#create window
window = QWidget()
window.setWindowTitle('Quick Mirror')

#Creating buttons

#global buttons
globalMirrorX = QPushButton("Global Mirror X")
globalMirrorY = QPushButton("Global Mirror Y")
globalMirrorZ = QPushButton("Global Mirror Z")

#connecting global buttons
globalMirrorX.clicked.connect(lambda: globalMirrorGeo(-1,1,1)) #lambda lets me put inputs into the fucntions
globalMirrorY.clicked.connect(lambda: globalMirrorGeo(1,-1,1)) 
globalMirrorZ.clicked.connect(lambda: globalMirrorGeo(1,1,-1)) 

#local buttons
localMirrorX = QPushButton("Local Mirror X")
localMirrorY = QPushButton("Local Mirror Y")
localMirrorZ = QPushButton("Local Mirror Z")

#connecting local buttons
localMirrorX.clicked.connect(lambda: localMirrorGeo(-1,1,1)) 
localMirrorY.clicked.connect(lambda: localMirrorGeo(1,-1,1)) 
localMirrorZ.clicked.connect(lambda: localMirrorGeo(1,1,-1)) 



#create text
globalLabelText = QLabel()
globalLabelText.setText("<b>Global Controls</b>")

localLabelText = QLabel()
localLabelText.setText("<b>Local Controls</b>")

#create layout in grid
layout = QGridLayout()


#global layout
layout.addWidget(globalLabelText, 0,1)
layout.addWidget(globalMirrorX, 1,0)
layout.addWidget(globalMirrorY, 1,1)
layout.addWidget(globalMirrorZ, 1,2)

#local layout
layout.addWidget(localLabelText, 3,1)
layout.addWidget(localMirrorX, 4,0)
layout.addWidget(localMirrorY, 4,1)
layout.addWidget(localMirrorZ, 4,2)



window.setLayout(layout)
window.show()