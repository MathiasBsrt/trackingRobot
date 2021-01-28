import time
import board
from adafruit_motorkit import MotorKit

'''
This class represent a motor DC
'''
class MotorDC:
    kit = 0
    def __init__(self):
        i2c=111
        print(i2c)
        self.kit = MotorKit(i2c)

    '''
    This function allow the motor to go forward
    @param speed of the motor speed=0 – 100
    '''
    def forward(self, speed):
        self.kit.motor1.throttle = 0.9
        self.kit.motor2.throttle = 0.9
    
        '''
    This function allow the motor to go backward
    @param speed of the motor speed=0 – 100
    '''
    def backward(self, speed):
        self.kit.motor1.throttle = -speed
        self.kit.motor2.throttle = -speed

    def right(self,speed):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0.9

    def left(self,speed):
        self.kit.motor1.throttle = 0.9
        self.kit.motor2.throttle = 0
    
    def stop(self):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0


    


    
