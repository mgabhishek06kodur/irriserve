from picamera import PiCamera
from time import sleep
camera=PiCamera()
camera.start_preview()
camera.annotate_text_size=50
sleep(1)
camera.stop_preview()
