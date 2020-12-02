import RPi.GPIO as GPIO 
from time import sleep
from MotorDC import MotorDC

'''
This class control the sensors and acuators of the robot
'''
class Robot:

    def __init__(self):
        print("init motors")
    '''
    This function allow the robot to go forward
    @param speed of the robot
    '''
    def forward(self, speed):
        print("forward !!!")
        motor1.forward(speed)
        motor2.forward(speed)

    
    '''
    This function allow the robot to go backward
    @param speed of the robot
    '''
    def backward(self, speed):
        motor1.backward(speed)
        motor2.backward(speed)

    '''
    This function allow the robot to go right
    @param speed of the robot
    '''
    def turnRight(self, speed):
        motor1.forward(speed)
        motor2.backward(speed)

    '''
    This function allow the robot to turn left
    @param speed of the robot
    '''
    def turnLeft(self, speed):
        motor1.forward(speed)
        motor2.backward(speed)

    '''
    This function stop the robot
    @param speed of the robot
    '''
    def turnLeft(self):
        motor1.forward(0)
        motor2.backward(0)
    
    