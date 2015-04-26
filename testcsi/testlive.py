from SimpleCV import *

cam = Camera(1,{"width":640,"height":480})
disp = Display(resolution=(640,480))

while not disp.isDone():
	img = cam.getImage()
	img.save(disp)

