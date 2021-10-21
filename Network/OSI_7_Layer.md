# Computer Network(ing)
* 컴퓨터들이 연결된 것
* Computer Network 보다 Computer **Networking**이 더 중요하다.
* Network : 과거에는 정해진 일을 하는 기기들을 연결하여 정보를 보내주기만 하면 됐다.
* **Networking** : 최근에는 더이상 하드웨어가 중요하지 않으며, 필요한 기능을 그때그때 바꿀 수 있는 Flexible한 **소프트웨어**가 올려진 기기를 연결해야 한다. 그들을 연결하는 방법이 더욱 중요하다. (Flexible 한 동작 자체가 중요)

### Computer
* Desktop Computer
* Server Computer
* Tablet Computer
* Smart Phones
* Smart Watches 
* IoT & Sensor Devices 
* Vehicles, Robots, Drones ...

### 4차 산업혁명
* 로봇, 인터넷 연결 등 글로벌한 제조환경이 만들어졌다.
* 네트워킹으로 연결 되어있으며, 정해진 시간에 똑같은 일을 하는 것이 아닌 로봇들의 상황이 **동적**으로 바뀌었을 때 그걸 인지하고 다른 행동한다. 사람과 로봇이 협업을 하기도 한다.
* 집단적으로 데이터를 가공하여 거시적 관점에서 로봇 제어함으로써 인공지능, 데이터 사이언스 등 **뇌**에 해당하는 부분이 강화되었다.

# OSI 7 Layer 🚀✨🔥
* **네트워크를 여러 단계로 나눈 이유?**
	* 데이터의 흐름을 한 눈에 볼 수 있다.
	* 하나의 문제를 7 단계로 나눔으로써 문제 해결이 쉽다.
	* 표준화를 통해 다양한 네트워크 장비가 오류 없이 작동하도록 한다. 

