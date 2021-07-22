import os
import cv2 as cv
img = cv.imread('photos/group.jpg')
# cv.imshow('person',img) 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('person',gray) 
haar_cascade = cv.CascadeClassifier('haar_face.xml')
face_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1 ,minNeighbors =6 )
print(len(face_rect))
for x,y,w,h in face_rect:
    cv.rectangle(img,(x,y),(w+x,h+y),(0,255,0),thickness = 1)

    cv.imshow('detected',img)

cv.waitKey(0)