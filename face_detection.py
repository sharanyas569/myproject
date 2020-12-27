import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
count=0
img = cv.imread('group2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    count=count+1
    cv.rectangle(img,(x,y),(x+w,y+h),(200,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
print('number of faces are',count)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
