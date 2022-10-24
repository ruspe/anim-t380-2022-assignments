import os
from os import listdir
#import argparse not sure if needed

framesPath = "C:/Users/cypek/Documents/anim-t380-2022-assignments/assignment-midterm/test"

#declare a list of broken images -  add to it later
brokenImages = []

print("Scanning...")

#loop through each image in directory
for images in os.listdir(framesPath):

    imgPath = "{}/{}".format(framesPath, images)

    #get image size
    imgSize = os.path.getsize(imgPath)
    print("Image: {} Size: {}".format(images, imgSize))


