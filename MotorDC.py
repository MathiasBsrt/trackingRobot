import time
import board
from adafruit_motorkit import MotorKit

'''
This class represent a motor DC
'''
class MotorDC:
    kit = 0
    def __init__(self):
        self.kit = MotorKit(i2c=board.I2C())

    '''
    This function allow the motor to go forward
    @param speed of the motor speed=0 – 100
    '''
    def forward(self, speed):
        kit.motor1.throttle = speed
        kit.motor2.throttle = speed

    
        '''
    This function allow the motor to go backward
    @param speed of the motor speed=0 – 100
    '''
    def backward(self, speed):
        kit.motor1.throttle = -speed
        kit.motor2.throttle = -speed

    def right(self,speed):
        kit.motor1.throttle = speed
        kit.motor2.throttle = 0

    def right(self,speed):
        kit.motor1.throttle = 0
        kit.motor2.throttle = speed
    
    def stop(self):
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0



    


    