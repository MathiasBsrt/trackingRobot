import time
import board
from adafruit_motorkit import MotorKit

'''
Cette classe représente un moteur DC
'''
class MotorDC:
    kit = 0
    def __init__(self):
        i2c=111
        print(i2c)
        self.kit = MotorKit(i2c)

    '''
    Cette fonction permet au robot d'aller en avant
    @param speed : vitesse des moteurs (0 - 1)
    '''
    def forward(self, speed):
        self.kit.motor1.throttle = speed
        self.kit.motor2.throttle = speed
    
    '''
    Cette fonction permet au robot d'aller en arrière
    @param speed : vitesse des moteurs (0 - 1)
    '''
    def backward(self, speed):
        self.kit.motor1.throttle = -speed
        self.kit.motor2.throttle = -speed
    '''
    Cette fonction permet au robot de tourner à droite
    @param speed : vitesse des moteurs (0 - 1)
    '''
    def right(self,speed):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = speed

    '''
    Cette fonction permet au robot de tourner à gauche
    @param speed : vitesse des moteurs (0 - 1)
    '''
    def left(self,speed):
        self.kit.motor1.throttle = speed
        self.kit.motor2.throttle = 0
    '''
    Cette fonction permet au robot de s'arrêter
    @param speed : vitesse des moteurs (0 - 1)
    '''
    def stop(self):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0


    


    
