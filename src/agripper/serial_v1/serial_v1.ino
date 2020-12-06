//new
//serial_node beta 

// ----------LIBRARIES--------------
#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/Int32MultiArray.h>
#include <std_msgs/String.h>
#include <AccelStepper.h>
//IntervalTimer myTimer; //Cannot use with uno :( 


// --------CONSTANTS---------------
const uint8_t arrayLength_steps = 3;

int sigPin = 9; // swithc signal
int NoNcPin = 8; // normaly open/close
int reverseSwitch = 2; // connected to switch signal for reverse
int driverPUL = 7;    // PUL- pin
int driverDIR = 6;    // DIR- pin
int enablePin = 3;
int buttonPin = 4;


//------------VARIABLES---------------------
bool sensorValue = LOW;
bool setdir = LOW; // Set Direction 
long int stepNow[] = {0, 0, 0};

volatile bool runallowed = false; // booleans for new data from serial, and runallowed flag
long previousMillis = 0;
int delta = 1000;
//----------------------
ros::NodeHandle  nh;
AccelStepper stepper(1, driverPUL, driverDIR); // AccelStepper stepper(1,7,6);

//------------CALLBACKS---------------------

void cb_move( const std_msgs::Float32MultiArray& msg ) {
  
  stepper.setMaxSpeed(500); // TODO change to a define const. 
  stepper.setAcceleration(250);
  stepper.moveTo(msg.data[0]);
  
  digitalWrite(13, HIGH-digitalRead(13));
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
  
  current_step_msg.data_length = arrayLength_steps;
  nh.advertise(pub_step);
//  stepNow = stepper.currentPosition();
  
  stepper.setMaxSpeed(500); // TODO change to a define const. 
  stepper.setAcceleration(250);
  stepper.disableOutputs();
//  stepper.moveTo(1500); 
  
  pinMode(sigPin, INPUT_PULLUP);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode (13, OUTPUT);
  pinMode (driverPUL, OUTPUT);
  pinMode (driverDIR, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(enablePin), natural, LOW);
  attachInterrupt(digitalPinToInterrupt(reverseSwitch), stop_motor, FALLING);
  //pinMode(NoNcPin, OUTPUT);
  //homeing();
//  myTimer.begin(Publish_Timer, 35000);
}

//========================================
/* void Publish_Timer() {  
  
  current_step_msg.data[0] = stepper.currentPosition();
  pub_step.publish( &current_step_msg );

}*/


void loop() {
  
  if(millis() - previousMillis > delta) {
    stepNow[0] = stepper.currentPosition();
    current_step_msg.data = stepNow;
    pub_step.publish( &current_step_msg );
    // save the last time you blinked the LED 
    previousMillis += delta;   
  }
  
  
  nh.spinOnce();
//  delay(1);
//delayMicroseconds()
  stepper.run();
  
}

//========================================



void homing (){
  if (stepper.currentPosition() == 0)
    {
        nh.loginfo("We are at the home position.");
        stepper.disableOutputs(); //disable power
    }
    else
    {
        
    }
  stepper.enableOutputs();
  stepper.setMaxSpeed(75); //set speed manually to 400. In this project 400 is 400 step/sec = 1 rev/sec.
  stepper.moveTo(-6500); //set abolute distance to move

}



void stop_motor()//function activated by the pressed microswitch
{
  
  //Stop motor, disable outputs; here we should also reset the numbers if there are any
  //runallowed = false; //disable running // ADD COND. TO MAIN ?
  stepper.stop(); //stop motor 
  stepper.setCurrentPosition(0);  // reset position
  stepper.move(5);
  stepper.disableOutputs();//disable power
  nh.loginfo("REACHED LIMIT & STOPED, Position sets to 0"); //feedback towards the serial port
}



void natural () {
  nh.logerror("Interupted");
}
