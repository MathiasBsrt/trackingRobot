import RPi.GPIO as GPIO 
from time import sleep

'''
This class represent a motor DC
'''
class MotorDC:
    AN = 25
    DIG = 23
    p = 0
    def __init__(self,AN,DIG):
        self.AN = AN
        self.DIG = DIG
        GPIO.setmode(GPIO.BCM) # GPIO numbering
        GPIO.setwarnings(False) # enable warning from GPIO

        GPIO.setup(self.DIG, GPIO.OUT) # set pin as output
        GPIO.setup(self.AN, GPIO.OUT) # set pin as output
        sleep(1) # delay for 1 seconds
        self.p = GPIO.PWM(AN, 100) # set pwm for M1

    '''
    This function allow the motor to go forward
    @param speed of the motor speed=0 – 100
    '''
    def forward(self, speed):
        GPIO.output(self.DIG, GPIO.HIGH) # set DIG1 as high, dir2 = forward
        p.start(speed) # set speed for M1, speed=0 – 100
    
        '''
    This function allow the motor to go backward
    @param speed of the motor speed=0 – 100
    '''
    def backward(self, speed):
        GPIO.output(self.DIG, GPIO.LOW) # set DIG1 as low, direction = backward
        p.start(speed) # set speed for M1, speed=0 – 100
    