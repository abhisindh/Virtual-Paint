import cv2
import weakref
import numpy as np


def empty(a):
    return a

def addMask(img,color):
    lower = np.array(color.lower)
    print(lower)
    upper = np.array(color.upper)
    mask = cv2.inRange(img,lower,upper)
    return mask






class Window:
    instances = []
    def __init__(self,name='Webcam',manipulate = empty):
        self.__class__.instances.append(weakref.proxy(self))
        self.name = name
        self.manipulate = manipulate

class ColorMask:
    instances = []
    def __init__(self,name='Mask', lower =[0,0,0], upper = [100,100,100] , manipulate = addMask):
        self.__class__.instances.append(weakref.proxy(self))
        self.name = name
        self.lower = lower
        self.upper = upper
        self.manipulate = manipulate
    

class TrackBar:
    instances = []
    def __init__(self,name='Value',var='var',initial=0,max=100):
        self.__class__.instances.append(weakref.proxy(self))
        self.name = name
        self.var = var
        self.initial = initial
        self.max = max












if __name__ == '__main':


    window1 = Window()
    window1.name = 'Webcam'

    window2 = Window()
    window2.name = 'HSV'

    window3 = Window()
    window3.name = 'something3'

    window4 = Window()
    window4.name = 'something4'
    list_ = [window1,window2,window3,window4]

    print([x.name for x in list_])
#     # orange = Color([1,1,],[2,2,2])
#     # print(orange.lower)

    # name='Webcam',frameWidth = 640,frameHeight = 480,brightness = 130,manipulate=empty