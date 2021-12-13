# Game Networking
## Definition
* Game Server :  수많은 사람들이 네트워크를 사용하여 가상의 공간 안에서 게임할 수 있도록 하는 서버
* Low - latency
* **Dedicated Server**
	* **Master Server** : 게임을 하기 위해서 합법적인 유저인지 확인하고 게임 서버에 넣는 서버. 트래픽이 많지는 않으나 보안이 매우 중요하다.
	* **Game Server** : 실제로 게임의 로직을 돌리는 서버, CPU 효율이 매우 높고 트래픽이 많다. 프로그램을 매우 잘 짜야한다.
* **Peer-to-Peer** : 게임 서버가 없는 경우
	* local area 안에 같이 존재하는 유저가 있을 때, 그들끼리 서버를 두지 않는다.
	* 들어올 수 있는 사용자의 제약이 있으며 상태 불일치 제어가 중요한 관건이다.
	* webRTC를 사용하면 web browser 위에서 게임을 돌릴 수 있고,  서버의 역할은 나눠서 한다.

## MMO Game Servers
### Photon
* Relay 기능 (1번 유저에게서 받은 트래픽 다른 유저에게 전달) 
* Client hosted (클라이언트의 복잡도가 올라가 있는 게임)
* self hostide (PaaS)
* OnPremise (스스로 컴퓨터를 구비하고 소프트웨어는 라이센스비 내고 빌려쓰는 것)

### Agones
* 구글 클라우드
* 구글은 Ubisoft와 함께 Agones dedicated 오픈 소스 게임 서버를 제공하고 있다.
* 전통적 방법 : 게임 회사는 본인만의 서버를 만들고 서버 관리, 운영하는 프로그램 서버도 만들어야 한다. 하드웨어, 소프트웨어 인프라 모두 책임져야 한다.
* Agones : 마스터 서버에 상응하는 일을 줄여주는 일을 한다.쿠버네티스 기반, 서버 유지 및 운영을 편하게 할 수 있다.
* Agones를 통해 게임 회사는 서버 앞단과 실제 게임 로직만 짜면 된다.

### Colyseus
* realtime multiplayer, turn-based multiplayer, scalable,…
* 게임 엔진에 대한 부분은 게임회사가 직접 해야 한다.
* 그래픽 렌더링 등은 없다.
* 서버와 클라이언트 기반의 네트워크 게임, 자바스크립트에 관심 있으면 콜리세우스를 사용하는 것을 추천한다.

### GameSparks
* amazon
* real-time control 

### PlayFab
* Microsoft

### Unity
* New unity multiplayer features

### IFUN Engine

## Public Cloud Solutions
### Google Cloud Platform
* 구글은 오픈 소스를 제공해서 결국 서버에서 게임 개발자가 해야 될 것을 최소화해주는 노력을 하고 있다.
* Google Stadia
* 구글은 크롬 브라우저가 올라가는 것들 위에서 돌아가는 게임들과 게임 콘솔도 확보하고 있다.
* Database, query, biodata, storage, …
* 결국 개발자는 게임 서버만 잘 짜면 된다.
* 쿠버네티스 기반 Agones를 통해 게임 서버를 만들고 운영하면 된다.

### Amazon GameLift
* 서버호스팅 : 스파크에 의해 가능하다.
* 개발자의 능력이 크다면 아마존의 low latency 장점을 더욱 잘 발휘할 수 있다.

## Streaming Games
### Concept
* 그래픽 랜더링 등의 작업은 모두 클라이언트가 한다.
* 본인이 다른 사람과 share 해야할 정보만 네트워크를 타고 서버로 간다.
* 즉, 클라이언트가 매우 heavy 한 상태다.
* Thin Client에서는 프로세싱을 거의 하지 못 한다. 
* `네트워크를 통과해서 갔다오는 지연이 상당히 적다면` 네트워크가 흔들리지 않는 Rate, loss를 보장하고 처리 속도가 빠른 것을 스트리밍 게임이라 부른다.

### Sony PlayStation Now
* 플레이스테이션 컴퓨터가 없더라도 단순하게 입출력과 동영상 스트리밍 할 수 있는 능력을 가진 디바이스만 있다면 플레이스테이션 게임을 할 수 있다.

### Microsoft x Cloud
### Google Project Streaming

## Networking Issue
### Latency & QUIC
* http 1의 지연 시간은 크기도 하지만 편차가 크다. 게임은 편차가 작은 게 좋다.
* http 2의 지연 시간은 그나마 좋아졌지만 편차는 크다.
* http 3.0, QUIC은 지연도 작아지고 보는 것과 같이 이 지연의 차이가 굉장히 줄어들었다.

### Deep Traffic Analysis & IDEAs
