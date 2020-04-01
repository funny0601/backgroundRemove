import cv2
import numpy as np

cap = cv2.VideoCapture('./resource/friend_video_Trim.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
background = cv2.imread('./resource/restaurant.jpg')
background = cv2.resize(background, dsize=(width, height))

out = cv2.VideoWriter('./resource/converted_video.mp4', 0x7634706d, fps, (width, height), isColor=True)

if (not cap.isOpened()):
    print('Error opening Video')

while True:
    retval, frame = cap.read()
    if not retval:
        break

    #frame = cv2.resize(frame, dsize=(360, 240))

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(frame_gray, 127, 255, 0)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    max_area = 0
    max_cnt = None

    mask = np.tile(np.uint8(0), (height, width, 3)) # black
    color = [255, 255, 255] # white

    for idx, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)

        if area >= max_area:
            max_area = area # 제일 영역이 넓은 윤곽선 찾기
            max_cnt = cnt

    cv2.fillPoly(mask, [max_cnt], color) # mask_inv 역할
    ret, mask_inv = cv2.threshold(mask,127, 255, cv2.THRESH_BINARY_INV )

    # 육안상 확인용
    # cv2.drawContours(frame, [max_cnt], -1, (0, 255, 0), 1)

    frame_only_face = cv2.bitwise_or(frame, mask)  # 흰 배경에 얼굴

    background_1 = cv2.bitwise_and(background, mask)
    background_2 = cv2.bitwise_and(mask_inv,frame_only_face)

    dst =cv2.add(background_1, background_2)

    out.write(dst)
    cv2.imshow("dst", dst)


    #cv2.imshow("background", background)
    #cv2.imshow("background_1", background_1)
    #cv2.imshow("background_2", background_2)
    #cv2.imshow('mask', mask)
    #cv2.imshow("mask_inv", mask_inv)
    #cv2.imshow('frame_only_face', frame_only_face)

    key = cv2.waitKey(25)
    if key==27:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()

