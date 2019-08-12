from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
camera.exposure_mode='auto'
sleep(5)
camera.capture('/home/pi/Desktop/sunlight.jpg')
camera.stop_preview()
