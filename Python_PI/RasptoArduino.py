import serial
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 18
# importing the requests library 
import requests 

ser=serial.Serial("/dev/ttyACM1",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
#def blink(pin):
    
    
#    GPIO.output(pin,GPIO.HIGH)  
 #   time.sleep(1)  
 #   GPIO.output(pin,GPIO.LOW)  
 #   time.sleep(1)  
  #  return
 
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)
#while True:
def soilmoisture():
    for i in range(3):   
        read_ser=ser.readline()
        #print(read_ser)
        #a=int(read_ser.strip())
        #print(a)
        time.sleep(2)
        #if(read_ser=="Hello From Arduino!"):
          #  blink(11)
      
        # URL ="http://www.irriserve.xyz/PiUpdate/UpdateSoil.php"
        URL = "http://www.irriserve.xyz/PiUpdate/UpdateSoil.php"
       
        # moisture given here 

        moisture=read_ser.strip()
        moisture=[int(s) for s in moisture.split() if s.isdigit()]
        moisture=int(moisture[0])
        print(moisture)
        # defining a params dict for the parameters to be sent to the GET Method 
        PARAMS = {'moisture':moisture} 
          
        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
          
        # extracting data in json format 
        #data = r.json() 
         
        print("Soil data Updated Sucessfully")
        return 0
def Temperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    for i in range(3): 
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            #temperature = temperature
        else:
            print('Failed to get reading. Try again!')
    URL = "http://www.irriserve.xyz/PiUpdate/UpdateTemp.php"
    PARAMS = {'temperature':temperature} 
    r = requests.get(url = URL, params = PARAMS)
    print("Temperature  Updated Sucessfully")
    return 0
def Humidity():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    for i in range(3): 
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            #humidity = humidity
        else:
            print('Failed to get reading. Try again!')
    URL = "http://www.irriserve.xyz/PiUpdate/UpdateHumidity.php"
    PARAMS = {' humidity': humidity} 
    r = requests.get(url = URL, params = PARAMS)
    print(" Humidity data Updated Sucessfully")
    return 0
if __name__ == '__main__':
    try:
        print(" ----------------------------------------------------------Hi New Bee---------------------------------------------------------- ")
        time.sleep(1)
        print(" ----------------------------------Welcome to IrriServe---------------------------------- ")
        time.sleep(1)
        while True:
            print(" -------------------------------------------Want to know How it Works?------------------------------------------- ")
            print(" ---------------------Lets Start With Soil Moisture of the area--------------------- ")
            a = int(soilmoisture())
            if((a > 300) and (a < 500)):
                print("Moisture is above 75%")
            elif((a > 500) and (a < 800)):
                print("Moisture is above 50%")
            else:
                print("Moisture is below 25%")
                
            time.sleep(1)
            print(" -------------------------------------------Lets Check the Temperature of the area------------------------------------------- ")
            print(" -------------------------------------------Wait for a second too settle the device------------------------------------------- ")
            b = Temperature()
            if(b > 45):
                print(" -------------------------------------------Its too Hot Over here------------------------------------------- ")
            elif((b < 45) and (b > 30)):
                print(" -------------------------------------------Its a Moderate Temperature------------------------------------------- ")
            else:
                print(" -------------------------------------------Its Cool Over here------------------------------------------- ")

            Humidity()
            time.sleep(1)
          
    except KeyboardInterrupt:

        print(" -------------------------------------------Stop------------------------------------------- ")

        GPIO.cleanup()

        
