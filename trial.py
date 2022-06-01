import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    

    lower = np.array([8,213,105])
    upper = np.array([91,250,243])
    Orangemask = cv2.inRange(frame,lower,upper)
    orangeMask = cv2.bitwise_and(frame,frame,mask=mask)

    lower = np.array([158,99,131])
    upper = np.array([173,186,255])
    mask = cv2.inRange(frame,lower,upper)
    cv2.imshow('Window',frame)
    cv2.imshow('Pink',mask)
    cv2.imshow('orange',orangeMask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break