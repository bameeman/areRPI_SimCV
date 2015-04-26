from SimpleCV import Camera,Display
import time 
cam = Camera()
display = Display()
while True:
	image = cam.getImage()
	image.save(display)

