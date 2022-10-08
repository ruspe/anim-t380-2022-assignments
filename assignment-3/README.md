makeDirectory.py makes an empty directory in the location of the script.
It takes no arguments, but requires that an environment variable named 'asset' is set.

in the terminal, make sure you source .alias and use newTestAsset to create an environment variable.

________________________________

makeGroup.py makes an empty group in a maya scene.
It takes no arguments, but requires that an environment variable named 'asset' is set. 
It will save the scene the same name as the environment variable. 
Make sure you run makeDirectory.py first. It relies on the folder structure already being in place. 
