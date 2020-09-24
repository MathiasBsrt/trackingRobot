import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import recognition
from Robot import Robot

image_width = 640
image_height = 480
center_image_x = image_width / 2
center_image_y = image_height / 2
minimum_area = 250
maximum_area = 100000
turn_speed = 50
speed = 85
robot = Robot() #Create Robot controller

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Le programme se décompose en 2 états :
'''
Atteindre la balle : reachBall
Pousser la balle dans le l'enclos : pushBall
'''
while(True):
    ball_location = recognition.objectRecognition(25, rawCapture, camera)
    #Action à faire en fonction de la localisation de la balle
    if ball_location:
        if (ball_location[0] > minimum_area) and (ball_location[0] < maximum_area):
            if ball_location[1] > (center_image_x + (image_width/3)):
                print("ON TOURNE A DROITE")
                #robot.turnRight(turn_speed)
            elif ball_location[1] < (center_image_x - (image_width/3)):
                print("ON TOURNE A GAUCHE")
                #robot.turnLeft(turn_speed)
            else:
                #robot.forward(speed)
                print("EN AVANT !")
        elif (ball_location[0] < minimum_area):
            #robot.turnLeft(turn_speed)
            print("On ne voit pas balle...")
        else:
            #robot.stop()
            print("on est assez proche")
    else:
        #robot.turnLeft(turn_speed)
        print("On ne trouve vraiment rien.")