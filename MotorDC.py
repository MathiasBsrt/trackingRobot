import time
import board
from adafruit_motorkit import MotorKit

'''
This class describe DC Motors
'''
class MotorDC:
    kit = 0
    def __init__(self):
        i2c=111
        print(i2c)
        self.kit = MotorKit(i2c)

    '''
    This function allow the robot to go forward
    @param speed 
    '''
    def forward(self, speed):
        self.kit.motor1.throttle = speed
        self.kit.motor2.throttle = speed
    
    '''
    This function allow the robot to go backward
    @param speed 
    '''
    def backward(self, speed):
        self.kit.motor1.throttle = -speed
        self.kit.motor2.throttle = -speed
    '''
    This function allow the robot to turn right
    @param speed 
    '''
    def right(self,speed):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = speed

    '''
    This function allow the robot to turn left
    @param speed 
    '''
    def left(self,speed):
        self.kit.motor1.throttle = speed
        self.kit.motor2.throttle = 0
    '''
    This function allow the robot to stop
    '''
    def stop(self):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0


    


    
