from SimpleCV import Camera,Display,Image
import SimpleCV
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)


#cam = Camera(1)
#cam = Camera(1,{"width":1280,"height":1024})
cam = SimpleCV.Camera(1,{"width":640,"height":480})
display = SimpleCV.Display(resolution=(640,480))
x = 0
print "Camera Ready"
while not display.isDone():
	inputvalue = GPIO.input(24)
	img = cam.getImage()
	img = img.flipHorizontal()
	img.save(display)

if (inputvalue == 0):
		img = cam.getImage()
		img = img.flipHorizontal()
		filepath = "image-"+str(x)+".jpg"
		img.save(filepath)
		print "Saved Image to:"+filepath
		time.sleep(2)
		x = x+1

