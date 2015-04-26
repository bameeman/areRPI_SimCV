from SimpleCV import Camera,Display
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)

cam = Camera()
display = Display()
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

