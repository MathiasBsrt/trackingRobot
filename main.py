#!/usr/bin/env python3
from __future__ import division
import cv2
import numpy as np
import time
from MotorDC import MotorDC

motorControl = MotorDC() #Create motor control object

def nothing(*arg):
        pass

#Picture size
FRAME_WIDTH = 320
FRAME_HEIGHT = 240

#Need to recognize red obejects
lowHue = 50
lowSat = 112
lowVal = 124
highHue = 255
highSat = 255
highVal = 255
speed = 0.9 #Motor speed (between 0 et 1)

# Camera init
vidCapture = cv2.VideoCapture(0)
vidCapture.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
vidCapture.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)

while True:
    timeCheck = time.time()

    # Get image
    _, frame = vidCapture.read()


    #Convert to HSV base
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Define MASK to keep red parts
    colorLow = np.array([lowHue,lowSat,lowVal])
    colorHigh = np.array([highHue,highSat,highVal])
    mask = cv2.inRange(frameHSV, colorLow, colorHigh)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Creation of contours
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    
    if(contour_sizes):
        print("empty")
        biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        x,y,w,h = cv2.boundingRect(biggest_contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) #Apply contours on the picture
        #Divide image in 3 columns (left,center, right)
        if(x<FRAME_WIDTH/3):
            motorControl.right(speed)
            print("right")
        elif(x>=FRAME_WIDTH/3 and x<(FRAME_WIDTH-(FRAME_HEIGHT/3))):
            print("forward")
            motorControl.forward(speed)
        else:
            motorControl.left(speed)
            print("left")
    else:
        motorControl.stop()
        print("no red object...")
	
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
vidCapture.release()
