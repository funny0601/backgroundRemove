from utils.arguments import *
from utils.attachingBackground import *
from utils.find_background_image import *
from utils.read_video_files import *

import cv2
from tqdm import tqdm

preview = get_arguments()  # default = yes
print(preview)
# inputVideo, outputVideo path
origin_path = './resource/inputVideo/'
result_path = './resource/outputVideo/'

# inputVideo list 모두 저장
video_list = read_video_files(origin_path)

for video in tqdm(video_list):

    cap = cv2.VideoCapture(origin_path + video)

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    background = cv2.imread(find_background_image(video))  # 파트, 유닛 번호에 맞는 배경
    background = cv2.resize(background, dsize=(width, height))

    out = cv2.VideoWriter(result_path + video, 0x7634706d, fps, (width, height), isColor=True)

    if (not cap.isOpened()):
        print('Error opening Video')

    if preview == 'yes':
        cap = attachingBackground_withPreview(cap, background, out, width, height)
    elif preview == 'no':
        cap = attachingBackground_withoutPreview(cap, background, out, width, height)

    if cap.isOpened():
        cap.release()
    cv2.destroyAllWindows()

