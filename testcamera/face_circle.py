from SimpleCV import Camera , Display,DrawingLayer,Color
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)

myCamera = Camera(prop_set={'width':320,'height':240})
myDisplay = Display(resolution=(320,240))

while not myDisplay.isDone():
	frame = myCamera.getImage()
	faces = frame.findHaarFeatures('face')
	if faces:
		for face in faces:
			print "Face at : " + str(face.coordinates())
		GPIO.output(23,1)
	else:
		print "No face Detect!"
		GPIO.output(23,0)
	
#	frame.save(myDisplay)
	frame.show()
