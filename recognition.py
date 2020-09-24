import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
'''
This function return the location of the object with the provided hue_value
@param hue_value : number between 10 and 245 which is the color.
See http://www.workwithcolor.com for more informations
@return object_location : [object_area, object_x, object_y] or False if no image can be procesed
'''

def objectRecognition(hue_value,rawCapture,camera):
    #Take image from camera
    print("object reco")
    frame = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)[0]
    image = frame.array

    image_width = 640
    image_height = 480
    center_image_x = image_width / 2
    center_image_y = image_height / 2
    minimum_area = 250
    maximum_area = 100000

    hue_value = 25 #Pour une balle de ping pong
    lower_color = np.array([hue_value-10,100,100])
    upper_color = np.array([hue_value+10, 255, 255])

    # Décomposition de l'image pour obtenir l'objet recherché
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV) 
    color_mask = cv2.inRange(hsv, lower_color, upper_color)
    countours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    object_area = 0
    object_x = 0
    object_y = 0
    
    for contour in countours:
        x, y, width, height = cv2.boundingRect(contour)
        found_area = width * height
        center_x = x + (width / 2)
        center_y = y + (height / 2)
        if object_area < found_area:
            object_area = found_area
            object_x = center_x
            object_y = center_y

    if object_area > 0:
        object_location = [object_area, object_x, object_y]
    else:
        object_location = None
        
    return object_location
