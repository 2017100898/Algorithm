# Network - 1
## Concepts
* **내가 가진 Packet을 어디에 전달해야 하는가?**
* IP : 네트워크 레이어에서 현재 시점에서 가장 많이 사용되는 SW
* Internetworking : Network 간의 통신  ( internet )
* A -> B 전달하기 위해 길을 선택하는 역할 ✔️

### Host-to-Host Communication concept
* Host = computer
* 3계층, 굉장히 많은 컴퓨터가 있을 때 원하는 목적지까지 잘 보내는 것
* Router :  받은 메세지 어디로 보낼지 결정하는 장치

### Packetizing
* 4계층에서 내려온 메시지를 2계층으로 보내기 전에 network layer 본인이 필요한 정보를 추가하는 행위 ✔️
* The first duty of network layer.
* message = packet

### Routing and Forwarding
* 네트워크 계층에서는 packet을 받아서 내보낸다. 고로 그것을 하기 위한 정보가 필요하고, 그래서 네트워크 계층에는 **table이 항상 있다**.
* Routing: 패킷을 destination까지 보내기 위해 라우터가 **최적의 경로 찾는 것**
* Forwarding: 패킷이 라우터에 도착하면 **forwarding table의 Output interface에 맞게 보내는 것**

## Datagram and Virtual Circuit
* **Datagram** : Routing에 '주로' 사용 (인터넷)
* **Virtual circuit**  : Forwarding 에 '주로' 사용 (전화기) 
* 차이점 : 연결 설정을 할지 말지

### Datagram
<img width="760" alt="스크린샷 2021-10-24 오전 1 50 51" src="https://user-images.githubusercontent.com/64299475/138564931-535ba93c-c908-436e-a923-1f14a5e5fb6c.png">

* **Connectionless** : 연결 설정 해제 과정이 없음.
* ALOHA, 이더넷처럼 보내고 싶을 때 보냄
* 라우터는 받아서 내가 가진 정보로 원하는 지점으로 보냄
* A -> B 3개의 메시지를 보내면 각 라우터마다 길이 다를 수도 있다.
* **패킷들이 다 독립적이기 때문에 같은 목적지로 가더라도 다른 줄로 내보낼 수 있다.** 따라서 보낸 순서와 받은 순서가 다를 수 있다.
* **라우터 중 하나가 부서지면 연결 된 라우터들은 그것을 알 수 있다.** 인근 라우터들은 다른 길을 찾아서 안정적으로 패킷 보내줌. 모든 장치는 각각 대등하고 독립적으로 동작. (~인터넷)

#### Forwarding process in a router
<img width="572" alt="스크린샷 2021-10-24 오전 1 53 10" src="https://user-images.githubusercontent.com/64299475/138565016-9ef24db6-1f7e-409c-a030-0bd381661b46.png">

* 네트워크 계층에서는 **Table 필수**
* 패킷 안의 데이터그램 안의 destination address 보고 출력하는 interface로 보냄
* input : 현재 받은 packet의 정보
* output : 어느 줄로 보낼지

### Virtual Circuit
<img width="574" alt="스크린샷 2021-10-24 오전 1 54 00" src="https://user-images.githubusercontent.com/64299475/138565038-014e08ab-a427-42cf-b612-3a695dbdb951.png">

* **connection setup** : 연결을 할 때 어떤 장치 통과할지 미리 조정해 놓는 것
* 연결을 먼저 하고 데이터 송수신되기 때문에 **데이터들의 목적지 같으면 똑같은 경로로 전달**
* Table의 정보 datagram과 다름
* input : port, Incoming label (ex. L1… 줄에서만 의미 있음)
* output: port, Outcoming label
* 복잡한 연결 설정 과정을 마치고 나면 전달 속도 빨라짐

#### example
* A는 R1에 정보 전달 + 연결 설정 요청
	* 최초에는 Label 없음. R1은 저장, Label R1이 채움 (14)
	* 최초에만 어디로 보낼지 고민 
	* R3에게 정보 전달 + 연결설정 요청
	* R3이 Label 새로 채움
	* R4 마찬가지로 Label 채움
* B에 도착 후 B에 연결 설정 요청
* 각각 table의 outgoing level 받은 쪽에서 채움 (B->R4->R3->R1)

## Network Performance
* 네트워크 계층의 서비스를 이용하는 상위 계층 프로토콜들은 이상적인 서비스를 받을 것으로 기대하지만, 네트워크 계층은 완벽하지 않다. 
* 네트워크의 성능은 지연, 처리량, 패킷 손실의 관점에서 측정될 수 있다. 

