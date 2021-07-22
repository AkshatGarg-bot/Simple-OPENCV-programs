import cv2 as cv
import numpy as np
img = cv.imread('photos/Screenshot from 2021-04-29 14-44-45.png')
cv.imshow('Screenshot',img) 

#translation--> shifting the image in x and y pixels
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# +x -> rigth
# -x -> left
# +y ->down
# -y -> up

translated = translate(img,-100,-100)
# cv.imshow('translated',translated) 


#rotation

def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2 , height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)


rotated = rotate(img,-45)
#cv.imshow('rotate',rotated) 

#flipping 

flip = cv.flip(img,-1); #1-> flipping the image vertically , 0->flipping the image horizontally , -1-> flipping the image both horizontally and vertically
cv.imshow('flipped',flip) 

cv.waitKey(0)