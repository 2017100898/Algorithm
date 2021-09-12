# MAC Layer
## Basic Terminologies
* Message
	* 송신하는 쪽에서 수신하는 쪽으로 전달하는 정보
	* text, number, pictures, sound, video …
* Sender
	* 메세지를 송신하는 쪽
	* 휴대전화, computer …
* Receiver
	* Sender가 보낸 메세지를 수신하는 쪽
	* 휴대전화, computer …
* Medium
	* 통신 매체
	* 전화선, 광섬유, 레이저, radio waves …
* Protocol
	* Sender와 Receiver의 동작과 형태 부분 정의

### Data Flow Direction
* 정보를 주고 받는 방향에 따른 명칭
1. Simplex : Device A -> B 일방적으로 보내는 것
2. Half-duplex : 무전기 등 Device A -> B or Device B -> A 중 한 가지만 됨
3. Full-duplex : 전화, 인터넷 등  동일 시점에서 Device A 과 B가 양방향으로 정보 주고 받음

### Physical Structure
* Medium의 연결 방식에 따른 명칭
1. Point-to-Point : 점에서 점을 한 줄로 연결한 것
2. Multipoint : 한 줄에 여러 점이 연결 되어 있는 것


![Types-of-network-topology-2](https://user-images.githubusercontent.com/64299475/132973718-b67b674f-9e8b-447e-a846-63ad2a27cd56.png)

### Topology
* Topology 는 Combination이 가능하다.
* **Mesh**
	* 본인을 제외한 Station과 모두 연결되어 있다. (Full Mesh)
	* Network 묶음들끼리 연결할 때 자주 사용한다. (Network’s Network)
	* 장점
		1. 하나의 Station이 다른 Station에 대해 전용의 링크를 갖고 있다. 방해 불가. 성능이 좋다.
		2. 연결이 고장나도 다른 Station을 경유해서 갈 수 있다. 안정적. 
		3. 보안이 잘 된다.
	* 단점 : Station의 수가 많아질 수록 연결이 매우 많아진다. 물리적으로 힘들다.
* **Star**
	* Hub와 다양한 Station이 연결되어 있다.
	* 장점 : Station이 늘어나도 연결 선은 Station 당 오직 한 줄이다.
	* 하지만 줄이 끊어지면 해당 Station은 통신을 못한다. 하지만 다른 Station들은 영향을 받지 않는다.
	* 단점 : Hub가 고장나면 Station들은 모두 통신이 두절된다.
* **Bus**
	* 한 줄을 여러 개의 컴퓨터가 공유하는 형태다.
	* 장점 : 설치가 용이하고 가격이 저렴하다. 
	* 단점 : 줄이 끊어지면 모든 통신이 두절된다.
* **Ring**
	* 동그랗게 원을 만들어서 연결 되어 있다.
	* 장점 : 설치가 용이하고 가격이 저렴하다. 
	* 줄이 끊어질 때 대비를 해두면 괜찮지만, 대비를 해두지 않으면 위험하다.
	* 단점 : 줄 내에서 충돌이 일어날 수 있다. Half-duplex System을 도입할 수 밖에 없고, 시간 지연이 발생할 수 있다.
* **Hybrid**
	* 4개의 Topology를 섞어서 사용한다.

### 네트워크 규모에 따른 명칭
* BAN (Body Area Networks)
	* 워치, 심박수 등 … 사람을 기준으로 만든 것
* PAN (Personal Area Networks)
	* 컴퓨터와 키보드 등 매우 가까운 거리 연결한 것
* **LAN (Local Area Networks)**
	* 하나의 방, 층, 건물, 캠퍼스 등을 연결한 것
	* 대부분 한 소유주가 전체를 가지고 있는 경우다.
	* Wireless
* **MAN (Metropolitan Area Network)**
	* 도시 규모의 Network
	* LAN을 연결한 Netwok
* **WAN (Wide Area Network)**
	* 큰 Network 들을 연결하는 줄을 뜻한다.
* LAN-MAN-WAN의 Combination도 가능하다.
* 모두 유/무선이 존재한다.
* MAN, WAN 이상의 기술도 존재한다.

### 상호 연동성에 따른 명칭 (Standards)
* By Law
	* 법을 지키도록 하는 것.
* By Fact
	* 법은 아니지만 사람들이 표준으로 사용하고 있는 것.
	* ex. microsoft, 한글

## MAC (Multiple-access protocols)
* **Random-access protocols**
	* ALOHA
	* CSMA/CD : 이더넷
	* CSMA/CA : 무선랜
* **Controlled-access protocols**
* **Channelization protocols**

![images-2](https://user-images.githubusercontent.com/64299475/132973749-6b28e432-b26d-4339-af25-ed671bcbdd5c.png)


## Random Access Protocols
* 알아서 독립적이고 분산적으로 접근하자.
* 컨트롤 타워가 없다.
* 송신을 하고자 하는 Station이 있으면 본인이 **독립적으로, 자발적으로** 데이터를 쏜다. -> 충돌 발생 문제

### ALOHA
* 보낼 데이터가 있으면 쏜다.
* 에러가 나면 쉬었다가 몇 번 더 시도해보는 단순한 시스템.
* 과거에는 간헐적 소량의 데이터를 주고 받았기때문에 가능했다.
* 타 Station과 충돌이 일어날 수 있다.
* 품질을 보장할 수 없다.

### Slotted ALOHA
* 메시지들이 시작하는 시간과 끝나는 시간의 구역을 만들어서, 꼬리의 꼬리를 물어서 통신 불능상태로 가는 것은 방지하는 시스템이다.
* 시간을 맞춰야 한다는 것이 단점이다.

### CSMA (Carrier sense multiple access)
* 메세지를 케이블에 싣기 전에 들어보고, 전자신호가 있으면 쏘지 않고, 아무런 신호가 없으면 내가 데이터를 전송하는 시스템이다. 충돌확률을 줄일 수 있다.
* 전파 지연으로, 지금 당장은 전자신호가 없을 수 있지만 가는 길에 데이터가 섞여서 깨져버리는 문제가 있을 수도 있다.
* propagation delay 만큼 기다리지 않으면 충돌문제를 피할 수는 없다.

#### Behavior of 3 persistence methods
1. 1-persistent : 채널을 끊임없이 보고 있다가 채널이 비면 내가 반드시 쏘는 것. 지연효과에서 제일 좋지만, 끊임없이 보는 전력이 많이 쓰이게 된다. 바로 쏘면 충돌 확률이 높아진다.
2. Nonpersistent : 센싱하다가 채널이 바쁘면 쉬고, Random하게 다시 센싱 후 비어있으면 내가 쏘는 것. 지연이 발생한다.
3. p-persistent (hybrid) : 끝나는 시점은 알지만 그때 모두가 쏘면 에러가 발생하기 때문에 Random하게 쉬고, 다시 와서 쏘는 것.

### CSMA / CD
* 송신을 하면서 내 신호를 듣고 있다가 **충돌을 탐지하면 전송을 중지**한다.
* 충돌 된 데이터는 결국 무용지물이 되지만, 버려지는 시간을 줄일 수 있다.
* 이더넷 만들어내는 데 공을 세웠으며, 아직도 기반 기술로 사용되고 있다.

### CSMA / CA
* 무선에서는 자신이 보내고 있는 것을 동시에 듣는 행위 어려웠다.
* 따라서 CSMA / CA에서는 **충돌을 탐지하지 않고 사전에 피하는 것**이다. 하지만 이 과정에서도 다른 네트워크가 신호를 놓칠 수도 있기 때문에 _에러를 완전히 없앨 수는 없다._
* **RTS** : 데이터 보낼 것임을 알림 ( = 들어오지 마! )
* **CTS** : 데이터 보내는 중 …  (= 들어오지 마!)
* **ACK** : 데이터 잘 도착했음을 알림 ( = 들어와도 돼!)
* CSMA 1-persistent + CSMA
* Contention Window : RTS, CTS 메시지 주고받는 공간

## Controlled Access Protocols
* 중앙 통제자가 있으므로 명령을 받아 일할 수 있다.

### Reservation (예약) 
* n번 네트워크가 쏠 시간이 되면 쏜다.
* 장점은 충돌이 발생하지 않는다.
* 단점은 내가 쏘고 싶을 때 바로 쏠 수 없고 예약 후 기다려야 하므로 지연시간이 증가한다.

### Polling
* Station에게 보낼 데이터 있는지, 받을 수 있는지 물어본다.
* 충돌이 거의 발생하지 않는다.
* 보낼 데이터가 없음에도 불구하고 메시지를 주고 받아야 하므로 낭비이다.
* 지연이 증가한다.

### Token Passing
* Token은 권한을 뜻한다.
* Station이 돌아가면서 발언권을 갖는다.
* 지연이 발생한다.
* 하지만 채널 효율이 좋고 충돌이 없다.

## Channelization Protocols
* multiple한 Station을 어떻게 공유할 것인가?

### FDMA (Frequency-division multiple access)
* Station 별로 전용 주파수를 준다.
* 하지만 주파수는 매우 비싸다.

### TDMA (Time-division multiple access)
* 음성을 일정 단위로 쪼갠 뒤, 압축해서 n배 빠른 네트워크에 실어 보내버린다.
* 받아서 1/n배로 늘여서 음성을 원 속도로 들려준다.
* 압축을 해서 보내주는 것이기에 지연 시간이 발생할 수 밖에 없다. 하지만 불편한 정도는 아니다.
* Time 안에서 Station 별로 구간을 나눌 수 있다.
* FDMA의 하나의 Frequency 를 또 n개로 쪼개서 Station을 배치할 수 있다.

### CDMA (Code-division multiple access)
* 내가 데이터를 쏘지 않으면 굉장히 소량의 데이터가 흘러간다.
* 내가 데이터를 쏘면 굉장히 큰 데이터가 흘러간다.
* 암호화 기술과 관련 있다.
* 본인이 곱할 데이터(d)에 코드(c)를 곱한다. 
	* 본인의 데이터 * 본인의 코드 = 1
	* 본인의 데이터 * 다른 코드 = 0
	* c를 알면 데이터 풀 수 있고 모르면 데이터 못 본다.

