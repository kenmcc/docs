import picamera
camera = picamera.PiCamera()
camera.capture('image.jpg')
print "Photo captured"
