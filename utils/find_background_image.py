def find_background_image(path):
    # 동영상 제목 예시: p3_u2_a2_1_k
    file_name = path[:-4]

    # 파트 번호 추출
    part = file_name[1:2]
    # 유닛 번호 추출
    unit = file_name[4:5]

    background_image_path = './resource/backgroundImage/Part' + part + "/Unit" + unit + "/A.png"
    print(background_image_path)
    return background_image_path
