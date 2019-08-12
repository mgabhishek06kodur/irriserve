import bluetooth
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m11, GPIO.OUT)

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

client_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
port = 1
client_socket.bind(("",port))
client_socket.listen(1)
 
server_socket,address = client_socket.accept()
print("Accepted connection from ",address)

def MotorStop():
    read_ser=ser.readline()
    stop=read_ser.strip()
    stop=[int(s) for s in stop.split() if s.isdigit()]
    stop=int(stop[0])
    return 0

def MotorStart():
    read_ser=ser.readline()
    stop=read_ser.strip()
    stop=[int(s) for s in stop.split() if s.isdigit()]
    stop=int(stop[0])
    return 0   

def MotorInter():
    read_ser=ser.readline()
    stop=read_ser.strip()
    stop=[int(s) for s in stop.split() if s.isdigit()]
    stop=int(stop[0])
    return 0

def bluetoot():
    data=""
    while 1:
             data= server_socket.recv(1024)
             print("Send: %s" % data)
             if((data > 300) and (data < 500)):
                 MotorStop()
             elif((data > 500) and (data < 800)):
                 MotorInter()
             else:
                 MotorStart()



client_socket.close()
server_socket.close()
