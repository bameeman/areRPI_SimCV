import subprocess
from SimpleCV import Image,Display
import time
disp = Display()

while not disp.isDone(): 
	subprocess.call("raspistill -n -w %s -h %s -o image.bmp"%(640,480),shell=True)
	img = Image("image.bmp")
	img.save(disp)


time.sleep(5)

