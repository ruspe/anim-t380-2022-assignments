'''
asset exporter

'''
import maya.cmds as cmds
import os
import json

#function for checking UVs
#works by checking the history of the object for anything UV related that has been done - does not work if history has already been deleted
def checkUVs():
    UVHistory = ["polyTweak", "polyMapSewMove"] #should be a list of all UV related commands

    objHistory = cmds.listHistory()
    print(objHistory)

    for ele in UVHistory:
        if any(ele in s for s in objHistory):
            print("yes UVs")  #UVs have been done - tool can continue
        else:
            print("no UVs") # pop up here - "There is no UV history on this object. Fix now?" with Fix (brings up UV editor) or Continue Anyway (continues tool)


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

#check UVs
checkUVs()

#Freeze transforms
cmds.makeIdentity(a=True)

#delete history
cmds.delete(constructionHistory = True)

#export file
cmds.file(filePathFormat.format(**assetInfo), force=True, exportSelected = True, type = 'FBX export')

#ui confirmation of exported asset