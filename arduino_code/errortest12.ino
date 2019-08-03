#include<SoftwareSerial.h>
#include <Servo.h>          //standard library for the servo
#include <NewPing.h>        //for the Ultrasonic sensor function library.

#define IN1 6
#define IN2 7
#define IN3 5
#define IN4 4
//#define EN1 6
//#define EN2 5

#define IN11 8
#define IN12 12

//sensor pins
#define trig_pin A1 //analog input 1
#define echo_pin A2 //analog input 2

#define maximum_distance 200
boolean goesForward = false;
int distance = 100;

NewPing sonar(trig_pin, echo_pin, maximum_distance); //sensor function
//SoftwareSerial Genotronex(10, 11); // RX, TX
SoftwareSerial Genotronex(10, 11);
String data;
int btVal;

// Declare the Servo pin 
int servoPin1 = 0; 
int servoPin2 = 1; 
int servoPin3 = 2; 
int servoPin4 = 3;
// Create a servo object 
Servo Servo1;
Servo Servo2;  
Servo Servo3;
Servo Servo4;
Servo servo_motor; 

int val = 0; //value for storing moisture value 
int soilPin = A0;//Declare a variable for the soil moisture sensor 

void setup() 
{  
  //Serial.begin(115200);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  //pinMode(EN1, OUTPUT);
  //pinMode(EN2, OUTPUT);

  pinMode(IN11, OUTPUT);//CUTTER
  pinMode(IN12, OUTPUT);
  
//  digitalWrite(IN1, HIGH);
//  digitalWrite(IN2, LOW);
//  digitalWrite(IN3, HIGH);
//  digitalWrite(IN4, LOW);
//  //analogWrite(EN1,63);
  //analogWrite(EN2,63);

  // We need to attach the servo to the used pin number 
     Servo1.attach(servoPin1); 
     Servo2.attach(servoPin2);
     Servo3.attach(servoPin3); 
     Servo4.attach(servoPin4);

       servo_motor.attach(9); //our servo pin

  servo_motor.write(115);
  delay(2000);
  distance = readPing();
  delay(100);
  distance = readPing();
  delay(100);
  distance = readPing();
  delay(100);
  distance = readPing();
  delay(100);
     Genotronex.begin(9600);
  
  Serial.begin(9600);
}
void loop()
{
  bluetooth();
}
void bluetooth()
{
  
  while (Genotronex.available())
 {  
  {  
  data = Genotronex.readStringUntil('\n');
      //Serial.print(str);        
  } 
    btVal = (data.toInt());
    //Serial.print("BlueTooth Value ");
    //Serial.println(btVal);
     Genotronex.begin(9600);
  Genotronex.println(btVal);    

  switch (btVal) 
   {
      case 1:                                
        //Serial.println("Forward");
        forward();
        break;
      case 2:                 
       //Serial.println("Reverse");
        reverse();
        break;
      case 3:         
       //Serial.println("Left");
        left();
        break;
      case 4:                     
        //Serial.println("Right");
        right();
        break;
      case 5:                                            
         //Serial.println("Stop");
        stoprobot();
        break;
      case 6:                                            
         //Serial.println("servo right ARM");
        servoarm1();
        break; 
       case 7:                                            
         //Serial.println("servo left Arm");
        servoarm2();
        break;  
       case 8:                                            
         //Serial.println("automatic moves");
        automatic();
        break;  
       case 9:                                            
         //Serial.println("GRASS CUT");
        grasscut();
        break;  
        case 0:                                            
         //Serial.println("NOGRASS CUT");
        nograsscut();
        break;
        case 10:                                            
         //Serial.println("ARM 1 UP");
        servoarm1up();
        break;
        case 11:                                            
         //Serial.println("ARM 2 UP");
        servoarm2up();
        break;     
  }
 }                                                           
   if (Genotronex.available() < 0)                              
    {
     //Serial.println("No Bluetooth Data ");          
    }
}
void forward()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}
void reverse()
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}
void left()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}
void right()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}
void stoprobot()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}
void servoarm1()
{
      Servo1.write(90); 
   delay(1000); 
   // Make servo go to 90 degrees 
   Servo1.write(120); 
   delay(1000); 
   // Make servo go to 180 degrees 
   Servo1.write(90); 
   delay(1000); 

    Servo2.write(70); 
   delay(1000); 
   // Make servo go to 90 degrees 
   Servo2.write(90); 
   delay(1000); 
   // Make servo go to 180 degrees 
   Servo2.write(180); 
   delay(1000);

   asoil();
    delay(1000);
}
void servoarm2()
{
      Servo3.write(90); 
   delay(1000); 
   // Make servo go to 90 degrees 
   Servo3.write(120); 
   delay(1000); 
   // Make servo go to 180 degrees 
   Servo3.write(90); 
   delay(1000); 

    Servo4.write(180); 
   delay(1000); 
   // Make servo go to 90 degrees 
   Servo4.write(90); 
   delay(1000); 
   // Make servo go to 180 degrees 
   Servo4.write(70); 
   delay(1000);
}
void servoarm1up()
{
      Servo1.write(0); 
   delay(1000); 
   // Make servo go to 90 degrees 
   Servo1.write(30); 
   delay(1000); 
   // Make servo go to 180 degrees 
   Servo1.write(30); 
   delay(1000); 

    Servo2.write(0); 
   delay(1000); 
   // Make servo go to 90 degrees 
   Servo2.write(30); 
   delay(1000); 
   // Make servo go to 180 degrees 
   Servo2.write(30); 
   delay(1000);
}
void servoarm2up()
{
      Servo3.write(0); 
   delay(1000); 
   // Make servo go to 90 degrees 
   Servo3.write(30); 
   delay(1000); 
   // Make servo go to 180 degrees 
   Servo3.write(30); 
   delay(1000); 

    Servo4.write(0); 
   delay(1000); 
   // Make servo go to 90 degrees 
   Servo4.write(30); 
   delay(1000); 
   // Make servo go to 180 degrees 
   Servo4.write(30); 
   delay(1000);
}

