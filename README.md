# project_laundry
졸업작품 프로젝트 : 스마트 빨래 분류기

## rasp
라즈베리

### camera_detect
메인 함수 run()
이미지(numpy array)를 iteration 으로 반환

### client_socket
메인 함수 run(ip, port, img)
이미지를 서버로 전송

## server

### server_socket
메인 함수 run(port)
클라이언트로부터 이미지를 전송받아
내부에서 model에 이미지를 인자로 넘겨주며 call
model로 부터 받은 반환값을 클라이언트로 전송

### model
이미지를 받아서 예측모델로 넘겨 label을 받아온다

## datasets
수집 데이터와 데이터를 tfrecord로 변환

### convert_datas.py
convert to tfrecord

## venv
파이선 가상환경 설정들

## slim
tf slim 라이브러리중 필요한것만 남기고
프로젝트에 맞게 수정
