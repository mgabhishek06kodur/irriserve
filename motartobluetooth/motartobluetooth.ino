#include <SoftwareSerial.h> 

#define relay A3
#define interval 10000

SoftwareSerial Genotronex(10, 11); // RX, TX
int ledpin=13; // led on D13 will show blink on/off
int BluetoothData; // the data given from Computer

void setup() {
  pinMode(relay, OUTPUT);
 Genotronex.begin(9600);
  Genotronex.println("Bluetooth On please press 1 or 0 blink LED ..");
  pinMode(ledpin,OUTPUT);
}   
void loop()
{
   // Feed any data from bluetooth to Terminal.
  if (Genotronex.available()){
BluetoothData=Genotronex.read();
   if(BluetoothData=='1'){   // if number 1 pressed ....
   digitalWrite(ledpin,HIGH);
   Genotronex.println("LED  On D13 ON ! ");
   digitalWrite(relay, HIGH);
   //delay(interval);
   }
   else
   (BluetoothData=='0'){// if number 0 pressed ....
  digitalWrite(ledpin,0);
   Genotronex.println("LED  On D13 Off ! ");
   digitalWrite(relay, LOW);
   =
   4
   //delay(interval);
     }
 }
delay(100);// prepare for next data ...
}
