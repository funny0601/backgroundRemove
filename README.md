# 배경 제거 및 합성 

1. Clone or download -> Download ZIP

2. zip 파일 압축 해제 후 backgroundRemove 폴더 위치에서 cmd 창 실행

3. cmd 창에서 ```pip install -r requirements.txt``` 

4. inputVideo 폴더에 영상 모두 업로드 </br>
영상 파일명 예시: p3_u2_a2_1_k -> script db 안의 script_id 형식임)

5. 배경과 영상 합성</br>
cmd 창에서 영상 합성되는 과정까지 보고 싶으면 ```python separate.py --preview yes``` 실행</br>
영상 합성되는 preview 창은 보고 싶지 않으면 ```python separate.py --preview no ``` 실행</br>

<em>(preview 창으로 영상 제대로 되는지 체크만 몇 개 해보고, 전체 다 합성할 때는 preview 끄는 것 추천,
preview 창 뜰 때 esc누르면 영상 플레이된 곳까지만 배경 합성되고 다음 동영상으로 넘어가니까 주의!)</em>

6. outputVideo에 원본 동영상 이름 그대로 배경 합성된 채로 저장
