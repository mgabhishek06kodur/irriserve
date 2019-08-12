#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
led = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(led, GPIO.OUT) #led
GPIO.setwarnings(False)
print("Waiting for sensor to settle")
time.sleep(2) # to stabilize sensor
print ("Detecting moisture")
def callback(channel):
        if GPIO.input(channel):
                GPIO.output(led, True)
                time.sleep(1)
                print("Water Detected!")
        else:
                GPIO.output(led, False)
                time.sleep(1)
                print("Water Not Detected!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
# infinite loop
while True:
       time.sleep(1)
