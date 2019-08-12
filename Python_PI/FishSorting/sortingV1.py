import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)

GPIO_TRIGGER = 18

GPIO_ECHO = 21

GPIO.setwarnings(False)

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)

GPIO.setup(GPIO_ECHO, GPIO.IN)

p = GPIO.PWM(24, 50)

p.start(7.5)

i=0

def distance():

    GPIO.output(GPIO_TRIGGER, True)

 

    # set Trigger after 0.01ms to LOW

    time.sleep(0.00001)

    GPIO.output(GPIO_TRIGGER, False)

 

    StartTime = time.time()

    StopTime = time.time()

 

    while GPIO.input(GPIO_ECHO) == 0:

        StartTime = time.time()

 

    # save time of arrival

    while GPIO.input(GPIO_ECHO) == 1:

        StopTime = time.time()

 

    # time difference between start and arrival

    TimeElapsed = StopTime - StartTime

    # multiply with the sonic speed (34300 cm/s)

    # and divide by 2, because there and back

    distance = (TimeElapsed * 34300) / 2

 

    return distance
def rightServo():
    p.ChangeDutyCycle(2.5)  # turn towards 0 degree
    time.sleep(1) # sleep 2 second
    p.ChangeDutyCycle(12.5) # turn towards 180 degree
    time.sleep(1) # sleep 2 second 
    
def leftServo():
    p.ChangeDutyCycle(2.5)  # turn towards 0 degree
    time.sleep(1) # sleep 2 second
    p.ChangeDutyCycle(12.5) # turn towards 180 degree
    time.sleep(1) # sleep 2 second 
    
def servo(d):
    try:
        #while True:
            #p.ChangeDutyCycle(7.5)  # turn towards 90 degree
            #time.sleep(2) # sleep 1 second
            print(d)
            if(d==1):
                rightServo()
            elif(d==2):
                leftServo()
            else:
                print("Not Matched")
           
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup() 

if __name__ == '__main__':

    try:

        while True:

            dist = distance()

            #print ("Measured Distance = %.1f cm" % dist)
            print("Hello")
            time.sleep(.01)
            
            if dist<=25 and dist>=5:
              print("distance:",dist,"cm")
              a = int(input("enter the number:"))
              servo(a)
              i=1
            time.sleep(.01)
            if dist>25 and i==1:
              print("place the object....")
              i=0
            time.sleep(.01)
 

        # Reset by pressing CTRL + C

    except KeyboardInterrupt:

        print("Measurement stopped by User")

        GPIO.cleanup()
