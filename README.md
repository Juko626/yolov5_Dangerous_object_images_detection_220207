# 휴먼에러 감소를 위한 사물 엑스레이 자동 인식 프로젝트 
![Generic badge](https://img.shields.io/badge/Yolo-v5-blue.svg)
![Generic badge](https://img.shields.io/badge/FastAPI-0.7.0-red.svg)
![Generic badge](https://img.shields.io/badge/Python-3.7.12-green.svg)

## 프로젝트 설명

휴대 수화물 검색 분야의 휴먼 에러를 줄이기 위해 엑스레이 위해물품 데이터를 이용하여 이 물품이 위해물품인지 아닌지를 판별한 후 이미지를 출력 후 Clova Voice를 이용하여 음성 출력을 하는 프로젝트를 진행.

<br>

![image](https://user-images.githubusercontent.com/98979901/156497098-3165d082-6255-4a20-9d0d-6b2070144590.png)
![image](https://user-images.githubusercontent.com/98979901/156497414-5ff5bc9b-7c00-440c-9745-9c4c8e9a7af5.png)
<br>
<br>

## 프로젝트 진행 과정
  1. AI hub의 위해물품 엑스레이 데이터 7000장을 라벨링(Roboflow 이용)
  2. 라벨링된 위해물품을 YOLOv5 모델을 이용하여 객체를 인식하고 이미지를 출력함.(150 epochs)
  3. 결과 값을 MP3 파일로 저장해주는 '사물 엑스레이 자동인식 시스템' 제공
![](../header.png)

<br>
<br>



## 설치 방법

YOLOv5:
- YOLOv5 설치
```sh
!git clone https://github.com/ultralytics/yolov5.git
```
<br>

YOLOv5의 requirements.txt:
- python 프로젝트의 의존성 정보가 담긴 문서이다. 의존성 정보를 requirements.txt에 작성하는 이유는 협업이나 오픈 소스 등 다른 사람이(혹은 자신이 다른 환경에서) 해당 프로젝트를 실행할 일이 있을 때 편의를 위해
```sh
!pip install -r requirements.txt
```



<br>



ngrok:
- ngrok 은 NAT와 방화벽 뒤에 있는 로컬 서버 를 안전한 터널을 통해 공개 인터넷에 노출시켜 주는 도구라고 설명


<br>

## 분류 데이터
```python
'Axe'
'Chisel'
'Gun'
'HDD'
'HandCuffs'
'Knife'
'Lighter'
'Plier'
'Saw'
'Scissors'
'Screwdriver'
'SmartPhone'
'Spanner'
'SupplymentaryBattery'
'USB'
```
<br>




## 노션을 이용하여 일정관리 및 역할 배분
![image](https://user-images.githubusercontent.com/98979901/156496909-0e5105f6-df6b-4976-b8fc-dd10a3b24a23.png)

<br>
<br>




