from picamera import PiCamera
from  time import sleep
print("----------Waiting for camera to settle-----------")
sleep(1) # to stabilize sensor
print ("Capturing the Images")
camera= PiCamera()
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/Image/image%s.jpg' % i)
    print("image",i,"created")
camera.stop_preview()
