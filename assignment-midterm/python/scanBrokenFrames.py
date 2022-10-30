"""
This script will scan a path for broken images and print report.txt with any images that are too small or all black.

"""

import os
from os import listdir
#from re import T
#from statistics import variance


import argparse

parser = argparse.ArgumentParser(description='This script scans a file path of images and reports if any are abnormally small or all black.')
parser.add_argument('pathToScan', type=str, help="STRING: Path of images to scan")
parser.add_argument('extension', type=str, help="STRING: intended extension of images")

args = parser.parse_args()

framesPath = args.pathToScan
sizeVariation = .5

#declare a list of broken images -  add to it later
brokenImages = []

#function for checking if frame is black
def checkIfBlackFrame(targetImg):


    os.chdir(framesPath)
    #run this command in cmd - outputs a temp text file that will have 'pblack=100' in it if frame is black
    os.system('ffprobe -f lavfi -i "movie={},blackframe=1" -show_entries frame=pkt_pts_time:frame_tags > {}_output.txt'.format(targetImg, targetImg))
    
    #open the temp file and look for pblack
    with open ("{}/{}_output.txt".format(framesPath, targetImg)) as outputFile:
        if 'pblack=100' in outputFile.read():
            brokenImages.append("{} : Black frame".format(targetImg))
    outputFile.close() 
    
    #gets rid of temp file
    os.remove("{}/{}_output.txt".format(framesPath, targetImg))


print("Scanning frames...")


#loop through each image in directory
for images in os.listdir(framesPath):

    imgPath = "{}/{}".format(framesPath, images)

    #check if image name ends with given extension
    if images.endswith(args.extension):


        #get image size
        imgSize = os.path.getsize(imgPath)

        #gets the size of the previous frame
        try: prevSize
        except NameError: prevSize = None
        #if previous frame exists, compare sizes
        if prevSize != None:

            #declaring variable for minimum size
            minSize = prevSize * sizeVariation

            #if size is too small
            if imgSize < minSize:
                brokenImages.append("{} : File abnormally small".format(images))


        prevSize = imgSize
        checkIfBlackFrame(images)

print("Writing Report...")

#output this to file - will replace any existing report.txt
with open("report.txt", 'w') as reportFile:

    #write each image in brokenImages as a new line in the report file
    for item in brokenImages:
        reportFile.write("{} \n".format(item))

reportFile.close()

print("Done!")