### Delay
* Packet 전달 시 Source host -> Destination host 까지의 걸리는 시간 (지연)
* 네 가지 유형
	* **transmission delay (전송지연)** : 인간이 만든 것, 표준 규격에 의거 전달하는 전송 지연
	* **propagation delay (전파지연)** : 재료 등 자연이 만들어내는 지연 
	* **processing delay (처리지연)** : 하드웨어와 소프트웨어를 사용하기 때문에 발생하는 지연
	* **queuing delay (큐지연)** : 대기로 인해 발생하는 지연
* 계산 가능, 계산 후 우리의 요구 수준 부합하는지 판단이 필요하다.

### Throughput
<img width="580" alt="스크린샷 2021-10-24 오전 2 02 58" src="https://user-images.githubusercontent.com/64299475/138565291-adeea3d0-ea4e-41c5-be60-afa2cb3aca29.png">


* 첫번째 의미 : 입력이 네트워크의 어느 지점에서 얼마나 흐를 수 있는지? (속도)
* 두번째 의미 : 입력에 비해 출력이 얼마나 나왔는지? (소수점으로 표현)
1. **Data rate** : 줄이 얼마만큼의 속도 제공할 수 있는가?
	* source-destination 최대속도는 가장 느린 줄의 속도 (Transmission rate)
	* 이렇듯 가장 느린 줄이 제약을 가하는 현상을 Bottleneck이라고 함 - 이를 제거하는 것이 중요
2. Throughput 모르는 경우 있음. 
	* 모르는 부분에서의 Throughput 값 맞출 수 있도록 요구해서 network performance의  Throughput  유지할 수 있어야 함.

### Packet Loss
* 내가 보낸 메시지 중에 몇 개가 없어졌는가?
	* 감당할 수 없을만큼의 입력 버퍼 들어오거나  3계층에서 버퍼 오버플로우 시 패킷 유실
* 장치 안에 버퍼가 얼마나 있고 혼잡도가 얼마인지 계산할 수 있어야 함. Congestion control 필요.

### Congestion control (혼잡제어)
* 네트워크 계층의 혼잡은 처리량과 지연 두 가지 문제와 관련 있다.
* switch, router 너무 과다한 데이터 받았거나 혹은 특정링크로 데이터가 가는 게 몰린 케이스
	* 3계층에서 datagram 방식 쓰게 되면 loss 피할 수 없으며, 4계층은 필수적으로 에러 검출 및 복구를 할 수 밖에 없고, 4계층에서 Congestion 풀기 위한 기능이 들어 감.
	* 2계층: 1계층과 2계층 자체의 에러검출 및 loss와 congestion 방어
	* 4계층: 3계층 및 그 이하의  에러검출 및 loss와 congestion 방어

### Packet delay and throughput as functions of load
<img width="567" alt="스크린샷 2021-10-24 오전 2 07 32" src="https://user-images.githubusercontent.com/64299475/138565410-330c0768-30cd-4f82-bd0e-035d3b06c55f.png">

* 왼쪽 그림 :  버퍼 무한하면 congestion 발생 시 무한으로 뻗는다.
* 오른쪽 그림 : buffer 유한하다면 일정 지점까진 올라가다가 뒤에는 알 수 없음.

## Addressing
* IPv4 address 
* IP address는 **줄**에 주는 것: 컴퓨터가 두 개 이상의 줄을 갖고 있으면 줄마다 address 부여.
* 라우터가 address 갖는 것이 아니고, 줄에 address 부여.

### IPv4 Address Space
* 패킷이 있다면 주소 적는 field 있고, 이러한 address space 유한한 크기로  존재.
* IPv4는 32bit 의 주솟값 가짐.

### Hierarchy in addressing
* 현재는 컴퓨터가 매우 많음.
* 국가-기관- … 단위로 쪼개서 IP 주소 나눠줌.
* **Prefix** : 네트워크 정의 (n bits)
* **Suffix** : 네트워크 내 호스트, 컴퓨터 의미 (32-n bits)

### Classful Addressing
<img width="581" alt="스크린샷 2021-10-24 오전 2 12 26" src="https://user-images.githubusercontent.com/64299475/138565589-6f0db79c-d272-47bf-ba82-05187a0c5283.png">

* 얼마만큼의 Prefix 부여? Prefix위해 몇 bit 쓸까?
* 처음: 8bit, 16bit, 24bit 짜리 Prefix 구현
* A = Prefix (8bit)
* B = Prefix (16bit)
* C = Prefix (24bit)
* D = Prefix (not applicable)
* E = Prefix (not applicable)
* 하지만 이렇게 잘라주기에는 컴퓨터 쓰는 사람이 너무 많고 문제가 있다.

