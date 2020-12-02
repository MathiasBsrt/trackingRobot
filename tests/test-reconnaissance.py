import cv2
import numpy as np
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

#while True:
#    try:
#        hue_value = int(input("Hue value between 10 and 245: "))
#        if (hue_value < 10) or (hue_value > 245):
#            raise ValueError
#    except ValueError:
#        print("That isn't an integer between 10 and 245, try again")
#    else:
#        break
hue_value = 25 #A modifier en fonction de la couleur que l'on veut : http://www.workwithcolor.com
lower_red = np.array([hue_value-10,100,100])
upper_red = np.array([hue_value+10, 255, 255])
while rval:
    rval, image = vc.read()

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
    color_mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(image, image, mask= color_mask)
 
    cv2.imshow("Camera Output", image)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Color Mask", color_mask)
    cv2.imshow("Final Result", result)
 
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")