import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture('./resource/friend_video_Trim.mp4') # 비디오 객체 cap 생성

if (not cap.isOpened()):
    print('Error opening Video')

while True:
    retval, frame = cap.read()
    if not retval:
        break
    frame = imutils.resize(frame, width=320, height=240)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(25)
    if key==27:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()