### Classless Addressing
<img width="525" alt="스크린샷 2021-10-24 오전 2 12 37" src="https://user-images.githubusercontent.com/64299475/138565586-94db7955-54b0-4783-8a15-aa1c2fadb581.png">

* 클래스가 없는 것, 가변적으로 n bit 구현
* IP address 부족한 문제 발생
* 하지만 이미 있는 것 버릴 수 없으므로 4바이트 제한 하되, n-bit 개념으로 prefix 할당하는 개념 도입하게 됨.

### Slash notation
* 몇 bit가 network prefix인지 알려줄 방법 별도로 필요.
	* `12.24.76.8/8`에서는 8비트가 prefix임을 판단. (12)
	*  `23.14.67.92/12` 에서는 8+4비트, 14를 비트로 펼친 다음 앞쪽에 4비트까지 prefix
* router가 알아야하는 것은, **나에게 연결된 네트워크와 그 네트워크의 prefix**

### Example of address aggregation
<img width="584" alt="스크린샷 2021-10-24 오전 2 14 11" src="https://user-images.githubusercontent.com/64299475/138565629-6bf3e13b-61cf-4563-9bcf-f72dc0d28980.png">

* 조직이 하나의 network prefix 할당받으면 내부적으로 주소를 잘라야 함.
* 우리 조직 바깥에 있는 사람은 우리 조직 내부에서 어떻게 돌아가든 관심 X
	* 내부적으로는 26비트까지 가야 network이지만 모두 연속적이고 larger block이 이를 커버하므로, 바깥에서는 주소를 합쳐서 24비트만 봄.

## More Issues
* IP address가 부족해서 나온 기법들

### DHCP (Dynamic Host Configuration Protocol)
1. host 나 node에 네트워크 환경을 자동으로 설치하는 방법
2. ip address 재사용 - 컴퓨터가 필요할 때 ip address 가져가고 다 쓰면 반납

#### Message Format
<img width="572" alt="스크린샷 2021-10-24 오전 2 15 17" src="https://user-images.githubusercontent.com/64299475/138565666-5f62b125-0592-4827-99f8-59838dcfd58d.png">

* DHCP의 Message format에는 Client ip address, server ip address, gateway ip address, client hardware address 등이 있고, 이를 주고 받음으로써 ip 받아서 본인의 기기에 셋팅 가능.
* Option field 사용하면 의미 담을 수 있음: DHCPDISCOVER, DHCPOFFER… 등 필드 채워서 전송

#### Operation
<img width="438" alt="스크린샷 2021-10-24 오전 2 15 55" src="https://user-images.githubusercontent.com/64299475/138565683-007bc556-1fbb-4ab9-a76c-e56e7f296985.png">

* Client는 Server로부터 offer 받은 address로 source address 채움.
* 임시로 IP 쓰고 반납하기 때문에 허용 시간 초과하면 재요청 또는 연장.
* 노트북이나 휴대폰으로 유무선 공유기에 접속할 때마다 해당 과정을 반복.

### NAT (Network Address Translation)
<img width="574" alt="스크린샷 2021-10-24 오전 2 16 37" src="https://user-images.githubusercontent.com/64299475/138565700-852cf850-5bd6-451d-92d1-11090dff946a.png">

* **Private address** : 지역 안에서만 의미 있는 IP 주소
* **Universal address** : 전세계에서 유니크하게 사용하는 IP 주소 (=public address)
* 유무선 공유기는 Universal address를 하나 부여받고, 집 안에 Private zone을 만든다. (=> NAT, 노트북마다 다른 Private address)

#### Address translation
<img width="589" alt="스크린샷 2021-10-24 오전 2 18 53" src="https://user-images.githubusercontent.com/64299475/138565757-aaca1c20-ba35-4ea0-92f5-6f0006e973dd.png">

* NAT router을 통과하여 인터넷으로 나갈 때는, Source address -> Public address로 바뀐다.
* 반대로 인터넷에서 받을 때는 Public -> Source 로 바뀐다.
* 이럴 때는 인터넷에서 정보 받을 때 누구에게 전달해야되는지 모르는 문제점 발생한다.
	* 따라서 Source address만 보는 것이 아닌 더 많은 것을 봐야 한다. (Source address, destination address, port number 등… 구분할 수 있는 정보 끄집어내야 하고, 우리가 쓸 수 있는 정보는 IP Frame 안에 있는 정보들)
	* NAT 는 표준 Scheme이 없고 업체마다 고유한 알고리즘 만듦.
