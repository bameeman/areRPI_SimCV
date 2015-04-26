import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.IN)

while 1:
	a = GPIO.input(24)
	if (a ==  0):
		GPIO.output(23,1)
	else:
		GPIO.output(23,0)
	

