"""
this script makes an empty group in maya with the name 'asset'
use after makeDirectory.py since it relies on the directory already existing

"""

import os
import maya.standalone
import maya.cmds

asset = os.getenv('asset') #makes asset a variable we can use later

maya.standalone.initialize()

#creates empty group named after the asset
print("Creating group...")
maya.cmds.group(em=True, n="%a" % (asset))


#saves this in the location we made in makeDirectory.py
assetPath = "C:/Users/cypek/Documents/anim-t380-2022-assignments/assignment-3/etc/assets/%a/maya/scenes/%a.ma" % (asset, asset)
maya.cmds.file(rename=assetPath)
newFile = maya.cmds.file( save=True, type='mayaAscii' )
print("Saved!")




