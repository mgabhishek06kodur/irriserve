import Adafruit_DHT
import time as t
import RPi.GPIO as GPIO
from picamera import PiCamera
from  time import sleep
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
# Set GPIO sensor is connected to
dht = 17
pir = 23
led = 24
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN) #PIR
GPIO.setup(led, GPIO.OUT) #led
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setwarnings(False)

def dht():
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, dht)
    try:
        print("-----------Waiting for the sensor to settle----------")
        t.sleep(2)
        print(" Detecting the temperature and Humidity.....")
        # Reading the DHT11 is very sensitive to timings and occasionally
        # the Pi might fail to get a valid reading. So check if readings are valid.
        while True:
            if humidity is not None and temperature is not None:
                t.sleep(1) 
                print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            else:
                print('Failed to get reading. Try again!')
                t.sleep(1)
    except:
        GPIO.cleanup()

def pir():
    try:
        print("----------Waiting for PIR to settle----------")
        t.sleep(2) # to stabilize pir
        print ("Detecting motion")
        while True:
            if GPIO.input(pir):
                GPIO.output(led, True)
                t.sleep(1) #led turns on for 1 sec
                print("Motion Detected...")
            else:
                GPIO.output(led, False)
                print("Motion Not Detected...")
                t.sleep(1) #to avoid multiple detection
            t.sleep(2) #loop delay, should be less than detection delay
    except:
        GPIO.cleanup()

def moisture():
    try:
        print("----------Waiting for sensor to settle----------")
        t.sleep(2) # to stabilize sensor
        print ("Detecting motion")
        def callback(channel):
                if GPIO.input(channel):
                        GPIO.output(led, True)
                        t.sleep(1)
                        print("Water Detected!")
                else:
                        GPIO.output(led, False)
                        t.sleep(1)
                        print("Water Not Detected!")
        GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
        GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
        # infinite loop
        while True:
                time.sleep(1)
    except:
        GPIO.cleanup()

def camcapture():
    print("----------Waiting for camera to settle-----------")
    t.sleep(2) # to stabilize sensor
    print ("Capturing the Images")
    camera= PiCamera()
    camera.start_preview()
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Desktop/Image/image%s.jpg' % i)
    camera.stop_preview()


def main():
    dht()
    pir()
    moisture()
    camcapture()


while True:    
    main()
