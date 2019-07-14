import cv2
import numpy as np
import os

facePath = 'faces/'

faces = os.listdir(facePath)
# print(faces)
names = {}
for i in range(len(faces)):
    name = faces[i].split('.')[0]
    names[i] = name

# print(names)

faceData = []
for file in faces:
    face = np.load(facePath+'/'+file)
    face = face.reshape(face.shape[0],-1)
    faceData.append(face)

# print(faceData)
# faceData = np.asarray(faceData)
# print(faceData.shape)
faceData = np.vstack(faceData)
# print(faceData.shape)
labels = np.zeros((len(faceData),1))
length = len(faces)
total_faces = len(faceData)
n = total_faces // length
for i in range(length):
    labels[i*n : (i+1) * n, :] = float(i)

def distance(x1,x2):
    return np.sqrt(sum((x2 - x1) ** 2))

def knn(x,faces):
    n = faces.shape[0]
    d = []
    for i in range(n):
        d.append(distance(x,faces[i]))
    d = np.asarray(d)
    sortedIndex = np.argsort(d)
    lab = labels[sortedIndex][:5]
    count = np.unique(lab, return_counts=True)
    return count[0][np.argmax(count[1])]

dataset = cv2.CascadeClassifier('data.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX

# image = cv2.imread('gallery27.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# faces = dataset.detectMultiScale(gray, 1.3)
# for x,y,w,h in faces:
#     cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,255),4)
#     input_face = gray[y:y+h,x:x+w]
#     input_face = cv2.resize(input_face, (50,50))
#     lab = knn(input_face.flatten(), facesData)
#     name = names[int(lab)]
#     cv2.putText(image, name,(x,y),font,1,(0,255,255),2)
#
# cv2.imwrite('result.jpg',image)

while True:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray, 1.3)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255),4)
            input_face = gray[y:y+h,x:x+w]
            input_face = cv2.resize(input_face, (50,50))
            lab = knn(input_face.flatten(), faceData)
            name = names[int(lab)]
            cv2.putText(img, name,(x,y),font,1,(0,255,255),2)
        cv2.imshow('result',img)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Camera not working")

cap.release()
cv2.destroyAllWindows()
#
