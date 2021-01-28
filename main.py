#!/usr/bin/env python3
from __future__ import division
import cv2
import numpy as np
import time
from MotorDC import MotorDC

motorControl = MotorDC() #creation de 'objet qui cntrole les moteurs

def nothing(*arg):
        pass

#taille de l'image
FRAME_WIDTH = 320
FRAME_HEIGHT = 240

#Utilisation du rouge
lowHue = 50
lowSat = 112
lowVal = 124
highHue = 255
highSat = 255
highVal = 255
speed = 0.9 #vitesse des moteurs (entre 0 et 1)

# Initialisation de la camera
vidCapture = cv2.VideoCapture(0)
vidCapture.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
vidCapture.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)

while True:
    timeCheck = time.time()

    # Récuparation de l'image
    _, frame = vidCapture.read()


    #conversion de l'image vers la base HSV.
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Valeurs HSV pour définir le masque et seulement garder l'encadrement de couleur que l'on souhaite
    colorLow = np.array([lowHue,lowSat,lowVal])
    colorHigh = np.array([highHue,highSat,highVal])
    mask = cv2.inRange(frameHSV, colorLow, colorHigh)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #création des contours de l'objet correpsondant à la couleur
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    
    if(contour_sizes):
        print("empty")
        biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        x,y,w,h = cv2.boundingRect(biggest_contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) #application du contour sur l'image
        #Division de l'image en 3
        if(x<FRAME_WIDTH/3):
            motorControl.right(speed)
            print("droite")
        elif(x>=FRAME_WIDTH/3 and x<(FRAME_WIDTH-(FRAME_HEIGHT/3))):
            print("AVANT")
            motorControl.forward(speed)
        else:
            motorControl.left(speed)
            print("gauche")
    else:
        motorControl.stop()
        print("aucun objet rouge...")
	
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
vidCapture.release()
