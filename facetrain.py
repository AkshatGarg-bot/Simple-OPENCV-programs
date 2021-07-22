import os
import cv2 as cv
import numpy as np

dir = r'/home/akshat/projects/OpenCv/photos/train'
people = []
for i in os.listdir(dir):
    people.append(i)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features=[]
labels=[]
def create_train():
    for person in people:
        path = os.path.join(dir,person)
        label = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY) 
            face_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1 ,minNeighbors =4 )
            for x,y,w,h in face_rect:
                faces_roi = gray[y:y+h , x:x+w]
                features.append(faces_roi)
                labels.append(label)    

create_train()
print('phull training baji')
features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()
#train the recognizer on features and label list
face_recognizer.train(features,labels)

np.save('features.npy', features)
np.save('labels.npy', labels)

            