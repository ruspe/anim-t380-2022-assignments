'''
asset exporter

'''
import maya.cmds as cmds

#asset information for naming - should be inputted by user through UI
assetInfo = {
"asset": "testAsset",
"location": "basement", #location is either basement, groundFloor, or secondFloor
"version": 1,
} #temp values


#formatting the file path - how to get file path from user?
filePathFormat = "C:/Users/cypek/Documents/Motel23Studios/ShadyCreekLodge/Content/ShadyCreekLodge/Assets/Environment/{location}/{asset}_{location}_V{version}.fbx"

#Freeze transforms
cmds.makeIdentity(a=True)

#delete history
cmds.delete(constructionHistory = True)

#check UVs


#export file
cmds.file(filePathFormat.format(**assetInfo), force=True, exportSelected = True, type = 'FBX export')

#ui confirmation of exported asset