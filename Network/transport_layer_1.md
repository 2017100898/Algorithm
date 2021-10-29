# Transport Layer - 1
## Transport Layer Basic
* 원하는 destination computer 까지 도달했을 때, destination SW 찾는 작업
* **Process-to-Process Delivery**
	* 컴퓨터 안에서 여러 프로그램 중에 어떤 것이 destination인지 찾는 작업
* 일반적인 형태는 **Client-Server 아키텍쳐**이다.
	* 두 프로세스는 Client와 Server 관계가 된다.
	* Client : 요구를 하는 쪽
	* Server : 요구 받아 처리하는 쪽
* 아래 네 가지 정보 갖고 동작하는 경우가 일반적이다.
	* Local Host
	* Local Process : host 내의 프로세스 (프로세스 고유의 주소로 판단)
	* Remote Host (상대, network 주소로 판단)
	* Remote Process 

### Addressing
<img width="427" alt="스크린샷 2021-10-20 오후 8 45 58" src="https://user-images.githubusercontent.com/64299475/138086854-c62776ee-f0c4-44a0-80f6-c2f0eb003f7a.png">

* Host 안에서 어느 프로그램이 통신의 대상인지 식별하는 과정 필요하다.
	* Data link layer에서는 MAC address 알아야 된다.
	* Network layer에서는 IP address 알아야 된다.
	* 그리고 **Transport layer는 Port number (address)** (0~65,535)를 알아야 된다.
* 사진에서의 Source code 번호는 52000, Destination code 번호는13이다.

### Socket Addresses
* 4계층 위에서 코드를 작성하는 사람이라면, IP address, port number 함께 생각하는 사람이 많다.
* **Socket Address = IP+Port number** `120.231.010.10:80`

### Multiplexing and Demultiplexing
<img width="450" src="https://user-images.githubusercontent.com/64299475/138580466-e00fd310-6d17-4d5b-9c67-3f75d614cd00.png">

* Multiplexing : 하나의 IP 위에서 여러 개의 프로세스 동시에 활용하는 것
* Demultiplexing : 하나의 IP에서 온 것을 여러 개의 프로세스에 배정하는 것

### Connectionless vs Connection-Oriented Service
* **Connection-Oriented**
	* 데이터 주고받기 전에 연결설정 과정 존재, 해제 과정 필요
	* ex. TCP (연결설정, 데이터 주고받음, 혼잡제어, 흐름제어, 에러검출), SCTP (TCP 보다 신뢰성 보장, but 막 쓰면 안 됨)
* **Connectionless**
	* 필요할 때 필요한 것을 보낸다. (ACK X, 패킷 번호 X)
	* 연결, 해제 과정이 없다.
	* ex. UDP

### Reliable vs Unreliable
* 신뢰성 보장 - TCP (느리다)
* Unreliable - UDP (빠르다, 에러검출 등이 없음)
* **신뢰성 보장 해야하는 서비스 있으면 transport layer 에서 신뢰성 보장을 위한 에러 검출 등을 해야한다.** 아니면 Application이 직접 신뢰성 보장을 해야 한다.

## User Datagram Protocol (UDP) ☁️
* 에러 검출 및 복구 없다.  (Connectionless)
	* 오직 **checksum**만 있다.
	* checksum : 네트워크를 통해 값이 변경되었는지 검사하는 값
* 모든 UDP 패킷은 독립적이다.
* **UDP는 사용자의 데이터를 실어 나르는 프로토콜으로, 신뢰성 보장 안 해도 되는 작은 메시지 간헐적으로 주고 받을 때 주로 사용한다.** 유실될 수도 있다.
* Process to Process, Port address 집어넣을 수 있게 됨으로써 어느 프로그램이 어느 프로그램에 전달하는지 알 수 있는 것이 중요하다.


### Frame Format
<img width="427" alt="스크린샷 2021-10-20 오후 9 05 19" src="https://user-images.githubusercontent.com/64299475/138089431-754b349b-2231-400f-82c7-6790aa40fa0b.png">

* Source Port, Destination Port, UDP total length, checksum, (padding) …
* 어느 프로세스가 보냈는지에 대한 *식별*과 어느 프로세스로 보내야하는지에 관한 정보전달 (제일 중요한 기능)
	* **Encapsulation and Decapsulation** 
### Queuing at Client Site
<img width="450" src="https://user-images.githubusercontent.com/64299475/138090777-bd1c606a-e80d-4c21-875c-847d6f336921.png">

* Server가 Client 보다 항상 먼저 동작하고 있어야 한다.
	* TCP도 동일하지만 UDP는 연결 설정 과정이 없기때문에 필수적이다.
	
