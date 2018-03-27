
import numpy as np
import cv2
import xlrd
#file luu so thu tu cua cac frame co mat nguoi
data = xlrd.open_workbook("face_detected.xls")
list = data.sheet_by_index(0)

#load model detect face co san
face_cascade = cv2.CascadeClassifier('/home/bkic611/Downloads/bkic611/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/bkic611/Downloads/bkic611/lib/python3.6/site-packages/cv2/data/haarcascade_eye.xml')
#load video
cap = cv2.VideoCapture('/home/bkic611/Desktop/test/bkopenday.avi')

nums_img = list.nrows-1
frame_time_pre = 0
#load thu tu cac frame co face va doc cac frame do de detect mat
for index in range(nums_img):
	
    frame_indx = list.cell(index+1, 0).value

    cap.set(1,int(frame_indx)-1)
    #chi lay 1 frame trong 1s
	time = cap.get(0)
    frame_time = int((cap.get(0) + 1) / 1000)

    if (frame_time > frame_time_pre):
        frame_time_pre = frame_time
    else:
        continue

    ret, img = cap.read()
    name_s = '/home/bkic611/face_detect/raw_img/' + 'ch4_fr%d' % frame_indx + '.png'
    cv2.imwrite(name_s, img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect face
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #khoanh vung detect duoc
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    name = '/home/bkic611/face_detect/detected_img/' + 'ch4_fr%d'%frame_indx + '.png'
    cv2.imwrite(name,img)
