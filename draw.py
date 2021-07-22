import cv2 as cv
import numpy as np

blank = np.zeros((1000,1000,3),dtype = 'uint8') #creates a complete blank image
#cv.imshow('khali',blank)

# 1. painting the whole image with a certain color

# blank[:] = 0,255,0
# cv.imshow('1khali',blank)

# 2. creating a rectangle
# cv.rectangle(blank,(0,0), (250,250),(0,255,0),thickness=-1) #thickness is the thickness of boundary line of rectangle if we do thickness = -1 it will fill the whole rectangle with that color

# #blank[0:250 , 0:250] = 0,255,0
# cv.imshow('1khali',blank)

# 3. creating a circle
# cv.circle(blank , (500,500) , 500 , (0,0,255),thickness = 2)
# cv.imshow('1khali',blank)

# 4. draw a line
# cv.line(blank , (0,0) , (200,200) , (0,0,255) , thickness = 1)
# cv.imshow('1khali',blank)

#5 write text on an image
# cv.putText(blank , 'Hello' , (225,225) , cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0,255,0) , 2)
# cv.imshow('1khali',blank)
cv.waitKey(0)