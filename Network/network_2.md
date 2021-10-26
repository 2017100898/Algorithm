# Network - 2
## Softwarization ⚙️
* 이제는 네트워크 장치와 통신 장치들도 하드웨어 위에서 **소프트웨어를 어떻게 짜느냐가 중요**해졌다.

### Linux Eating the Networking Industry
<img width="597" alt="스크린샷 2021-10-19 오전 1 46 49" src="https://user-images.githubusercontent.com/64299475/137774026-a2240835-3e57-424f-bab7-e087a60a388a.png">

* **새로운 네트워크 구조 탄생** (2010~)
* 기존의 OS 7 Layer -> I/O Abstraction & DataPath에 포함함
* 그 위에 OS로 덮고 Controlability 확보 -> 클라우드 (가상화 기술)  -> Orchestration -> Analytics -> Application (서비스)
* **내가 Network 원하는대로 컨트롤 가능**
* OSI 7 Layer와 표준의 힘이 약화 되었고, Linux 산하에서 OpenSource sw로 새롭게 만들어진 네트워킹 기술들이 대거로 퍼지기 시작했으며, Linux가 network industry까지 점령했다.
* Ericsson : "Hardware" to "Software and Service" within a decade
* Intel ⇒ Linux에 투자 ⇒ Intel & Linux 위에서 enduser application 어떻게 하면 효율적으로 돌아가게 설계할지 생각하는 단계가 됨.

#### Purpose-Built for Performance
<img width="549" alt="스크린샷 2021-10-19 오전 2 10 01" src="https://user-images.githubusercontent.com/64299475/137777110-6d9dfe2d-a7c0-49f4-a7b4-6bb92897327c.png">

1. Ericsson RBS 6000 : 이동 통신에서 사용자 입장에서 첫번째로 만나는 장치 (안테나)
	* 하드웨어 하나, 소프트웨어를 돌려서 기지국을 바꿈.
3. Ericsson Blade Server :  노트북 같은 intel CPU server (Control)
4. SSR 8000 Family : 라우터, 스위치 받아서 어디론가 전달하는 장치 (data and networking, 메모리 고성능)
	* 하드웨어 하나, 필요한 기능 소프트웨어로 설치하면 됨. 

#### Purpose-oriented Common Platform
* 용량 커지거나, 물리적인 공간 주어지면 어떻게 하느냐?
	* 책꽂이 식으로 필요한 모듈 필요할 때 꽂으면 됨. (=common platform)
* **Network 장치의 가상화**
	* 장치 설치 후 내가 필요한만큼, 필요한 기능으로 돌린다.

#### Big Change in Current Network
* 과거 : 할 일이 정해진 장치 (장치 중심) / 표준이 중요함 / 길을 정하는 것은 라우터의 판단
* 현재 : 장치보다 장치 내의 소프트웨어 중심 (함수 중심) / 소프트웨어 연동만 되면 OK (표준 약화) / 네트워크 컨트롤 가능

## Software Defined Network(ing)
* 통신사가 인공지능을 해야하는 이유

### Internet
<img width="501" alt="스크린샷 2021-10-19 오전 2 28 40" src="https://user-images.githubusercontent.com/64299475/137779147-3f1accb2-7034-4766-b94d-08a80ea4c4e8.png">

### Router
<img width="501" alt="스크린샷 2021-10-19 오전 2 51 18" src="https://user-images.githubusercontent.com/64299475/137782007-733dd325-f2da-4056-a34a-06a8e1af8724.png">

* 패킷이 Port를 통해 들어오면 어디로 내보낼지 table을 보고 내보냄.
* controller : 이 SW가 돌아가는 CPU, controller가 주변의 라우터와 통신해서 forwarding table 만든다.
* 라우터끼리 정보 주고 받아서 독립적으로 시행 되는 것이 단점이다.

### Problems on Router
1. 패킷 길 **컨트롤** 원함
	* 새로운 통신 프로토콜
	* 사용자 전용 Customized 라우팅
	* 패킷 레벨 전송 경로 제어
2. 네트워크는 **서비스**를 위한 도구이길 바람
	* 서비스 인식 기반 전송 기술
	* 서비스 인식 기반 패킷 처리 기술
	* Cross Layer 서비스 지원
	* 멀티 벤더의 일관된 제어 / 관리

### Why SDN?
<img width="484" alt="스크린샷 2021-10-19 오전 3 23 26" src="https://user-images.githubusercontent.com/64299475/137786385-b78d0cbd-0816-4f9a-b57a-6d95a2680d1a.png">

