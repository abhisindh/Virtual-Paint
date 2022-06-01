import cv2
import numpy as np
import time

def empty(a):
    pass

def back(*args):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('trackbars')

cv2.createButton("Back",back,None,cv2.QT_PUSH_BUTTON,1)



cv2.createTrackbar('Hue Min','trackbars',0,179,empty)
cv2.createTrackbar('Hue Max','trackbars',179,179,empty)
cv2.createTrackbar('Sat Min','trackbars',0,255,empty)
cv2.createTrackbar('Sat Max','trackbars',255,255,empty)
cv2.createTrackbar('Val Min','trackbars',0,255,empty)
cv2.createTrackbar('Val Max','trackbars',255,255,empty)

while True:

    h_min = cv2.getTrackbarPos('Hue Min','trackbars')
    h_max = cv2.getTrackbarPos('Hue Max','trackbars')
    s_min = cv2.getTrackbarPos('Sat Min','trackbars')
    s_max = cv2.getTrackbarPos('Sat Max','trackbars')
    v_min = cv2.getTrackbarPos('Val Min','trackbars')
    v_max = cv2.getTrackbarPos('Val Max','trackbars')

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    


    success , frame = cap.read()
    imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV,lower,upper)
    cv2.imshow('Webcam',frame)
    cv2.imshow('HSV', imgHSV)
    cv2.imshow('Mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break