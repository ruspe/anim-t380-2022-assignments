'''
asset exporter

'''
import maya.cmds as cmds
import os
import json

settings = json.load("C:/Users/cypek/Documents/anim-t380-2022-assignments/assignment-final/python/settings.json") #move to standard location

#asset information for naming - should be inputted by user through UI
assetInfo = {
"asset": "testAsset",
"location": "basement", #location is either basement, groundFloor, or secondFloor
"version": 1,
"projectDirectory": settings.get("projectDirectory")
} #temp values


#formatting the file path - how to get file path from user?
#filePathFormat = "C:/Users/{user}/Documents/Motel23Studios/ShadyCreekLodge/Content/ShadyCreekLodge/Assets/Environment/{location}/{asset}_{location}_V{version}.fbx"
filePathFormat = "{projectDirectory}/ShadyCreekLodge/Content/ShadyCreekLodge/Assets/Environment/{location}/{asset}_{location}_V{version}.fbx"

#Freeze transforms
cmds.makeIdentity(a=True)

#delete history
cmds.delete(constructionHistory = True)

#check UVs


#export file
cmds.file(filePathFormat.format(**assetInfo), force=True, exportSelected = True, type = 'FBX export')

#ui confirmation of exported asset