#### Client
* 프로세스 살아나면 본인의 random Port number OS로 부터 받는다. 
* source port 번호로 사용한다.
* UDP 에게 전달 및 포트번호 기반으로 헤더 만들고 완성한다.
* UDP 헤더가 붙은 데이터를 IP에 전달한다. buffer가 꽉 찼으면 5계층 ⇒ 4계층으로 데이터를 내릴 수 있다.
* 3계층에서 데이터 및 UDP 받아서 해당하는 어플리케이션 destination 번호를 보고 해당하는 것에 데이터 전달

#### Server
* 기본적으로 대기, 프로세스 시작시 특정 포트 열어놓고 데이터 기다림
* well-known port 점령
* 데이터 받아서 destination port address 보고 적절한 Port address에 전달

### Applications of UDP
* bulk data에서는 사용하지 않고, 소량 데이터 보낼 때 간헐적으로 사용한다.
* TFTP
* Routing Information Protocol (RIP) : 근처 Router 정보 알고싶을때
* SNMP - management process

## Transmission Control Protocol (TCP) ☁️
* TCP는 Connection-oriented이다. 
	* 누군가가 상대방에게 연결요청- 상대방이 응답 - 서로 확인 시 데이터 주고 받는다.
* TCP는 두 프로세스 사이에 Virtual한 connection을 생성하고 인터넷을 통해 그들의 데이터를 전송한다.
* Buffer를 만들고, 보내고자 하는 데이터 없어지면 Buffer 지우고 연결 해제한다.
* 에러 검출 및 복구, 흐름제어가 가능하다.
* **결국 시퀀스 넘버와 ACK, NCK 메시지가 제일 중요하다.** (DataLink와 동일)


### Stream Delivery Service
* TCP is a **stream-oriented protocol**
* 메시지 단위가 아닌 **byte 단위로 센다.** (Stream of bytes, 패킷 아님)
* 보내는쪽 : sequence 
* 번호 받는쪽 : ack에 의해 응답 but 메시지 번호와 상관없이 byte 사용한다.

### Sending and Receiving Bufers
<img width="511" alt="스크린샷 2021-10-22 오후 4 01 19" src="https://user-images.githubusercontent.com/64299475/138546041-6f9f0c79-354b-4561-bfc2-5c5bfbf19f54.png">

* 유한한 버퍼를 유지하기 위해 Circular Queue 를 만든다.
	* 분홍색 : 보내야함 (대기)
	* 하얀색 : 비어있음
	* 회색 : 보냈는데 응답 없음

> sending process가 메시지를 보내면 next byte to write에 쓰고, 회색 처럼 보내고   
> 받은 receiving process는 next byte to read에 쓰고 시간 될 때 읽으면 된다.  

### Segments
* TCP 에서 주고 받는 메시지의 단위, byte의 묶음 ⇒ **segment**
* 헤더 붙여서 IP layer (네트워크 계층)로 보내고, IP layer에서 encapsulation 되고 전송된다.
* out of order, lost, corrupted의 경우에 재전송 한다.

### Full Duplex Service
* TCP는 Full Duplex로 동작한다.
* 양방향 전송이 가능하며 동시에 송수신 가능하다.
* Piggybacking : 내가 보내는 데이터에 ACK 붙여서 보낼 수 있다.

### Byte numbers
* _TCP에는 segment number (메시지 번호) 따로 쓰는 곳 없다._
* Byte 단위를 세려서 사용한다.
* 내가 보내고 싶은 byte 6000 일 때, 시퀀스 넘버가 1057이면,
	* 1000바이트 먼저 보내자 `1057~2056` (segement num : 1057)
	* 1000바이트 또 보내자 `2057~3056` (segement num : 2057)
	* 다 보낼 때까지 계속 반복하며,  **segment 번호는 내가 보내는 바이트의 첫 번째 번호가 된다.**
* segment 번호가 아닌 byte의 개수를 통해 에러 검출 및 복구, 흐름제어를 한다.
* 연결 설정 과정에서 **최초로 사용할 시퀀스 번호는 random 번호**로 설정한다. (보안 등을 위함)

### ACK number
* 단위가 byte로만 바뀌면 된다.
* `n까지 잘 받았고 n+1 보내줘! 를 byte로...`

### Control Field
<img width="403" alt="스크린샷 2021-10-23 오후 4 51 37" src="https://user-images.githubusercontent.com/64299475/138547735-25123ee6-574a-4f88-8c10-24658ececac5.png">

### Connection Oriented?
* Sender와 Receiver 사이에 **가상의** path 만들었고, path를 통해 모든 데이터 주고 받는다. 따라서 physical layer는 건드릴 수 없다.
* 에러 검출 및 복구를 위한 재전송도 path위에서 이뤄진다.
* `IP를 믿을 수 없는 입장이기에 본인이 복잡해진 것.`

