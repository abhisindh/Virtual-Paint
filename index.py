from functions import *

orange = ColorMask([5,107,0],[19,255,255])

normal = Window('Normal')
hsv = Window('HSV',toHSV)
mask = Window('Mask',addMask)

h_min=TrackBar('Hue Min',139,179)
h_max=TrackBar('Hue Max',179,179)
s_max=TrackBar('Sat Min',23,255)
s_min=TrackBar('Sat Max',255,255)
v_max=TrackBar('Val Min',73,255)
v_min=TrackBar('Val Max',255,255)








startWebcam()

