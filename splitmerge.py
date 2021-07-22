import cv2 as cv
img = cv.imread('photos/Screenshot from 2021-04-29 14-44-45.png')
# cv.imshow('Screenshot',img) 


b,g,r = cv.split(img)
# cv.imshow('blue',b) 
# cv.imshow('green',g) 
# cv.imshow('red',r) 

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('red',merged) 

cv.waitKey(0)