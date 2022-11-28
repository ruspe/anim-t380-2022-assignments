scanBrokenFrames.py will scan a file path of images and look for broken frames. 
It looks for:

    • Frames with a file size of less than 50% of the frame before it
    • Frames that only contain the color black

It takes 2 arguments:

     • pathToScan: The path where the frames are located. Note that this must in be in quotes and only contain images, as this script will scan everything in that path.  (string)
     • extension: extension of target frames ex. .jpeg (string)


It will save 'report.txt' in the path specified. 

This project also contains a folder with test images: 1 is abnormally small and the other is all black.

example:

    $ python scanBrokenFrames.py "C:\Users\cypek\Documents\anim-t380-2022-assignments\assignment-midterm\test" .jpeg
