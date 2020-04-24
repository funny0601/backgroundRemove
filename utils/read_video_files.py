import os

def read_video_files(path):
    file_list = os.listdir(path)
    file_list_mp4 = [file for file in file_list if file.endswith(".mp4")]
    print(file_list_mp4)
    return file_list_mp4