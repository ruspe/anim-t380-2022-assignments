"""
this script should take a file with proper naming structure and increment the version by 1
if file name is not set up, use initializeFileName.py first

for use in maya, either make it its own shelf button or copy directly into the script editor

"""

import maya.cmds as cmds

#get current file name
currentFileName = cmds.file(q=True, sn=True, shn=True)

#splits file name
project, asset, task, artist, version, ext = currentFileName.split(".")
saveFileFormat = "{project}.{asset}.{task}.{artist}.{version}.{ext}"

#moves split file name into its own dict
assetInfo = {
"project": project,
"asset": asset,
"task": task,
"artist": artist,
"version": int(version) + 1, #increment the version
"ext": ext
}

#rename and save
cmds.file(rename=saveFileFormat.format(**assetInfo))
cmds.file(save=True)
