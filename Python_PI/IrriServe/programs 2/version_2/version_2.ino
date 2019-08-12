#include "dht.h"
#define dht_apin A0 // Analog Pin sensor is connected to
dht DHT;
//#define DHTPIN 8 
//int trigPin=2;
//int echoPin=3;
 
const int ledPin  = 13; //  the LED pin

void  setup()
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);//led pin is a variable which is assigned to 13 pin of arduino
}
void  loop() 
{ 

    Serial.println("Blink:");
    Blink();//calling Blink
    delay(1000);
    Serial.println("DHT Sensor:");
    temp();
    delay(1000);
}

//program for blinking an LED
void Blink()
{//  read  the button  state 
  digitalWrite(ledPin,HIGH);
  delay(1000);
  digitalWrite(ledPin,LOW);
  delay(1000);
}


void temp()
{
   DHT.read11(dht_apin);
    
    Serial.print("Current humidity = ");
    Serial.print(DHT.humidity);
    Serial.print("%  ");
    Serial.print("temperature = ");
    Serial.print(DHT.temperature); 
    Serial.println("C  ");
    
    delay(1000);//Wait 5 seconds before accessing sensor again.
}





