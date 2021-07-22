import cv2 as cv
img = cv.imread('photos/Screenshot from 2021-04-29 14-44-45.png')
cv.imshow('Screenshot',img) 

cv.waitKey(0)

# capture = cv.VideoCapture('videos/WhatsApp Video 2021-05-08 at 20.11.17.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video',frame)
#     if cv.waitKey(20) & 0xFF == ord('e') :
#         break 
# capture.release()
# cv.destroyAllWindows()