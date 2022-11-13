initializeFileName.py takes the current maya scene and saves it with the proper naming conventions.
The file format is this: {project}.{asset}.{task}.{artist}.{version}.{ext}
______________

incrementVersion.py takes a file name, given it's following the conventions set up in initializeFileName.py, and increments it by 1. 
If your file is not set up with that naming convention, use initializeFileName.py first.
It takes no arguments. 