import numpy as np
import cv2
from xlwt import Workbook
#load model face detect của opencv
face_cascade = cv2.CascadeClassifier('/home/bkic611/Downloads/bkic611/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/bkic611/Downloads/bkic611/lib/python3.6/site-packages/cv2/data/haarcascade_eye.xml')

#load video
cap = cv2.VideoCapture('/home/bkic611/Desktop/test/bkopenday.avi')

#tao file excel de luu so thu tu cua cac frame co mat nguoi 
detected = Workbook()
detected_s1 = detected.add_sheet("Sheet1")
detected_s1.write(0,0,'frames')

index = 0

while True:

    ret, img = cap.read()
    if ret == True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #goi ham detect face
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        #neu detect duoc mat thi luu anh vao raw_img va luu chi so frame va file excel
        if(len(faces) > 0):
            frame_indx = cap.get(1)
            detected_s1.write(index + 1, 0, frame_indx)
            index = index + 1
            name = '/home/bkic611/Dropbox/Computer_vision_bkic/face_detect/rawimg/' + 'ch4_fr%d' % frame_indx + '.png'
            cv2.imwrite(name, img)
    else:
        break

cap.release()

detected.save("face_detected.xls")
