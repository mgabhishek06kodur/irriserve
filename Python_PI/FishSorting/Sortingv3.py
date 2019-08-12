from __future__ import print_function
from __future__ import division

import RPi.GPIO as GPIO
import time

import cv2 as cv
import numpy as np
import argparse,os


from picamera import PiCamera
from time import sleep

#GPIO.setmode(GPIO.BOARD)

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
ser1 = 24
ser2 = 23
GPIO_ECHO = 21

GPIO.setup(ser1, GPIO.OUT)
GPIO.setup(ser2, GPIO.OUT)

GPIO.setwarnings(False)

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)

GPIO.setup(GPIO_ECHO, GPIO.IN)

camera = PiCamera()

p1 = GPIO.PWM(ser1, 50)
p2 = GPIO.PWM(ser2, 50)
p1.start(7.5)
p2.start(7.5)
i=0




def cameraPic():
    try:
        camera.start_preview()

        for i in range(10):
            sleep(0.01)
            camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    except KeyboardInterrupt:
        camera.stop_preview()
        GPIO.cleanup()
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
def Servo1():
    p1.ChangeDutyCycle(2.5)  # turn towards 0 degree
    time.sleep(1) # sleep 2 second
    p1.ChangeDutyCycle(12.5) # turn towards 180 degree
    time.sleep(1) # sleep 2 second 
    
def Servo2():
    p2.ChangeDutyCycle(12.5)  # turn towards 0 degree
    time.sleep(1) # sleep 2 second
    p2.ChangeDutyCycle(2.5) # turn towards 180 degree
    time.sleep(1) # sleep 2 second 
    
def servo(d):
    try:
        #while True:
            #p.ChangeDutyCycle(7.5)  # turn towards 90 degree
            #time.sleep(2) # sleep 1 second
            print(d)
            if(d==1):
                Servo1()
            elif(d==2):
                Servo2()
            else:
                print("Not Matched")
           
    except KeyboardInterrupt:
        p1.stop()
        p2.stop()
        GPIO.cleanup() 

if __name__ == '__main__':

    try:

        while True:

            dist = distance()

            #print ("Measured Distance = %.1f cm" % dist)
            print("Hello")
            time.sleep(.01)
            
            cameraPic()
            print("Picture Captured")
            
            if dist<=25 and dist>=5:
              print("distance:",dist,"cm")
              
            srcb="/home/pi/Desktop/image6.jpg" #KoduvaiTest/PampletTest/FishTest/BandaTest
            src_t1="/home/pi/FinalCode/Fishes/Koduvai.jpg"
            src_t2="/home/pi/FinalCode/Fishes/Pamplet.jpg"
            print("Test File :",srcb)
              
            src_base = cv.imread(srcb)
            src_test1  = cv.imread(src_t1)
            src_test2  = cv.imread(src_t2)
            
            src_base = np.array(src_base, dtype=np.uint8)  
              
            hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
            hsv_test1 = cv.cvtColor(src_test1, cv.COLOR_BGR2HSV)
            hsv_test2 = cv.cvtColor(src_test2, cv.COLOR_BGR2HSV) 
            
            h_bins = 50
            s_bins = 60
            histSize = [h_bins, s_bins] 
            
            channels = [0, 1]
            
            hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
            cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

            hist_test1 = cv.calcHist([hsv_test1], channels, None, histSize, ranges, accumulate=False)
            cv.normalize(hist_test1, hist_test1, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

            hist_test2 = cv.calcHist([hsv_test2], channels, None, histSize, ranges, accumulate=False)
            cv.normalize(hist_test2, hist_test2, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

            compare_method=0
            base_base = cv.compareHist(hist_base, hist_base, compare_method)
            base_test1 = cv.compareHist(hist_base, hist_test1, compare_method)
            base_test2 = cv.compareHist(hist_base, hist_test2, compare_method)
            print('Method:', compare_method, 'Perfect,  Base-Test1,  Base-Test2:',base_base, '/',  base_test1, '/',  base_test2)
            print("----------------------------------------------")
            if base_test1<0 or base_test2<0:
                print("Other Fish")
                a=3
            elif base_test1>base_test2:
                print("Koduvai Fish")
                a=2
            elif base_test2>base_test1:
                print("Pamplet Fish")
                a=1
            else:
                print("Other")
                a=0
            print("----------------------------------------------")
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
