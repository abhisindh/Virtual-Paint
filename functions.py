from classes import *


def empty(a):
    pass


def startWebcam(ColorList=[],frameWidth = 640,frameHeight = 480,brightness = 130):
    cap = cv2.VideoCapture(0)
    cap.set(3,frameWidth)
    cap.set(4,frameHeight)
    cap.set(10,brightness)

            
    while True:
        success, img = cap.read()
        for window in Window.instances:
            #img = frame.copy()
            img = window.manipulate(img)
            cv2.imshow(window.name,img)

        for color in ColorList:
            #img = frame.copy()
            lower = np.array(color.lower)
            upper = np.array(color.upper)
            color.mask = cv2.inRange(img,lower,upper)

            cv2.imshow(color.name,color.mask)

            # Mask = cv2.bitwise_and(frame,frame,mask=color.mask)
            # cv2.imshow(color.name,Mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('quitting')
            break










def toHSV(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    return imgHSV



if __name__=='__main__':
    startWebcam()
    
