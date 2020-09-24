import RPi.GPIO as GPIO 
from time import sleep
from MotorDC import MotorDC
'''
This class control the sensors and acuators of the robot
'''
class Robot:
    motor1 = 0
    motor2 = 0
    def __init__(self):
        self.motor1 = MotorDC(25,23)
        self.motor2 = MotorDC(24,18)
    '''
    This function allow the robot to go forward
    @param speed of the robot
    '''
    def forward(self, speed):
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
    
    