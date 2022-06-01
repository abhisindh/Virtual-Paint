import cv2
import weakref
import numpy as np


def empty(a):
    return a






class Window:
    instances = []
    def __init__(self,name='Webcam',manipulate=empty):
        self.__class__.instances.append(weakref.proxy(self))
        self.name = name
        self.manipulate = manipulate

class ColorMask(Window):
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
    

class TrackBar:
    instances = []
    def __init__(self,name='Value',initial=0,max=100):
        self.__class__.instances.append(weakref.proxy(self))
        self.name = name
        self.initial = initial
        self.max =max











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