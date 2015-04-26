from SimpleCV import Camera,Image,Display
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)

cam = Camera(2,prop_set={"width":320,"height":240})
display = Display(resolution=(320,240))
x = 0
print "Camera Ready"

while 1:
	img = cam.getImage()
	img.save(display)
	inputvalue = GPIO.input(24)
	if (inputvalue == 0):
		img = cam.getImage()
		img.save(display)
		filepath = "image-"+str(x)+".jpg"
		img.save(filepath)
		print "Saved Image to:"+filepath
		time.sleep(2)
		x = x+1

