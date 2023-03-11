# Import library
from Motor import *
from Buzzer import *
from Led import *
import time
# Import neccesssary functions
PWM=Motor()
led=Led()
buzzer=Buzzer()
# The main loop is here. Simply copy the functions from the template code and modify it.
try:
    # moving forward
    PWM.setMotorModel(1000,1000,1000,1000)
    print("The car is moving forward")
    time.sleep(2)
    # turn left (rotate 90 degrees)
    PWM.setMotorModel(-1500,-1500,2000,2000)       
    print ("turn left")
    time.sleep(1)
    # This is the index for red color led
    led.ledIndex(0x01,255,0,0)      
    print ("The led has been lit with color Red")
    
    # moving forward
    PWM.setMotorModel(1000,1000,1000,1000)
    print("The car is moving forward")
    time.sleep(2)
    # turn left (rotate 90 degrees)
    PWM.setMotorModel(-1500,-1500,2000,2000)       
    print ("The car is turning left")
    time.sleep(1)
    # This is the index for blue color led
    led.ledIndex(0x02,0,0,255)      
    print ("The led has been lit with color Blue")
    
    # moving forward
    PWM.setMotorModel(1000,1000,1000,1000)
    print("The car is moving forward")
    time.sleep(2)
    # turn left (rotate 90 degrees)
    PWM.setMotorModel(-1500,-1500,2000,2000)       
    print ("The car is turning left")
    time.sleep(1)
    # This is the index for blue color green
    led.ledIndex(0x04,0,255,0)    
    print ("The led has been lit with color Green")
    
    # This is the last block in the main loop. The car will move forward, turn left, beep and stop.
    PWM.setMotorModel(1000,1000,1000,1000)
    print("The car is moving forward")
    time.sleep(2)
    PWM.setMotorModel(-1500,-1500,2000,2000)        
    # turn left (rotate 90 degrees)
    print ("The car is turning left") 
    time.sleep(1)
    # This is the index for blue color Yellow
    led.ledIndex(0x08,255,255,0)      
    print ("The led 3 has been lit with color Yellow")
    # Stop the robot
    PWM.setMotorModel(0,0,0,0)
    print ("Motor is dead now")  
    # sleep for 2 second
    time.sleep(2)   
    # turn off the red led
    led.colorWipe(led.strip, Color(0,0,0))  
    print ("Led is dead")
    # Let Buzzer beep for 1 second
    buzzer.run('1')   
    print ("Buzzer beeps for 1 second") 
    time.sleep(1)
    # Stop the buzzer and finish
    buzzer.run('0')    
    
# The usage is to interrupt the program with keyboard input
except KeyboardInterrupt:
    # This command will stop the motor
    PWM.setMotorModel(0,0,0,0)
    # The following command will stop the led and the buzzer.
    led.colorWipe(led.strip, Color(0,0,0))  #turn off the light
    buzzer.run('0')    
    print ("\nProgram end because of keyboard interrupt")
