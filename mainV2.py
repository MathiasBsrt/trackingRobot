#!/usr/bin/env python3
from __future__ import division

"""
Programme principal du robot traqueur d'objet.
Le robot suit un objet d'une couleur définit.


Author:     Mark Heywood
Date:	    31/12/2017
Version     0.1.0

Sources : https://www.bluetin.io/opencv/opencv-color-detection-filtering-python/
"""
import cv2
import numpy as np
import time

def nothing(*arg):
        pass

#Costantes
FRAME_WIDTH = 320
FRAME_HEIGHT = 240

#Utilisation du rouge
lowHue = 50
lowSat = 112
lowVal = 124
highHue = 255
highSat = 255
highVal = 255
forward_speed = 0.7
turn_speed = 0.5

# Initialisation de la camera
vidCapture = cv2.VideoCapture(0)
vidCapture.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
vidCapture.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)

while True:
    timeCheck = time.time()

    # Get frame
    _, frame = vidCapture.read()


    # Convert the frame to HSV colour model.
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # HSV values to define a colour range we want to create a mask from.
    colorLow = np.array([lowHue,lowSat,lowVal])
    colorHigh = np.array([highHue,highSat,highVal])
    mask = cv2.inRange(frameHSV, colorLow, colorHigh)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    
    if(contour_sizes):
        print("empty")
        biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        x,y,w,h = cv2.boundingRect(biggest_contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        print("x="+str(x))
        if(x<FRAME_WIDTH/3):
            #motorControl.left(turn_speed)
            print("gauche")
        elif(x>=FRAME_WIDTH/3 and x<(FRAME_WIDTH-(FRAME_HEIGHT/3))):
            print("AVANT")
            #motorControl.forward(forward_speed)
        else:
           # motorControl.right(turn_speed)
            print("droite")
    else:
        #motorControl.left(turn_speed)
        print("aucun objet rouge...")



    # Show final output image
    cv2.imshow('colorTest', frame)
	
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
vidCapture.release()