![7layer](https://user-images.githubusercontent.com/64299475/132338070-ff17588c-340c-46dc-8dd0-2dbb173f5945.png)


1. **Physical Layer** : 기기가 접하는 부분, 두 장치를 유/무선으로 연결한 다음 0과 1의 조합을 주고 받게 한다. But 유/무선 모두 에러가 안 날 수가 없다. 가장 복잡한 계층.
2. **Data Link Layer** : 에러가 났을 때 에러를 검출하고 복구하는 역할을 한다. 속도 차이 등을 방지한다. 대부분 1, 2 계층은 합쳐져 있다. 흐름 제어 지원. (하지만 모든 장치 100% 지원하는 것은 아니다.)
3. **Network Layer** : Routing 이 가장 중요한 역할. 여러 길 중 방금 받은 메세지를 어떤 길로 보낼지 결정한다. 어떤 SW냐에 따라 Routing or Switching. (IP) 
4. **Transport Layer** : 서비스 입장에서의 에러 검출 및 복구. (TCP)
5. **Session Layer** : Authentication (유튜브 가격에 따른 다른 기능 제공 / 넷플릭스 요금제), Permission (로그인), Session (음성-데이터-영상 구분해서 보냄) 서비스 시작 지점, 서비스 제공 범위, 서비스 구성요소들간의 관계 결정
6. **Presentation Layer** : 코드 간 번역, 저장 규칙, 암호화 등 미디어를 컴퓨터에 어떻게 저장할 것인지 결정한다.
7.  **Application Layer** : 사람이 접하는 부분, UI, 사용자의 입출력

* **[ Upper Layer ]** Application / Presentation / Session
* **[ Lower Layer ]** Transport / Network / Data Link / Physical

## Peer-Communication

![peer](https://user-images.githubusercontent.com/64299475/132338100-1b9c0220-4ad7-46cc-a28f-db3d6e4675bb.png)


* Device A, B 사이에 수많은 장치들이 있다.
* **A의 application layer 가 B의 application layer 와 통신하는 것이 최종 목적이다.**

1. A가 메시지를 A의 Application으로 전달한다.
2. A의 Application은 Presentation으로 전달하고 미디어의 모양 갖춘다.
3. Session을 통해서 영상, 음성, 텍스트 트래픽을 Transport로 전달한다.
4. Transport 에서 Network layer로 에러 없이 전달한다.
5. Network layer는 인접한 장치로 메시지를 보내야 된다. Data link 와 Physical 을 통해 왼쪽 Intermediate node로 메시지 보낸다.
6. 왼쪽 Intermediate node 메시지는 Data link와 Network을 타고 위로 올라갔다가 방향을 결정하고 내려온다.
7. Physical을 통해 오른쪽 Intermediate node에 메시지를 보낸다. 오른쪽 Intermediate node는 올라가서 방향을 결정하고 내려온다.
8.  Device B의 Physical로 메시지를 보내고, B의 Application 까지 올라간다.

* 기능 : 왼쪽과 오른쪽의 Peer communication 
* 전달 : 위에서 아래로, 아래에서 위로

<img width="372" alt="스크린샷 2021-09-07 오후 7 28 22" src="https://user-images.githubusercontent.com/64299475/132338113-2a880ca8-6299-4e46-8876-b70449f473b7.png">

* Router : Physical, Data Link, Network (OSI 1,2,3) 지원

<img width="368" alt="스크린샷 2021-09-07 오후 7 32 35" src="https://user-images.githubusercontent.com/64299475/132338129-3012a1d5-bc3f-400a-8b08-27571bd45467.png">


* 요즘에는 Application+Presentation+Session 을 합쳐서 Application 하나로 정의할 수도 있다. 

### Layering Example

<img src="https://user-images.githubusercontent.com/64299475/132338149-f811d345-d7ce-4f90-ab14-0fb40d927bfc.png">


## Open Source Hardwares
* 아두이노 : 회로도 공개 및 오픈소스라는 개념을 하드웨어에 적용. 디지털과 아날로그 정보를 받아 결국 다시 디지털과 아날로그로 출력하는 장치. 하고 싶은 것을 굉장히 쉽게 할 수 있도록 해주고, 다양한 기능과 형태, 성능의 제품이 있다. 
* 아두이노 Shields (써드파티) : 아두이노는 범용성을 띠어야 했기에 써드파티인 Shields 업체들이 아두이노가 하지 못 한 기능을 추가할 수 있게 되었다. 아두이노의 기능을 강화하고 각 분야에 특화된  보드들을 만들기 시작했으며 아두이노의 쓰임새가 확산되었다고 볼 수 있다.
* Open Source 정신이 확산되기 시작했다. (집단지성의 작용)
* Facebook’s Open Source Datacenter - 모든 건물 설계도, 서버, 네트워크, 회로도 공개 (OCP)

## Single Board Computer (SBC)
* Raspberry Pi : 저전력의 작은 컴퓨터 필요할 때 더할 나위 없이 사용하기 좋은 하드웨어. Linux 운영체제 사용. 라즈베리 파이 덕분에 지금껏 없었던 분야의 프로그래밍이 가능해졌다.
* ODROID, BeagleBone, INTEL NUC, Google Coral, NVIDIA Jetson… 의 등장
* 우리는 컴퓨터를 직접 만들 수 있고, 매우 작고 파워풀해졌다! 앞으로는 이러한 컴퓨터를 어떻게 사용하는가? 가 매우 중요하다.
* 컴퓨터 네트워크는 이러한 **컴퓨터**를 연결하는 것. 사람이 주로 end user가 아니다.

## Linux
* 일반적인 데스크탑 뿐만 아니라 수 많은 전자기기에 Linux가 들어있다. 
* Open source hardware: 거의 대부분 Linux 고려, Linux 기반 네트워킹이 가장 중요한 화두가 되었다. 거의 모든 것의 기반이자 표준이라고 표현할 수 있다. 
* Ubuntu, debian, CentOS, fedora, mint, elementary…
* Ubuntu : 일반 데스크탑, 대형 Server, Cloud computing, 작은 IoT 등 다양한 컴퓨터 위에서 돌아갈 수 있다.
* 경량의 Ubuntu도 굉장히 많다. (Ubuntu MATE…) 