void grasscut()
{
  digitalWrite(IN11, LOW);
  digitalWrite(IN12, HIGH);  
}
void nograsscut()
{
  digitalWrite(IN11, LOW);
  digitalWrite(IN12, LOW);  
}

void asoil()
{
  Serial.print("Soil Moisture = ");    
  //get soil moisture value from the function below and print it
   delay(10);//wait 10 milliseconds 
    val = analogRead(soilPin);//Read the SIG value from sensor   
  Serial.println(val);
  delay(1000);//take a reading every second
}
//
//int readSoil()
//{
//    delay(10);//wait 10 milliseconds 
//    val = analogRead(soilPin);//Read the SIG value from sensor 
//    return val;//send current moisture value
//}

void automatic()
{
  int distanceRight = 0;
  int distanceLeft = 0;
  delay(50);
  Serial.println(distance);
  Genotronex.begin(9600);
  Genotronex.println(distance);
  if (distance <= 20){
    moveStop();
    delay(300);
    moveBackward();
    delay(400);
    moveStop();
    delay(300);
    distanceRight = lookRight();
    delay(300);
    distanceLeft = lookLeft();
    delay(300);

    if (distance >= distanceLeft){
      turnRight();
      moveStop();
    }
    else{
      turnLeft();
      moveStop();
    }
  }
  else{
    moveForward(); 
  }
    distance = readPing();
}

int lookRight(){  
  servo_motor.write(50);
  delay(500);
  int distance = readPing();
  delay(100);
  servo_motor.write(115);
  return distance;
}

int lookLeft(){
  servo_motor.write(170);
  delay(500);
  int distance = readPing();
  delay(100);
  servo_motor.write(115);
  return distance;
  delay(100);
}

int readPing(){
  delay(70);
  int cm = sonar.ping_cm();
  if (cm==0){
    cm=250;
  }
  return cm;
}

void moveStop(){
  
  digitalWrite(IN3, LOW);
  digitalWrite(IN1, LOW);
  digitalWrite(IN4, LOW);
  digitalWrite(IN2, LOW);
}

void moveForward(){

  if(!goesForward){

    goesForward=true;
    
    digitalWrite(IN1, LOW);
    digitalWrite(IN3, LOW);
  
    digitalWrite(IN2, HIGH);
    digitalWrite(IN4, HIGH); 
  }
}

void moveBackward(){

  goesForward=false;

  digitalWrite(IN2, LOW);
  digitalWrite(IN4, LOW);  
  digitalWrite(IN1, HIGH);
  digitalWrite(IN3, HIGH);
  
}

void turnRight(){

  digitalWrite(IN1, HIGH);
  digitalWrite(IN4, HIGH);
  
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  
  delay(500);
  
  digitalWrite(IN1, HIGH);
  digitalWrite(IN3, HIGH);
  
  digitalWrite(IN2, LOW);
  digitalWrite(IN4, LOW);
 
  
  
}

void turnLeft(){

  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  
  digitalWrite(IN1, LOW);
  digitalWrite(IN4, LOW);

  delay(500);
  
  digitalWrite(IN1, HIGH);
  digitalWrite(IN3, HIGH);
  
  digitalWrite(IN2, LOW);
  digitalWrite(IN4, LOW);
}


