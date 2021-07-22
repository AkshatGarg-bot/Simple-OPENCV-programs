import cv2 as cv
img = cv.imread('photos/cat.jpg')
# cv.imshow('Screenshot',img)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Screenshot',gray)


#simple thresholding

threshold , thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('THRESHOLD',thresh)

#threshold inverse
threshold , thresh_inv = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('THRESHOLD_inverse',thresh_inv)

#adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,(11) , 1)
cv.imshow('adaptive',adaptive_thresh)

cv.waitKey(0)