### Connection Establishment
<img width="339" alt="스크린샷 2021-10-23 오후 4 56 00" src="https://user-images.githubusercontent.com/64299475/138547945-b7c4b19a-9300-4eba-b515-5f46831ce667.png">

#### 연결 요청 절차 (두 개의 통신 링크)
* Client 가 Server로 메시지를 보냄으로써 `SYN (= 1)` 연결 요청한다.
* Server는 SYN에 대한 응답 `ACK`을 줌과 동시에 `SYN`을 보낸다.
* Client는 다시 Server의 SYN에 대한 응답 `ACK`을 준다.

> Simultaneous Open : 클라이언트 - 서버 두개의 통신링크 동시에 만들어지는 것  
> SYN Flooding Attack : 서버 포트 열고 대기하고 있을 때 SYN 엄청 많이 보내서 서비스 불능 상태로 만드는 것.  

#### 데이터 보내기 (Full-Duplex)
<img width="450" src="https://user-images.githubusercontent.com/64299475/138548179-dbb5ec1d-4cbf-4dff-9c0f-4f85688fe9d3.png">

* 8001번째 byte 데이터를 시작으로 보낸다. `8001~9000`
* 15001 : random number 유지
* ACK 셋팅
* ACK 10001 : `이제 10001부터 보내줘!`
* Pushing Data : 기다리지 말고 바로 보내달라고 요청하는 것
* Urgent Data : 받았는데 Urgent Bit로 셋팅 되어 있으면, 이것 먼저 본다.

#### Connection termination
<img width="450" src="https://user-images.githubusercontent.com/64299475/138548464-81bc9f30-faac-4f5b-b786-6f1c875f8b07.png">

* Client가 FIN 요청 했으나 Server는 FIN 안 하면 `Half Close` 상태가 된다.
* Server가 ACK 해도 본인은 계속 데이터 보낼 수 있다. 


### Flow control
#### Normal Operation

<img width="450" src="https://user-images.githubusercontent.com/64299475/138548844-5a5d0c8c-beb9-4344-b9f5-50c2cf56d485.png">

* ACK delaying Timer - 메시지가 여러개 올 수도 있으니 타이머 켜놓고 일정시간 만큼 기다린 뒤 ACK 전송하는 방법
* 장점 : 매번 응답을 주는 것보다 효율이 올라간다.
* 단점 : 급할 때는 응답 바로바로하지 않으면, 상대방은 응답 기다려야 하므로 오히려 효율이 떨어진다.

#### Lost Segment
<img width="617" alt="스크린샷 2021-10-23 오후 5 22 34" src="https://user-images.githubusercontent.com/64299475/138548872-1e5ef0b2-06cc-4d02-ba6b-3f4ae00fdd65.png">

* 701이 없어졌으면 ACK 로 다시 요청하면 된다.

#### Fast retransmission
<img width="450" src="https://user-images.githubusercontent.com/64299475/138548978-fe2095b9-b755-472c-940f-2ba42e847f57.png">

* 동일한 ACK 메시지가 3번 연속해서 오면 타이머 restart 하면서 바로 재전송하는 방법이다. 빠르게 에러 검출 및 복구를 하기 위함이다.

### Slow Start, Exponential increase

<img width="450" src="https://user-images.githubusercontent.com/64299475/138549172-3acfb5b3-a199-4b27-a36b-060e8b25acf0.png">

* 수신 버퍼와 상관이 없다.
* 클라이언트와 서버 사이에 많은 줄과 장치가 있다는 것을 예측할 수는 있으나 얼마나 많은지는 모른다. 따라서, 네트워크의 상태 정확히 알 수 없다. 
* 과부하를 주지 않기 위해, 처음에는 천천히 시작한다. (연결 설정 후, 첫 번째 데이터 보낼 때 적용) 즉, 하나의 segment만 보낸다.
	* congestion window : 1
* 시간이 지나 ACK를 받으면 , congestion window : 2
* ACK 2개 받으면, congestion window : 4, 8, 16…
* 2 제곱으로 개수를 올려보면서, 에러가 나는지 안나는지 보고 조절하는 방법이다.

### Congestion avoidance, additive increase
* 2제곱이 아닌, linear 하게 1씩 증가시키는 방법이다.

### Taho TCP
* Slow Start, Exponential increase +  Congestion avoidance, additive increase
* 2, 4, 8 로 가다가 에러가 나면, congestion window 다시 1로 떨어뜨린다. (threshold : 4)
* 2, 4 까지만 가고 그 이후로는 +1 씩 진행하는 방법이다.
* +1 하다가 떨어지면 max 값의 반에 해당하는 값을 threshold로 설정한다.
* Taho에 변형을 한 Reno TCP도 존재한다. 