* 통신사업자는 거대하고 Private한 network zone

#### Longest mask matching
<img width="543" alt="스크린샷 2021-10-24 오전 2 19 33" src="https://user-images.githubusercontent.com/64299475/138565775-4553c2e5-d387-4084-ba01-8bff44463230.png">

* network address는 **위에서 아래로 (prefix 긴 것 중심으로)** 찾아간다.
* 네트워크는 뿌리가 있고 뿌리로부터 퍼지며 Hierarchical 하게 이뤄져 있다.

#### Forwarding based on destination address
* destination network를 찾아서 내려가다가 match 되면 Found -> Found된 곳으로 내보냄.
* 부하가 크지만 연결 및 해제 설정 X

#### Forwarding based on label
* hash 값을 통해 next label 을 쉽게 알 수 있으므로 Lookup 기능 없어지고 바로 찾을 수 있음.
* 연결 및 해제 설정 필요

## IP Protocol
* 네트워크 레이어로서, 현재 인터넷을 지탱하고 있는 SW

### Format
<img width="514" alt="스크린샷 2021-10-24 오전 2 21 22" src="https://user-images.githubusercontent.com/64299475/138565811-f56274e3-db8d-4362-8fe5-40d31a237a61.png">

* IP protocol의 header는 가변적이다. 20~60byte.
	* option 을 통해 새로운 기능 확장 가능.
	* Source ip address / destination ip address
	* Protocol / Time-to-live (loop 방지) …
	* header length / service type… 
* header 뒤에 payload 들어감.

### Multiplexing
<img width="475" alt="스크린샷 2021-10-24 오전 2 22 42" src="https://user-images.githubusercontent.com/64299475/138565840-8e7c39e5-5421-4168-a45e-c4db88169340.png">

* Network layer 위에 Transport layer 올라감. (TCP, UDP)
* Network layer 안에서도 IP 위에  ICMP, IGMP, OSPF을 올릴 수 있음.
* 하나의 ip 프로토콜 위에 여러개의 프로토콜 돌아갈 수 있다는 가정하에 multiplexing 개념 적용 가능.

### Fragmentation
* Layer 2는 Layer1의 특성 반영. 필연적으로 맞물림.
* IP protocol은 내가 보낼 network 장치의 IP 최대 사이즈 (2계층 패킷 사이즈)에 맞춰서 패킷 사이즈 조정해야 함. (= Fragmentation)

### Maximum transfer unit (MTU)
* Layer2에서 받을 수 있는 최대 사이즈. 넘어가면 쪼개서 보내야 함.
* 총 4000byte의 IP frame (0000~3999) 
	* 3개로 찢어지면, 0 ~ 1399 / 1400 ~ 2799 / 2800 ~ 3999
	* **Offset field** : 본인이 전달한 메시지의 최초의 것 : 0으로 계산, 8로 나눔
	* Offset 값 : 0000/8 = 0 , 1400/8 = 175, 2800/8 = 350

### Security
* IPv4는 보안까지 신경쓰지 않음.  (IPsec 별도로 같이 씀)
* security는 성능을 많이 저하시키므로 필요에 의해서만 해야 함.

### ICMPv4
* IP protocol 이 제대로 동작하는지 관리하기 위한 프로토콜
* 지연, 에러 리포팅, 정보 쿼리,…
* 예시
	* IP를 받으면 IP message의 헤더 및 데이터를 ICMP 프로토콜에 준다. ICMP는 header를 붙여서 돌려준다. -> 이를 통해 네트워크 및 링크, 라우터 살았는지 판단 가능 (디버깅)
		* **Ping** : 상대방이 살아있고 중간 과정의 네트워크 장치와 줄들이 모두 괜찮다는 것, 안정적 동작, 갔다 온 시간, 네트워크 지연 파악 가능.
		* **Traceroute** : TTL 늘려가면서 n번째 장비까지 보내고 응답 받음. 중간에 거쳐야하는 장치들을 하나하나 Ping해봄. Ping 했을 때 응답 안오면 어떤 장치에 문제가 있는지 traceroute 통해서 파악 가능.
		
### Mobile IP
* 지역과 상관 없는 가상의 IP
* 사람이 봤을 땐 안 바뀌지만, 밑바닥에서는 끊임없이 위치정보에 해당하는 IP 할당함.
* 주로 회사에서 사용. 바뀌지 않는 IP address 사용하기 위함. 