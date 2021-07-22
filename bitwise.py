import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype = 'uint8')
rectangle = cv.rectangle(blank.copy(),(30,30) , (370,370) , 255 , -1)
circle = cv.circle(blank.copy(),(200,200) ,200 , 255 , -1)
cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

#bitwise and--> intersection
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('and',bitwise_and)

#bitwise or-->union

bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('or',bitwise_or)

#bitwisexor-->non intersecting region

bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('xor',bitwise_xor)

#bitwise not

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('not',bitwise_not)

cv.waitKey(0)