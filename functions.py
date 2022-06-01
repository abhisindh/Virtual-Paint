
from classes import *


def empty(a):
    pass


def startWebcam(frameWidth = 640,frameHeight = 480,brightness = 130):
    cap = cv2.VideoCapture(0)
    cap.set(3,frameWidth)
    cap.set(4,frameHeight)
    cap.set(10,brightness)

    for trackbar in TrackBar.instances:
            print(trackbar.name)

            
    while True:
        success, img = cap.read()
        for window in Window.instances:
            img = window.manipulate(img)
            cv2.imshow(window.name,img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('quitting')
            break


def createTrackBar(name='name',in_value=0,max_value=100):
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars",640,240)
    cv2.createTrackbar(name,"TrackBars",in_value,max_value,empty)

def addMask(img):
    lower = np.array([5,107,0])
    upper = np.array([5,107,0])
    mask = cv2.inRange(img,lower,upper)
    return mask



def findColor(img,color):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

def toHSV(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    return imgHSV



if __name__=='__main__':
    startWebcam()
    
