import numpy as np
import cv2
from xlwt import Workbook
import xlrd

face_cascade = cv2.CascadeClassifier('/home/bkic611/Downloads/bkic611/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/bkic611/Downloads/bkic611/lib/python3.6/site-packages/cv2/data/haarcascade_eye.xml')

data = xlrd.open_workbook("video_list_ch3.xls")
list = data.sheet_by_index(0)

detected = Workbook()
detected_s1 = detected.add_sheet("Sheet1")
detected_s1.write(0,0,'video')
detected_s1.write(0,1,'frames')
index = 0

for video_indx in range (1,41):
    channel = list.cell(video_indx, 0).value
    date = list.cell(video_indx, 1).value
    time = list.cell(video_indx, 2).value
    path = '/home/bkic611/Desktop/camera_data/' + channel + '/' + date + '/' + time + '.mp4'
    cap = cv2.VideoCapture(path)

    gray_pre = np.zeros((1080,1920),dtype=np.uint8)
    pre_face = 0

    while True:

        ret, img = cap.read()

        if ret == True:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            dif = cv2.subtract(gray, gray_pre)
            th, dst = cv2.threshold(dif, 2, 1, cv2.THRESH_BINARY)
            dif_rate = np.sum(dst) / 2073600
            gray_pre = gray
            if((dif_rate < 0.04) & (pre_face == 0)):
                continue
            pre_face = 0
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            # print(cap.get(1),faces)

            if(len(faces) > 0):
                pre_face = 1
                frame_indx = cap.get(1)
                detected_s1.write(index + 1, 0, channel)
                detected_s1.write(index + 1, 1, time)
                detected_s1.write(index + 1, 2, frame_indx)
                index = index + 1
                name_raw = '/home/bkic611/face_detect/raw_img/'+ channel + '/'+ time + '_fr%d' % frame_indx + '.png'
                cv2.imwrite(name_raw, img)

                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    roi_color = img[y:y + h, x:x + w]

                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                name_detected = '/home/bkic611/face_detect/detected_img/' + channel + '/'+ time + '_fr%d' % frame_indx + '.png'
                cv2.imwrite(name_detected, img)
        else:
            break

    cap.release()

detected.save("face_detected_ch3_27_30.xls")
