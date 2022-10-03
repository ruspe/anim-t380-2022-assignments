#Code that creates a snowman in maya

#import args
    #baseRadius: int
    #midRadius: int
    #topRadius: int

import argparse

parser = argparse.ArgumentParser(description='This script creates three maya spheres in the shape of a snowman.')
parser.add_argument('baseRadius', type=int, help="INT: Radius of the base sphere")
parser.add_argument('midRadius', type=int, help="INT: Radius of the middle sphere")
parser.add_argument('topRadius', type=int, help="INT: Radius of the top sphere")


args = parser.parse_args()

import maya.standalone
maya.standalone.initialize()

import maya.cmds


#creates the base sphere. it does not need to move
print("Creating base...")
maya.cmds.polySphere(r=args.baseRadius)

#creates the middle sphere and moves it up
print("Creating middle...")
maya.cmds.polySphere(r=args.midRadius)
maya.cmds.move(0,args.baseRadius + args.midRadius,0)

#creates the top sphere and moves it up
print("Creating top...")
maya.cmds.polySphere(r=args.topRadius)
maya.cmds.move(0,args.baseRadius + args.midRadius*2 + args.topRadius,0)

#saves file to default project as snowman.ma
cmds.file( rename='snowman.ma' )
newFile = cmds.file( save=True, type='mayaAscii' )
print("Saved!")
print(newFile)