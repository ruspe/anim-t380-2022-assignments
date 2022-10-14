"""
this script should save the current file with the proper naming conventions as version 1

for use in maya, either make it its own shelf button or copy directly into the script editor

"""

import maya.cmds as cmds

#format
saveFileFormat = "{project}.{asset}.{task}.{artist}.{version}.{ext}"

#dict - replace with project information
#can turn into UI if i have time?
assetInfo = {
"project": "myCoolProject",
"asset": "character",
"task": "model",
"artist": "user",
"version": 1,
"ext": "ma"
}

#rename and save
cmds.file(rename=saveFileFormat.format(**assetInfo))
cmds.file(save=True)
