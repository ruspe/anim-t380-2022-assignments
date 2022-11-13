from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance 
import maya.cmds as cmds

#function for mirroring objects 
def mirrorGeo(scaleX, scaleY, scaleZ):
    selected = cmds.ls(sl=True)
    mirrorGroup = cmds.group(selected, n='mirrored',r=True)
    cmds.xform(objectSpace=True, pivots=(0, 0, 0))
    cmds.scale(scaleX,scaleY,scaleZ)
    cmds.ungroup()
    



#create window
window = QWidget()
window.setWindowTitle('Quick Mirror')

#create buttons
mirrorX = QPushButton("Mirror X")
mirrorY = QPushButton("Mirror Y")
mirrorZ = QPushButton("Mirror Z")

mirrorX.clicked.connect(lambda: mirrorGeo(-1,1,1)) 
mirrorY.clicked.connect(lambda: mirrorGeo(1,-1,1)) 
mirrorZ.clicked.connect(lambda: mirrorGeo(1,1,-1)) 


#create layout
layout = QHBoxLayout()
layout.addWidget(mirrorX)
layout.addWidget(mirrorY)
layout.addWidget(mirrorZ)



window.setLayout(layout)
window.show()