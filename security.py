import cv2
from datetime import datetime
import os

cap = cv2.VideoCapture(0) 

face_part = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_part = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
eye_part = cv2.CascadeClassifier('haarcascade_eye.xml')

if not os.path.exists('file'):
    os.mkdir('file')

while True:    
    _, frame = cap.read()    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    
    faces = face_part.detectMultiScale(gray, 1.3, 5)    
    bodies = body_part.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:    
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        face_snap = frame[y:y+h, x:x+w]        
        if not os.path.exists('file/' + datetime.now().strftime('%Y-%m-%d')):
            os.mkdir('file/' + datetime.now().strftime("%Y-%m-%d"))

        cv2.imwrite('file/' + datetime.now().strftime("%Y-%m-%d") + '/' + datetime.now().strftime("%H-%M") + '.jpg', face_snap)
        cv2.imshow('frame', frame)

    for (x, y, w, h) in bodies:    
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        body_snap = frame[y:y+h, x:x+w]
        if not os.path.exists('file/' + datetime.now().strftime('%Y-%m-%d')):
            os.mkdir('file/' + datetime.now().strftime("%Y-%m-%d"))

        cv2.imwrite('file/' + datetime.now().strftime("%Y-%m-%d") + '/' + datetime.now().strftime("%H-%M") + '.jpg', body_snap)
       
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    