from SimpleCV import Camera,Image
import time

cam = Camera()

numframes = 10

for x in range(0,numframes)
		img = cam.getImage()
		filepath = "image-"+str(x)+".jpg"
		img.save(filepath)
		print "Saved Image to:"+filepath
		time.sleep(2)
	

