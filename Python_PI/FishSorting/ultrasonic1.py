import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
triger = 18
echo = 24

GPIO.setup(triger,GPIO.OUT)
GPIO.setup(echo ,GPIO.IN)
def distance():
    GPIO.output(triger, True)
    time.sleep(.00001)
    GPIO.output(triger, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(echo)==0:
        StartTime = time.time()
        while GPIO.input(echo)==1:
            StopTime = time.time()
        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300)/2
        return distance
if __name__ == '__main__':
    try :
        while True:
            dist = distance()
            print("Measured DIstance = %.if cm" %dist)
            time.sleep(1)
    except KeyboardInterupt:
        print("Measurement Stopped by User")
        GPIO.cleanup()





#import RPi.GPIO as GPIO                    #Import GPIO library
#import time                                #Import time library
#GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

#TRIG = 18                                  #Associate pin 23 to TRIG
#ECHO = 24                                  #Associate pin 24 to ECHO

#print "Distance measurement in progress"

#GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
#GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

#while True:

 # GPIO.output(TRIG, False)                 #Set TRIG as LOW
 # print "Waitng For Sensor To Settle"
  #time.sleep(2)                            #Delay of 2 seconds

  #GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  #time.sleep(0.00001)                      #Delay of 0.00001 seconds
  #GPIO.output(TRIG, False)                 #Set TRIG as LOW

 # while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
  #  pulse_start = time.time()              #Saves the last known time of LOW pulse

  #while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
  #  pulse_end = time.time()                #Saves the last known time of HIGH pulse 

 # pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  #distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  #distance = round(distance, 2)            #Round to two decimal points

  #if distance > 2 and distance < 400:      #Check whether the distance is within range
  #  print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
  #else:
   # print "Out Of Range"                   #display out of range






GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

while True:

  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print"Waitng For Sensor To Settle"
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 2 and distance < 400:      #Check whether the distance is within range
    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
  else:
    print "Out Of Range"                   #display out of range
