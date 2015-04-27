from SimpleCV import Image,Display,Camera,Color

myCamera = Camera(prop_set={'width':320,'height':240})
myDisplay = Display((320,240))
red1 = 0
green1 = 0
blue1 = 0
#red2 = 0
#green2 = 0
#blue2 = 0

while not myDisplay.isDone():
	img = myCamera.getImage().flipHorizontal()
#	img.toHSV()
	if myDisplay.mouseLeft:
		point = (myDisplay.mouseX,myDisplay.mouseY)
		(red1,green1,blue1) =  img.getPixel(myDisplay.mouseX,myDisplay.mouseY)
#	if myDisplay.mouseRight:
#		(red2,green2,blue2) =  img.getPixel(myDisplay.mouseX,myDisplay.mouseY)		 
	red1 = int(red1)
	green1 = int(green1)
	blue1 = int(blue1)
	imgDist = img.colorDistance((red1,green1,blue1))
	imgDist.morphOpen()
#	imgDist.morphClose()



	
	imgBin = imgDist.binarize(35)
	imgBin = imgBin.erode()
#	imgBin.save(myDisplay)
# clear noise complete #
	blobs = imgBin.findBlobs()
#	print "Area: ", blobs.area()
#	print "Angles: ", blobs.angle()
	if blobs:
		print "Center: ",blobs.coordinates()
		img.dl().circle((int(blobs[0].x),int(blobs[0].y)),10,Color.RED,width=2)
	else:
		print "No Detect!"

#	imgBin.save(myDisplay)
	img.save(myDisplay)	


#	imgBin.erode().save(myDisplay)



#	imgBin.save(myDisplay)
#	imgBlobs = imgBin.findBlobs(Color.BLACK)
#	if imgBlobs:
#		print "postion at: " + str(imgBlobs[0].x) + "," + str(imgBlobs[0].y)
#	img.dl().circle((int(imgBlobs[0].x),int(imgBlobs[0].y)),10,Color.RED,width=2)
#	img.save(myDisplay)	
##	img.dl().circle((myDisplay.mouseX,myDisplay.mouseY),10,Color.RED,width=2)   # circle around mouse	
##	img.save(myDisplay)
