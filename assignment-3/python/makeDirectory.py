#This script takes an environment variable 'asset' and uses it to create a directory

import os
asset = os.getenv('asset') #makes asset a variable we can use later
asset = asset.replace("'", "") #should get rid of 's
print(asset)

#Creates the directories we need
path = "assets/%a/maya/scenes" % (asset) #not sure why this still has ' in the directory
os.makedirs(path)
print("New Directory:")
print(path)


