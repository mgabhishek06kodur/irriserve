//#include <dht.h>
//#include <DHT_U.h>

//#include "Adafruit_Sensor.h"
#include "dht.h"
#define dht_apin A0 // Analog Pin sensor is connected to
//#define DHTPIN 8 

dht DHT;

int ledPin  = 13;
 
 //  the LED pin
 

int trigPin=2;
int echoPin=3;

#define motion 7
#define led 8

int val = 0; //value for storing moisture value 
int soilPin = A0;//Declare a variable for the soil moisture sensor 
int soilPower = 7;//Variable for Soil moisture Power

long cm;

void  setup()
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);//led pin is a variable which is assigned to 13 pin of arduino

  pinMode(motion,INPUT);
  pinMode(led,OUTPUT);

  pinMode(soilPower, OUTPUT);//Set D7 as an OUTPUT
  analogWrite(soilPower, LOW);
}
void  loop() 
{ 

    Serial.println("Blink:");
    delay(1000);
    Blink();       //calling Blink
 //   delay(1000);
   // Blink();
    delay(1000);
    Serial.println("DHT Sensor:");
    delay(1000);
    temp();       //calling DHT Sensor 
    delay(3000);
    Serial.println("Ultrasonic sensor:");
    ultrasonic();
    delay(1000);
    Serial.println("PIR motion sensor");
    PIR();
    delay(1000);
    Serial.println("Analog soil moisture:");
    asoil();
    //if(cm >5)
    //{
     //digitalWrite(ledPin,HIGH);
     //delay(1000);
    //}
    //Serial.end();//calling Ultrasonic sensor
}


//program for blinking an LED
void Blink()
{//  read  the button  state
  Serial.println("ON"); 
  digitalWrite(ledPin,HIGH);
  delay(1000);
  Serial.println("OFF");
  digitalWrite(ledPin,LOW);
  delay(1000);
}

//Program for calculating the temperature
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
//Program for calculating the range
void ultrasonic()
{
  pinMode(trigPin, OUTPUT);
  digitalWrite(trigPin, LOW);
  delay(1000);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(300);
  digitalWrite(trigPin, LOW);

  pinMode(echoPin, INPUT); 
  digitalWrite(echoPin, HIGH);

long duration,inch,cm,distance;
duration = pulseIn(echoPin, HIGH);


inch=microSecondsToInches(duration);
cm=microSecondsToCentimeter(duration);
if(cm > 5)
{
 digitalWrite(ledPin,HIGH);
 Serial.println("on");
}
else
{
  digitalWrite(ledPin,LOW);
  Serial.println("off");
}
Serial.println("inches:\t");
Serial.println(inch);
Serial.println("centimeter:\t");
Serial.println(cm);

}

long microSecondsToInches(long microseconds)
{
  return  microseconds/74/2;
}

long microSecondsToCentimeter(long microseconds)
{
   return microseconds/94/2;
}

void PIR()
{
  if(digitalRead(motion)==HIGH)
  {
    digitalWrite(led,HIGH);
    Serial.println("motion detected");
    delay(1000);
    digitalWrite(led,LOW);
    delay(1000);
  }
  else
  {
    digitalWrite(led,LOW);
    Serial.println("motion not detected");
    delay(1000);
  }
}

void asoil()
{
  Serial.print("Soil Moisture = ");    
//get soil moisture value from the function below and print it
Serial.println(readSoil());

//This 1 second timefrme is used so you can test the sensor and see it change in real-time.
//For in-plant applications, you will want to take readings much less frequently.
delay(1000);//take a reading every second
}

int readSoil()
{

    analogWrite(soilPower, HIGH);//turn D7 "On"
    delay(10);//wait 10 milliseconds 
    val = analogRead(soilPin);//Read the SIG value form sensor 
    analogWrite(soilPower, LOW);//turn D7 "Off"
    return val;//send current moisture value
}


