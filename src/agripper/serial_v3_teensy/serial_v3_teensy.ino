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

int NoNcPin123 = 12;// normaly open/close for all sensors
//st1
int driverPUL1 = 0;    // PUL- pin
int driverDIR1 = 1;    // DIR- pin
int sigPin1_start = 2; // switch signal
int sigPin1_end  = 3; // switch signal
int irsPin1_start = 4; // connected to switch signal (sigPin) for homing
int irsPin1_end = 5; // connected to switch signal (sigPin) for end limit

//st2
int driverPUL2 = 14;    // PUL- pin
int driverDIR2 = 15;    // DIR- pin
int sigPin2_start = 16; // switch signal
int sigPin2_end = 17; // normaly open/close
int irsPin2_start = 18; // connected to switch signal (sigPin) for homing
int irsPin2_end = 19; // connected to switch signal (sigPin) for end limit

//st3
int driverPUL3 = 6;    // PUL- pin
int driverDIR3 = 7;    // DIR- pin
int sigPin3_start = 8; // swithc signal
int sigPin3_end = 9; 
int irsPin3_start = 10; // connected to switch signal for homing
int irsPin3_end = 11; // connected to switch signal (sigPin) for end limit


//int enablePin = 13; // emer. stop TEMP
int buttonPin = 12;

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

  pinMode(buttonPin, INPUT_PULLUP);
  pinMode (13, OUTPUT);
  pinMode(NoNcPin123, OUTPUT);
  digitalWrite(NoNcPin123, LOW);
  
  pinMode(sigPin1_start, INPUT_PULLUP);
  pinMode(sigPin1_end, INPUT_PULLUP);
  pinMode(sigPin2_start, INPUT_PULLUP);
  pinMode(sigPin2_end, INPUT_PULLUP);
  pinMode(sigPin3_start, INPUT_PULLUP);
  pinMode(sigPin3_end, INPUT_PULLUP);
    
  attachInterrupt(digitalPinToInterrupt(irsPin1_start), stop_motor1, FALLING);
  attachInterrupt(digitalPinToInterrupt(irsPin1_end), rev_motor1, FALLING);
  attachInterrupt(digitalPinToInterrupt(irsPin2_start), stop_motor2, FALLING);
  attachInterrupt(digitalPinToInterrupt(irsPin2_end), rev_motor2, FALLING);
  attachInterrupt(digitalPinToInterrupt(irsPin3_start), stop_motor3, FALLING);
  attachInterrupt(digitalPinToInterrupt(irsPin3_end), rev_motor3, FALLING);
  
  
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
    digitalWrite(13, !digitalRead(13));
  }
  stepNow[0] = stepper1.currentPosition();
  stepNow[1] = stepper2.currentPosition();
  stepNow[2] = stepper3.currentPosition();
  current_step_msg.data = stepNow;
  stepper1.run();
  //if (stepNow[0] <= 1300 && abs(stepNow[1]) <= 910) {// CHANGE !!! NOT GOOD
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
        nh.loginfo("Im at the home position.");
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



void stop_motor1()//function activated by the pressed microswitch
{
  
  //Stop motor, disable outputs; here we should also reset the numbers if there are any
  //runallowed = false; //disable running // ADD COND. TO MAIN ?
  stepper1.stop(); //stop motor 
  stepper1.setCurrentPosition(0);  // reset position
  stepper1.move(3);
  nh.loginfo("No.1 REACHED START & STOPED, Position sets to 0"); //feedback towards the serial port
  digitalWrite(13, HIGH-digitalRead(13));
  stepper1.disableOutputs();//disable power
}


void rev_motor1()//function activated by the pressed microswitch
{
  
  stepper1.stop(); //stop motor 
  stepper1.setCurrentPosition(6760); // limit 520 mm
  stepper1.move(-4);
  nh.loginfo("No.1 REACHED END LIMIT");
  digitalWrite(13, HIGH-digitalRead(13));
}



void stop_motor2()//function activated by the pressed microswitch
{
  
  //Stop motor, disable outputs; here we should also reset the numbers if there are any
  //runallowed = false; //disable running // ADD COND. TO MAIN ?
  stepper2.stop(); //stop motor 
  stepper2.setCurrentPosition(0);  // reset position
  stepper2.move(-2);
  nh.loginfo("No.2 REACHED START & STOPED, Position sets to 0"); //feedback towards the serial port
  digitalWrite(13, HIGH-digitalRead(13));
  stepper2.disableOutputs();//disable power
}


void rev_motor2()//function activated by the pressed microswitch
{
  
  stepper2.stop(); //stop motor 
  //stepper2.moveTo(500); // limit
  nh.loginfo("No.2 REACHED END LIMIT");
  digitalWrite(13, HIGH-digitalRead(13));
}



void stop_motor3()//function activated by the pressed microswitch
{
  
  //Stop motor, disable outputs; here we should also reset the numbers if there are any
  //runallowed = false; //disable running // ADD COND. TO MAIN ?
  stepper3.stop(); //stop motor 
  stepper3.setCurrentPosition(0);  // reset position
  stepper3.move(-2);
  nh.loginfo("No.3 REACHED START & STOPED, Position sets to 0"); //feedback towards the serial port
  digitalWrite(13, HIGH-digitalRead(13));
  stepper3.disableOutputs();//disable power
}


void rev_motor3()//function activated by the pressed microswitch
{
  
  stepper3.stop(); //stop motor 
  //stepper3.moveTo(500); // limit
  nh.loginfo("No.3 REACHED END LIMIT");
  digitalWrite(13, HIGH-digitalRead(13));
}
