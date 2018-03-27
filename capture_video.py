import numpy as np
import cv2
from xlwt import Workbook

#load model face detect của opencv
#face_cascade = cv2.CascadeClassifier('/home/bkic611/Downloads/bkic611/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('/home/bkic611/Downloads/bkic611/lib/python3.6/site-packages/cv2/data/haarcascade_eye.xml')

# Load model Haar-cascade Detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#load video
cap = cv2.VideoCapture('./bkopenday.avi')

# Create a file excel to save the index of frame have face.
detected = Workbook()
detected_s1 = detected.add_sheet("Sheet1")
detected_s1.write(0,0,'frames')

index = 0

while True:

    ret, img = cap.read()
    if ret == True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Call detect function
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # If detect have face, then save images into raw_img and the frame index into excel file
        if(len(faces) > 0):
            frame_indx = cap.get(1) # Get frame index
            detected_s1.write(index + 1, 0, frame_indx)
            index = index + 1
            name = '/home/bkic611/Dropbox/Computer_vision_bkic/face_detect/rawimg/' + 'ch4_fr%d' % frame_indx + '.png'
            cv2.imwrite(name, img)
    else:
        break

cap.release()

detected.save("face_detected.xls")