* 기존 라우터의 역할이 아닌, 패킷 길을 컨트롤하고, 네트워크를 서비스를 위한 도구로 사용하기 위해 Control Plane을 바깥으로 빼냈다. 
* 원래는 주변 라우터들과 통신한 다음 본인 스스로 Table을 만들었지만, 지금은 외부 장치가 API를 통해 table주면, Forwarding table을 바깥 장치로부터 가져와서 본인의 table을 업데이트만 한다. 그리고 오로지 **받은 table에서 시킨대로만 행동한다.**

### OpenFlow based SDN Network
<img width="439" alt="스크린샷 2021-10-24 오전 2 35 35" src="https://user-images.githubusercontent.com/64299475/138566199-333ffe06-33e5-483f-9622-b68e3ef6e94b.png">

* 중앙 집중형 SDN 컨트롤러와 OpenFlow 프로토콜 
* *Secure Channel* : 외부와의 통신하는 채널 (보안) ⇒ Flow Table update
* 통신사업자의 라우터가 있는 자리에 OpenFlow Switch로 모두 바꾼다. table은 외부의 컨트롤러가 만들고 내려준다.

#### OpenFlow Protocol
* OpenFlow : 룰을 주고 그 룰에 맞으면 취할 액션을 정의해주는 것
* Rule : 2,3,4계층의 address 줌 (cross layer)
* Action : 관련 액션 
* Stats : Packet+byte counters
* controller : 중앙집중의 Center이며, Open flow 명령 내린다.
* OpenFlow Switch : controller에게서 명령을 받는다.
* Controller가 중앙집중으로 전체 네트워크 상황을 봐가면서 행동할 수 있으므로 네트워크가 할 수 있는 일이 굉장히 많아졌다.


## Network Function Virtualization (NFV)
* 네트워크의 기능이 가상화 되어 있는 것.
* Standard 기반의 Volume server, Volume Storage(=disk), switch 존재.
* Virtualized 된 network function SW들

## SDN / NFV
* NFV != SDN
* **SDN** : 스위치 장치에게 받은 패킷 어느 포트로 내보낼지에 대한 길잡이 (기능 연결)
* **NFV** : 박스 안에 국한 된 기능에 관한 것

## SDN / NFV Softwares
* OpenDaylight : OpenFlow controller 컨셉 이미 구현되어있는 소프트웨어 (기존의 통신사 제품까지 제어 가능하므로 복잡)
* ONOS : 새롭게 도입하는 장치에 대해서만 SDN 하고 싶을 때 (단순)
* OpenStack : OpenStack 이후로 클라우드 급 성장 (네트워크 관점에서의 SW 추가)
* OPNFV : open platform for NFV (클라우드 소프트웨어 기반으로 NFV 컨셉 구현)
* Open Network Linux : 외부 통신,…
* OpenWRT : 전세계 유무선 공유기에 들어감

## SDN / NFV Use Cases
* 네트워크에 내가 필요한 SW들 각각 구동 후 필요할 때 인과관계로 연결하면 된다.
* CDN : 캐쉬서버, 유튜브 서버 처음에는 미국 -> 한국에 들어옴 (속도 빨라짐) -> LG U+ 와의 전략적 협력 (더 빨라짐)
* 수많은 기지국 옆에 CPU, Disk 두고 그들을 캐쉬 서버로 쓰면 속도 굉장히 빨라질 수 있다.
* edge computing, edge networking

## SDN / NFV into 5G
* METIS 2020
	* 5G - SDN Controller 가 이동통신 장비들의 줄 관리 함.
	* 그 위에 NFV SW들이 제어
* 5G 이동통신
	* 5G 이동통신에서 네트워크 장치는 어디든 있을 수 있다.
	* SDN, 클라우드(distributed), 네트워크 슬라이싱, Orchestration
	* 이동통신 네트워크는 이제 요구를 받아주는 그릇이다.
* 5G 이동 통신의 기본 철학은 SDN, NFV이다. 
	* 5G는 SDN, 필요할 때 필요한만큼 CPU를  띄우는 Distributed Cloud, 필요한 사람에게 나눠줌을 보장하는 Network Slicing, 다양한 Network Function의 Virtualization, 체계적인 관리 Orchestration로 이루어져 있다.
 
## P4 (Programming language)
* Data Plane 영역까지 코드로 짜겠다
* Layer 2까지도 Speed 지원하면서 완전히 짜겠다!
