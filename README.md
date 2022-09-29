# Server_management

- 여러개의 Server가 있다고 가정 했을 때 해당 Server들의 상태를 한번에 확인하고 관리할 수 있는 Web Service이다. 

필요한 패키지
npm
mysql
pm2 
express

### server
sudo apt-get install npm
npm install pm2 -g
npm install mysql -S
npm install 
apt-get install mysql-server

Sudo apt-get install python3-pip
Pip install flask
Pip install shedule
Pip install pymysql
Pip install pycryptodomex
Sudo apt-get powertop

### client
apt-get install powertop 


## 실행 방법 및 종료 방법

1. Server Computer
```shell
cd Python_data

# 백그라운드 실행
nohup python3 -u serverCom.py &
# [1] 21836 => 해당 Process ID를 출력하여 준다.

# 로그 기록 보기
tail -f nohup.out

# pid 로 백그라운드 실행 멈추기
sudo kill -9 21836
```

2. Client Computer 
```shell
# 백그라운드 실행
nohup python3 -u clientCom.py &
```


## 1. Server
1) Web Service
- Web Service는 기본적으로 NodeJS 프레임워크를 통해 생성했다.

Main
-----
<image src="https://user-images.githubusercontent.com/111109411/193001568-3662069f-1dca-42a6-8eaa-29cca8506223.png"  width="600" height="400"/>

* Main화면에서는 기본적으로 각각의 Server의 Data를 Block형식으로 나타내주고 현재 CPU사용량을 Circle Progress bar를 통해 나타냈다.
해당 Server의 Block을 클릭 할 경우 각각의 Server의 History를 확인 할 수 있고 Menu에 있는 Add Server를 통해 새로운 Server를 추가할 수 있다.

<image src="https://user-images.githubusercontent.com/111109411/193002554-534c3ae2-8967-4b9b-90c9-0a7931c98183.png"  width="600" height="400"/>
- 생성이 완료된 Server는 위와 같이 생성이 되고 아직 Client Program이 한번도 Data를 보낸적이 없다면 Empty를 나타내게 된다.
만약 Server가 Data를 보낸 History가 존재하지만 상태가 Off되어 있을 경우에는 아래와 같이 빨간 배경에 OFF를 나타낸다.

<image src="https://user-images.githubusercontent.com/111109411/193002851-e846483c-5826-4f63-af70-6fc8cf2102f1.png"  width="600" height="400"/>


<image src="https://user-images.githubusercontent.com/111109411/193003444-04dc01ea-4917-4b7c-800a-d234267f111f.png"  width="600" height="400"/>
- Main 화면 하단에는 각각의 Server의 가장 최신 정보들을 확인 할 수 있고 어떤 Server가 존재하는지 List 형식으로 확인이 가능하다.
그리고 필요가 없어진 Server의 경우에는 Delete 버튼을 통해 DB에 저장된 Key 값을 삭제 할 수 있다.




Add Server
----------
<image src="https://user-images.githubusercontent.com/111109411/193002161-813cf3b9-23e7-4b12-973f-6c28611bc2c6.png"  width="600" height="400"/>

- 각각의 Server는 특정 Key value를 부여받게 되며 해당 Key value를 통해서 Client program이 Server Program에게 Data를 보내게 된다.
Key value는 Random하게 생성이되고 모두 고유한 값을 가지게 된다.
- Server의 이름은 자유롭게 지정이 가능하다.


History
-------
- History Page는 총 3가지로 나눠진다.

1) CPU Usage
- CPU 사용량을 최근 30개 Data들을 출력해준다. 출력해주는 Data는 Chart형태로 출력이 되고 마우스를 가져다 대거나 화면을 터치하면 자세한 정보(시간, %)를 확인 할 수 있다. 
<image src="https://user-images.githubusercontent.com/111109411/193003917-6dc646c5-c5cc-44db-a645-b916bc9a5fc4.png"  width="600" height="400"/>



2) Power Usage
- Power의 경우 단위는 W단위로 Data가 저장이되고 해당 Data의 최근 30개를 출력해준다. 출력되는 형식은 CPU와 동일하게 Chart형태로 출력이 된다.
<image src="https://user-images.githubusercontent.com/111109411/193004809-1b12f4cf-4c3a-4d89-81ba-1f534e35e642.png"  width="600" height="400"/>


3) History List
- History는 Table 형식으로 출력이되며 현재 Server로 들어온 Client의 Data들을 모두 출력해준다.
<image src="https://user-images.githubusercontent.com/111109411/193004887-5849da30-d8a9-41b7-8a85-434105ac1430.png"  width="600" height="400"/>



2) Python script





## 2. Client
1) Python script





