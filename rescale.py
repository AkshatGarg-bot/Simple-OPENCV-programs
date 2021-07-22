import cv2 as cv
img = cv.imread('photos/Screenshot from 2021-04-29 14-44-45.png')
cv.imshow('Screenshot',img) 


def rescaleFrame(frame,scale=0.75):
    #works with pre recorded videos and images
    width= (int)(frame.shape[1]*scale)
    height = (int)(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resize_img = rescaleFrame(img,scale = 0.2)
cv.imshow('Screenshot_new',resize_img)
cv.waitKey(0)

def changeRes(width,height):
    #used for live video
    capture.set(3,width)
    capture.set(4,height)

# capture = cv.VideoCapture('videos/WhatsApp Video 2021-05-08 at 20.11.17.mp4')
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame,scale = 0.5)
#     cv.imshow('video',frame)
#     cv.imshow('video_resized',frame_resized)
#     if cv.waitKey(20) & 0xFF == ord('e') :
#         break 
# capture.release()
# cv.destroyAllWindows()

