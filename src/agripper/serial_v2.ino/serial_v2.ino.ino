//serial_node beta 

// ----------LIBRARIES--------------
#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/Int32MultiArray.h>
#include <std_msgs/String.h>
#include <AccelStepper.h>
//IntervalTimer myTimer; //Cannot use with uno :( 

// --------CONSTANTS---------------
const uint8_t arrayLength_stepsR = 3;
//st1
int driverPUL1 = 0;    // PUL- pin
int driverDIR1 = 1;    // DIR- pin
int irsPin1 = 2; // connected to switch signal for homing
int sigPin1 = 6; // swithc signal
int NoNcPin1 = 7; // normaly open/close
//st2
int driverPUL2 = 8;    // PUL- pin
int driverDIR2 = 9;    // DIR- pin
int irsPin2 = 3; // connected to switch signal for homing
int sigPin2 = 10; // swithc signal
int NoNcPin2 = 11; // normaly open/close
//st3
int driverPUL3 = A0;    // PUL- pin
int driverDIR3 = A1;    // DIR- pin
//int irsPin3 = 3; // connected to switch signal for homing
int sigPin3 = A2; // swithc signal
int NoNcPin3 = A3; // normaly open/close

//int enablePin = 3; // emer. stop TEMP
//int buttonPin = 12;

int MaxSpeed = 200;
int Acceleration = 75;

//------------VARIABLES---------------------
bool sensorValue = LOW;
//bool setdir = LOW; // Set Direction 
long int stepNow[] = {0, 0, 0};

volatile bool runallowed = false; // booleans for new data from serial, and runallowed flag
long previousMillis = 0;
unsigned int delta = 1000;
bool flag = HIGH;
//----------------------
ros::NodeHandle  nh;
AccelStepper stepper1(1, driverPUL1, driverDIR1);
AccelStepper stepper2(1, driverPUL2, driverDIR2);
AccelStepper stepper3(1, driverPUL3, driverDIR3); 

//------------CALLBACKS---------------------

void cb_move( const std_msgs::Float32MultiArray& msg ) {
  
  stepper1.setMaxSpeed(MaxSpeed); // TODO change to a define const. 
  stepper1.setAcceleration(Acceleration);
  stepper1.moveTo(msg.data[0]);
  
  stepper2.setMaxSpeed(MaxSpeed); // TODO change to a define const. 
  stepper2.setAcceleration(Acceleration);
  stepper2.moveTo(msg.data[1]);

  stepper3.setMaxSpeed(MaxSpeed); // TODO change to a define const. 
  stepper3.setAcceleration(Acceleration);
  stepper3.moveTo(msg.data[2]);
  
  
}

void cb_home( const std_msgs::String& msg ) {
  homing();
  
  
}

//========================================

ros::Subscriber<std_msgs::Float32MultiArray> steps_sub("write/steps", cb_move);
ros::Subscriber<std_msgs::String> home_sub("home", cb_home);

std_msgs::Int32MultiArray current_step_msg;
ros::Publisher pub_step("read/current_step", &current_step_msg);


void setup() {

  nh.initNode();
  nh.subscribe(steps_sub);
  nh.subscribe(home_sub);
  
  current_step_msg.data_length = arrayLength_stepsR;
  nh.advertise(pub_step);
//  stepNow = stepper1.currentPosition();
  
  stepper1.setMaxSpeed(MaxSpeed); // TODO change to a define const. 
  stepper1.setAcceleration(Acceleration);
//  stepper1.disableOutputs(); // Does nothing ?

  stepper2.setMaxSpeed(MaxSpeed); // TODO change to a define const. 
  stepper2.setAcceleration(Acceleration); 
//  stepper2.disableOutputs();
  
  stepper3.setMaxSpeed(MaxSpeed); // TODO change to a define const. 
  stepper3.setAcceleration(Acceleration); 
//  stepper3.disableOutputs();
  
  pinMode(sigPin1, INPUT_PULLUP);
  //pinMode(buttonPin, INPUT_PULLUP);
  pinMode (13, OUTPUT);
  pinMode (driverPUL1, OUTPUT);
  pinMode (driverDIR1, OUTPUT);
  
  attachInterrupt(digitalPinToInterrupt(irsPin1), stop_motor, FALLING);
//  attachInterrupt(digitalPinToInterrupt(enablePin), natural, LOW);
  
  //pinMode(NoNcPin, OUTPUT);
//  myTimer.begin(Publish_Timer, 35000);
}

//========================================
/* void Publish_Timer() {  
  
  current_step_msg.data[0] = stepper1.currentPosition();
  pub_step.publish( &current_step_msg );

}*/


void loop() {
  
  if(millis() - previousMillis > delta) {
    pub_step.publish( &current_step_msg ); 
    previousMillis += delta;   
  }
  stepNow[0] = stepper1.currentPosition();
  stepNow[1] = stepper2.currentPosition();
  stepNow[2] = stepper3.currentPosition();
  current_step_msg.data = stepNow;
  stepper1.run();
  //if (stepNow[0] >= 1300 && ) {
  stepper2.run();
  //}
  
  stepper3.run();
  
  nh.spinOnce();
//  delay(1);
//delayMicroseconds()
}

//========================================



void homing (){
  if (stepper1.currentPosition() == 0)
    {
        nh.loginfo("We are at the home position.");
        stepper1.disableOutputs(); //disable power
    }
  else
    {
        stepper1.enableOutputs();
        stepper1.setMaxSpeed(75); //set speed manually to 400. In this project 400 is 400 step/sec = 1 rev/sec.
        stepper1.moveTo(-6500); //set abolute distance to move
        //runallowedX = false; //disable running // ADD COND. TO MAIN ?    
    }
}



void stop_motor()//function activated by the pressed microswitch
{
  
  //Stop motor, disable outputs; here we should also reset the numbers if there are any
  //runallowed = false; //disable running // ADD COND. TO MAIN ?
  stepper1.stop(); //stop motor 
  stepper1.setCurrentPosition(0);  // reset position
  stepper1.move(2);
  nh.loginfo("REACHED LIMIT & STOPED, Position sets to 0"); //feedback towards the serial port
  digitalWrite(13, HIGH-digitalRead(13));
  stepper1.disableOutputs();//disable power
}



void natural () {
  nh.logerror("Interupted");
}
