'''
asset exporter

'''
import maya.cmds as cmds
import os
import json

#function for checking UVs
#works by checking the history of the object for anything UV related that has been done - does not work if history has already been deleted
def checkUVs():
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

#check UVs

checkUVs()

#Freeze transforms
cmds.makeIdentity(a=True)

#delete history
cmds.delete(constructionHistory = True)

#export file
cmds.file(filePathFormat.format(**assetInfo), force=True, exportSelected = True, type = 'FBX export')

#ui confirmation of exported asset