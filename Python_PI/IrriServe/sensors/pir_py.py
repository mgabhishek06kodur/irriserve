import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN) #PIR
GPIO.setwarnings(False)


try:
    print("Waiting for sensor to settle")
    time.sleep(2) # to stabilize sensor
    print ("Detecting motion")
    while True:
        if GPIO.input(14):
            time.sleep(1) #led turns on for 0.5 sec
            print("Motion Detected...")
        else:
            print("Motion Not Detected...")
            time.sleep(1) #to avoid multiple detection
        time.sleep(2) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()
