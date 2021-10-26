# MAC/DLC
* [MAC](https://github.com/2017100898/TIL/blob/main/Network/mac_layer.md)
* [DLC](https://github.com/2017100898/TIL/blob/main/Network/dlc_layer.md)

## Ethernet
* Physical Layer를 만들기 위해서는 전선이나 광섬유 등의 소자도 필요하고, Connector를 어떻게 꼽느냐에 대한 것도 정해야 한다. 그리고 이런 것들을 모두 표준화 해야 한다.
* 인터넷 서비스, 유무선 공유기 연결할 때 가장 많이 쓰는 기술이 바로 **이더넷**이다.
* 이더넷은 처음에는 Local area network(LAN)을 위해 만들어졌다. 현재는 MAN, WAN에서도 이더넷이 일반적으로 사용된다.
* 이더넷은 싸고 고속에서도 무리없이 동작하는 것이 장점이다.
* 이더넷은 끊임없이 확장이 된다. 자동차, 로봇, 공장,.. 클라우드, 통신사 (KT, SKT)

### 이더넷의 특징
* [OSI 7 Layer](https://github.com/2017100898/TIL/blob/main/Network/OSI_7_Layer.md)에서 1,2계층을 지원한다.
* 1. Frame 만드는 작업
* 2.  Header 부분에 Source, destination address 들어감
* 3. Frame 체크하는 시퀀스 들어감
* 4. 손실이 되거나 없어졌을 때 매우 미약하지만 재전송이 있음
* 막강한 에러 검출, 흐름제어 기능은 없음.
* data 최소 46byte, 최대 1500byte 까지 실어나를 수 있음 

![다운로드 (2)](https://user-images.githubusercontent.com/64299475/135893805-7422f335-f35e-420f-a5dc-58f09a03d703.png)

### Topologies
* 이더넷은 처음에는 Bus Topology 구조였다. 저렴하다는 것이 장점이지만 줄이 끊기면 모든 통신이 끊기는 단점이 있다. 저가로 근거리의 컴퓨터를 연결하기에는 좋은 기술이다.
* **현재는 Star Topology** 를 사용하며 이는 속도가 굉장히 빠르지만 허브 고장나면 통신 두절되는 단점이 있다.

### Bridging
* Contention Based (다수의 사용자들이 하나의 채널을 두고 서로 경쟁하며 나눠쓰는 방식) 매커니즘은 우연히 충돌이 없으면 성공하는 구조이기 때문에 문제가 많다. 
* **Bridging 기법을 활용하여 이 문제를 완화할 수 있다.**
	* Bridge는 왼쪽과 오른쪽으로 네트워크를 2개로 나누는 역할을 한다. 하지만 둘을 연결하는 다리 역할을 한다. **충돌에 참여하는 노드 갯수 줄이기 위함.**

### Power over Ethernet
* 이더넷은 원래 통신 목적으로 나왔지만, 소규모의 전원을 공급할 수 있는 기술이 있으므로 통신+전기 동시 공급 가능하다. (로봇, 카메라, 센서에서 사용)

### GPS & IEEE 1588
* 정확도 높게 시간을 맞추는 것은 굉장히 어려운 기술이다. 우리는 GPS 신호를 이더넷을 통해서 빠르게 전달하여 멀리 떨어져있는 장치가 시간을 맞출 수 있게 한다.

## WiFi
* Physical Layer, Mac Layer 있음.
* **에러 검출 및 복구는 없고** 위에 LLC (Logical link control, 논리링크제어) 올라감.
* 따라서 무선랜이 사용하는 경우에는 안전성이 보장이 안 된다.
* LAN 무선으로 지원하는 기술이다.

### Topologies
![R800x0](https://user-images.githubusercontent.com/64299475/135896855-d7cf0d98-f139-4fe0-8cb6-ee995ee8f1e1.png)
* **Ad hoc network** : 유무선 공유기가 없어도, 근거리의 컴퓨터들끼리 통신 가능한 형태.
* Access point : 결국 Ad hoc에 있는 장치 모아서 트래픽을 인터넷에 보내고 받을 수 있는 장치를 Access point라 한다. (유무선 공유기)
* **Infrastructure network** : Access point를 통해 다른 노드들의 무선랜 신호를 받아 인터넷(Infrastructure)으로 보내고, 인터넷의 신호를 다시 와이파이로 보내주는 형태.

### Layers
![2-Figure2-1](https://user-images.githubusercontent.com/64299475/135898567-e607b2e6-3027-4b3a-974b-73a83c343bb9.png)

* **PCF** : 유선에서 온 것들은 너무 늦지 않게 무선으로 준다. 노트북 중에 한 대라도 PCF 소프트웨어 돌아간다면 공유기와 같은 역할 한다. (Contention-free service,  완전히 없는 건 아님, IEEE802.11에서 지원)
* **DCF** : 어떤 대장도 존재하지 않고 각자가 동일하게 작동한다.(Contention service)

> contention-free : 중앙제어기가 각 Station 에게 전송 기회를 주기 때문에 각 Station이 채널 접근에 대한 경쟁 없다.   
> contention based : 여러 Station 들이 하나의 채널을 두고 서로 경쟁하며 나누어쓰는 방식


### AP Repetition
1. AP가 일단 B (무선 정보 및 이름) 전송
2. Polled station에 Poll message 보냄. - 보낼 거 있는지?
3. Polled station 이 통신하고 있는 동안 다른 기기들은 못 들어오도록 (NAV) 막음.

## Bluetooth
* WiFi와 같은 주파수 대역을 사용한다. 다 같이 쓰는 것은 아님.
* 서로 간섭이 일어나기 쉬움.
* 0과 1이 끊임없이 흘러가는 형식 : 유선 줄 ⇒ 무선 줄로 바꾸는 데에 크게 기여.
* 처음에는 키보드나 마우스 연결하기 위해 만들어짐.

### Layer Stack
![3-s2 0-B9781928994428500124-f09-07-9781928994428](https://user-images.githubusercontent.com/64299475/135900924-c2cef194-1343-4542-8170-3521bb3f6251.jpg)

* Baseband : Physical Layer의 상단
* OSI 7계층 구조 따르지 않는다. (필수 아님)
* WAP-UDP/TCP-IP-PPP : 이렇게 스택 쌓으면 블루투스 위에서 IP 통신 가능, 인터넷 서비스 올리는 것도 충분히 가능.
* 다양한 application 올라갈 수 있다.

## Bluetooth Low Energy (BLE)
* 블루투스 디바이스가 컴퓨터 디바이스에 맞게 개량되는데, BLE는 에너지를 적게 씀으로써 궁극적으로는 굉장히 오래 간다.

### Bluetooth vs BLE
* 음성지원에서 가장 차이가 남.
	* Bluetooth : YES, BLE : NO
	* **BLE는 간헐적으로 발생하는 트래픽 보내기 위함. 복잡한 기능 제거. 연결 설정 작업 굉장히 빠름.**
* BLE는 도어락, 가정장치, 센서 등을 타겟으로 만들어진 장치.

### BLE Layer Stack
![stack-link-layer](https://user-images.githubusercontent.com/64299475/135902934-222b2db9-4416-4cd4-9555-400b4e5992ea.png)

* Bluetooth SIG: 1,7 계층, Application 까지 모두 표준화 됨. (Samsung-LG 호환O)
* BLE: 1, 2계층

### BLE Network
* Node들이 Bluetooth 기술로 연결 되고 한 장치가 어떠한 장치로도 데이터 보낼 수 있음. -  Pairing, Broadcasting, Mesh Network

### BLE Applications
* 음성인 경우에는 Bluetooth 쓰임.
* 전구 안에서도 BLE 들어감.
* 자동차 안에 유용하게 쓸 수 있는 것들 (스마트키, Tyre pressure monitor sensor,…)
* Health-care 분야 (체중계, 혈당체크,…)

### BLE SW Stack
<img width="486" alt="스크린샷" src="https://user-images.githubusercontent.com/64299475/136254062-7aa92ae6-65a2-423d-b3fe-8facc63713e5.png">

* Third-party device : Sensor (받아들임) / actuator (반응 - 불켜기)
* Mesh node : Sensor, actuator로부터 정보 받거나 주는 것
* Mesh gateway : 필요 시 인터넷 연결

### BLE Mesh Application
* 원하는 지점에 배터리로 동작하고 BLE로 연결 된 전구를 놓고, 사람 또는 자동차의 움직임을 탐지하면 불을 켜고 시간차에 따라 인근 전구에게 불을 켜라고 명령할 수 있다. 사람이 탐지될 때만 불을 켤 수 있으므로 전력 사용을 줄일 수 있다.

## LoRa
* Wide Area Network for IoT
* 저전력, 속도 낮음 - 사람을 위한 것이 아닌 센서/기계를 위한 것.
* 산업용 용도 많음 (long range 간헐적으로 모니터링)

### LoRa Protocol Layer
 <img width="425" alt="스크린샷 2021-10-07 오전 2 42 30" src="https://user-images.githubusercontent.com/64299475/136255736-6c80ad0c-4d68-4d06-8056-00cebe805b77.png">

* Class A : 필요할 때 필요한 것만 - 가장 LoRa 목적에 맞음
* Class B : 주기적으로
* Class C : 연속

## LoRaWAN
* 타겟팅 : 이동통신
* 장거리 무선 센싱 가능
* LoRa 기술을 확장한 것
* gateway, server 등 network SW 넣음 - OSI 7Layer 굳이 지키지 않음.

### Network Architecture
<img width="425" alt="스크린샷 2021-10-07 오전 2 53 02" src="https://user-images.githubusercontent.com/64299475/136257176-d531b565-087a-408b-94af-fe8d896bc355.png">

* 모니터링 - Gateway - Network Server (어딘가로 보낸다) - Application server
* End device와 Server, gateway를 묶음으로 만듦.

### Protocol Stack
<img width="434" alt="스크린샷 2021-10-07 오전 2 55 54" src="https://user-images.githubusercontent.com/64299475/136257645-dee32236-eebe-4f41-a500-3d804a73cc43.png">

* Application 끼리는 필요한 정보 주고 받고 무선의 해당하는 부분은 LoRaWAN을 따르며 OpenSource 등을 사용할 수 있다.

## LoRa/LoRaWAN Implementation
* Ethernet, Wifi, Bluetooth의 MAC은 바꿀 수 없음.
* **LoRa, LoRaWAN의 MAC은 바꿀 수 있음.**




