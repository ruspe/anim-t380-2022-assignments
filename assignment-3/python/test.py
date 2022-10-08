#This script takes an environment variable 'asset' and uses it to create a directory

import os
asset = os.getenv('asset') #makes asset a variable we can use later

#Creates the directories we need
path = "assets/%a/maya/scenes" % (asset)
os.makedirs(path)
print("New Directory:")
print(path)


