from classes import *




def empty(a):
    pass


def startWebcam(ColorList=[],frameWidth = 640,frameHeight = 480,brightness = 130):
    
    point_list = []

    global imgResult
    cap = cv2.VideoCapture(0)
    cap.set(3,frameWidth)
    cap.set(4,frameHeight)
    cap.set(10,brightness)

            
    while True:
        #print(point_list)
        success, img = cap.read()
        imgResult = img.copy()
        for window in Window.instances:
            img = window.manipulate(img)
            
            #cv2.imshow(window.name,img)
            #cv2.imshow('Result',imgResult)

        for color in ColorList:
            #img = frame.copy()
            lower = np.array(color.lower)
            upper = np.array(color.upper)
            color.mask = cv2.inRange(img,lower,upper)
            imgContour = color.mask
            x,y = getContours(imgContour)
            if x:
                point_list.append([x,y,color.bgrValue])
            for point in point_list:
                cv2.circle(imgResult,(point[0],point[1]),10,point[2],-1)

            #cv2.imshow(color.name,imgContour)

        cv2.imshow('result',imgResult)

            # Mask = cv2.bitwise_and(frame,frame,mask=color.mask)
            # cv2.imshow(color.name,Mask)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('quitting')
            break

def getContours(img):
    x,y,w,h = 0,0,0,0
    contours, heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        
        if area>500:
            #img = cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,peri*0.02,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y











def toHSV(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    return imgHSV



if __name__=='__main__':
    startWebcam()
    
