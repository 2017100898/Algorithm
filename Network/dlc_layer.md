# DLC Layer (Data Link Control Layer)
## DLC Basic
* Physical Layer에서 에러 발생했을 때, 어떤 방식으로 검출하고 복구할 것인지?
* **에러 컨트롤 및 복구 문제 해결을 위함.**
* 메세지 흐름 속도 등을 조절한다.

### Framing
* 보내는 정보는 결국 형태를 갖춰야 한다. 
* Layer 3가 보낸 데이터에 추가적으로 Layer 2인 DLC가 넣어야할 데이터를 넣고, 필요시 사이즈를 자르는 행위들을 일컫는다.
* 보내고자 하는 데이터가 3계층으로부터 왔을 때, 에러검출 및 복구, 흐름제어를 하기 위해서 추가적으로 필요한 정보를 집어 넣는 것.

### A frame in a character-oriented protocol
* A에서 B로 보내는 정보를 byte / bit 중 어떤 걸로 처리할 것인지가 가장 큰 차이

<img width="441" src="https://user-images.githubusercontent.com/64299475/133818261-7393ab66-8d13-4615-be13-da923f8f97c6.png">

* physical layer 가 A-B를 연결하고 있을 때, 사용자가 유의미한 정보를 주고 받지 않아도, layer는 끊임없이 어떤 정보를 주고 받는다. A에서 1을 쏘고 B에서 1을 받아 해석하려면, 1이라는 값을 이해해야 한다.  하지만 오는 길에 왜곡(손실 / 저항)이 발생하기 때문에, 보내는 값과 받는 값이 다를 수 있다. 따라서, 얼마나 떨어졌을 때 값을 1로 판단할 것인지, 중간값(레퍼런스값)이 필요하다.
* 사용자가 정보를 받지 않더라도, Physical Layer끼리는 고유의 목표를 위해 뭔가를 주고 받고 있다.
* **이때, DLC가 뭔가를 쏜다.** 그러면 지금부터는 트레이닝을 위한 것이 아닌, 사용자가 전송한 것이므로,  정보에 **Flag** 패턴을 담는다.

### Byte Stuffing and Unstuffing
<img width="441" alt="스크린샷 2021-09-18 오전 12 59 09" src="https://user-images.githubusercontent.com/64299475/133818658-41c6560a-0d58-4821-9215-ac1b5eddde30.png">

1. 사용자가 보내는 데이터에 flag와 같은 패턴이 우연히 들어가게 될 수도 있다.
	* 패턴이 같은 데이터 앞에 특수코드 (ESC)를 붙여줌으로써 flag와 데이터를 구별 가능하다. 
2. 사용자가 보내는 데이터에 ESC가 우연히 들어가게 될 수도 있다.
	* ESC 앞에 ESC를 한 번 더 넣어서 특수코드가 아님을 알려준다.

### Bit Stuffing and Unstuffing
<img width="441" alt="스크린샷 2021-09-18 오전 1 04 55" src="https://user-images.githubusercontent.com/64299475/133819469-1b6bfb7b-ce2c-4642-808f-a80f8d05f019.png">

* 그림에서는 Flag가 01111110 일 때를 얘기한다.
* 이럴 때는 flag 패턴이 나오지 않게 하기 위해서, 데이터에 1이 5개가 등장하면 무조건 0을 하나 집어넣는다.

### Flow Control
* Receiving node 가 Sending node에게 피드백을 주는 것.

### Connection
* **Connection oriented**: 2계층부터는 Logical한 SW적인 작업이다. 이들은 **연결 설정, 연결 유지, 연결 해제**라는 과정을 꼭 포함하고 있어서 복잡하다.
* Connectionless:  상대방을 고려하지 않고, 보내고 싶을 때 보낸다. 설정, 유지, 흐름제어, 에러제어 등의 과정을 거치지 않는다고 볼 수 있다.
* 하지만 둘 다 데이터를 주고 받는다.

## Simple Protocol
* Flow control, Error control 하지 않고 송신단이 보내고 싶은 것이 있을 때 바로 전송을 하고 수신단은 잘 받는다.
* Data-link layer 위에 Network Layer가 존재한다. 
* Sending node의 network layer 가 보낼 것이 있을 때 data-link layer로 내리고 sending node data-link layer -> logical link -> receiving node의 data-link layer로 전송하고 network layer로 올린다.
* 자연계에서는 불가능.

### FSM for the simple protocol
#### 상태천이도 (STD)
* Packet came from network layer : 이벤트
* Make a frame and send it : 액션
* 그 다음 상태 -> Ready
* **Ready -> 이벤트 -> 액션 -> Ready**
* Start : 프로그램이 최초로 살아날 때의 시작 상태

### 사다리 그림 / Message Sequence Chart
* 장치들 간 (hw나 sw간) 메세지를 주고 받는 것을 **시간에 따라** 나타난 다이어그램.
* Netwrok -> Data-link : 시간차가 거의 없기에 일직선임.
* Data-link -> Data-link : 어느정도 시간이 걸림.

## Stop-and-Wait Protocol
* 에러가 났다는 것을 아는 경우
	1. 메시지가 말도 안 되게 왔을 때 (CRC)
	2. 수신자가 메시지를 아예 못 받았을 때
	
### 방법론
* data의 까만 부분 (CRC): Flag 등을 붙일 부분…
* code 값이 data를 기준으로 sending node의 data-link에서 계산이 된다.
* Receiving data는 code를 받아서 본인도 CRC 값 (code)을 계산해본다.
* 계산한 값을 상대방이 보낸 데이터와 비교해 본다. 같으면 잘 보존 되어서 왔다는 뜻.
* 잘 받았으면 Sending node에게 ACK code를 돌려준다. 잘 받았다는 뜻.

1. 보내고 ACK 올 때까지 기다린다. (stop - wait)
2. 제대로 ACK 오면 잘 보낸 것이고, ACK 안 오면 에러났다고 판단. 정해진 횟수만큼 재전송 한다.

### FSM for the stop-and-wait protocol

### Message Sequence Chart
<img width="414" alt="스크린샷 2021-09-23 오후 12 57 16" src="https://user-images.githubusercontent.com/64299475/134452946-727f2626-70fb-4d0e-aa74-c72eaa44eb6f.png">

1. Packet1
	* 파란색 타이머 : 타이머 스타트, Frame 전송
	* ACK receiving -> sending node로 전송, 타이머 멈춤
2. Packet2
	* Frame 중간에 날아감
	* sending node의 데이터링크는 타임아웃, 리스타트 (재전송)
	* 똑같은 Frame copy본 resent
3. Packet3
	* 잘 받았는데 ACK 없어짐.
	* 타이머 타임아웃, 리스타트 (재전송)
	* _문제는 receiving node 입장에서 2번 받음. network 레이어에 올라가면 안되는데 올라감. (duplicate)_
	* 개선 시도 됨.



### Message Sequence Chart 개선점
<img width="414" alt="스크린샷 2021-09-23 오후 1 05 00" src="https://user-images.githubusercontent.com/64299475/134453129-6b7f858f-241e-4857-94c2-7aeb9a94aed6.png">

* 주고 받는 Frame에 번호를 달기 시작함
	* 처음에는 0, 두번째 패킷 1
* 첫 번째 패킷을 Frame0로 보냈을 때 이것을 잘 받은 receiving node는 ACK1 보냄. _(1번 Frame 달라는 뜻)_
* **번호는 0 아니면 1로도 충분**



### Piggybacking
* 보내는 쪽이 Frame 보내고 받는 쪽 ACK 보냄.
* 즉, ACK 메시지 별도로 존재함. 또한, 대부분의 통신시스템은 **송수신 둘 다** 함.
* **받는 쪽에서 보내는 쪽으로 다시 보낼 데이터 있으면 ACK 따로 보내지 않고 Frame 메시지에 구겨서 함께 보냄.** 메시지의 개수 매우 중요함.

## Go-Back-N Protocol
<img width="487" alt="스크린샷 2021-09-23 오후 1 25 21" src="https://user-images.githubusercontent.com/64299475/134454455-85fd9b25-ddb5-4266-8bb8-151cb1b41185.png">

* Stop-and-wait 의 문제점 : 보내는 데이터가 많아질 수록 전송 시간 오래 걸리고 통신링크의 효율 떨어짐.
* 통신 링크가 놀고있는 시간 제대로 활용해 봐야함.
* **기다리는 것이 아닌, 보내는 쪽에서 미리 정한 숫자만큼의 메시지를 ACK 없더라도 일단 보냄.** 
* **S(size) - send window size** : 상대방으로부터 ACK 없어도 보낼 수 있는 메시지의 range (사진 상의 회색부분, 15개, **2^m - 1**)
* **S(f)** : 메시지 보냈으나 ACK 안 온 첫번째 메시지 가리킴 (주황색 : 응답안와서 ACK 기다리고 있는 것들)
* **S(n)** : 다음에 보낼 메시지 가리킴
* Circular Ring : Ring 형태의 순환 구조

![다운로드 (1)](https://user-images.githubusercontent.com/64299475/134455602-9849bb59-fd6d-4e6c-b64c-b315c5ffd86d.png)

> **왜 2^m-1 ?**  
> 2^m 쓰면 receiver의 ACK sender에 하나도 도착하지 않아도,   
> **다시 보낸 Frame0가 이전것인지 새로운 것인지 구별하지 못 한다.**  


### Message Sequence Chart for Go-Back-N Protocol
<img width="487" alt="스크린샷 2021-09-23 오후 1 48 10" src="https://user-images.githubusercontent.com/64299475/134455960-26a4216a-ec2f-4d24-b1db-7ea8effb27a7.png">

* 수신단은 버퍼 1개만 가짐.
* ACK2 Lost 되어도 3, 4 받았으면 괜찮음.
* 하지만 Frame1 Lost 되었으면 Reciever는 뒤에 것 받았어도 no-action.
* 따라서 Sender는 Frame1부터 다시 전송.

## Selective Repeat Protocol
* Go-Back-N 문제점 : Frame 2, 3번이 성공적으로 도착했어도 1번이 도착하지 못했으면 모두 재전송해야함. 모두 버리지 말고 잘 살려볼 방법은?
* 선택적으로 Error 난 것들에 대해서만 재전송 하겠다!
* Go-Back-N과의 차이점
	1. 수신단의 버퍼 커졌다.
	2. ACK message 위에 NAK 생김. (못받았음을 말하는 메세지)

### Sender
![Selective Repeat Automatic Repeat Request_send window](https://user-images.githubusercontent.com/64299475/134456546-f13d6617-748e-4578-b0ea-5f0bd3a64a41.jpeg)

* S(size) - Window size : **2^(m-1)**

### Receiver
![Selective Repeat Automatic Repeat Request_receive window](https://user-images.githubusercontent.com/64299475/134456544-118052f0-b2d7-48c8-bb55-c09a4f8cc4d3.jpeg)
* 수신단이 버퍼 여러 개 가질 수 있음.
* R(n) : 받아야할 다음 프레임
* 빨간 색 : 이미 받았다!
* 에러가 나면 비우고 잘 받았으면 채운다.
*  R(size) - Window size : **2^(m-1)**

###  Message Sequence Chart for Selective Repeat Protocol
![Figure+Flow+diagram+for+Selective+Repeat+ARQ](https://user-images.githubusercontent.com/64299475/134456927-9e214ade-7dce-4eec-bde1-3c81bd430150.jpeg)
* Sender가 NAK 받으면 1번만 선택적으로 재전송.
* ACK4 : 이제 4번부터 주면 됨!

## DLC Example - HDLC
### HDLC (High level Data Link Control)
* High-level : MAC 위에서 동작하는 것
* 전화선을 이용한 데이터 통신 (ATM, 소규모 매장의 신용카드, FAX…)

<img width="482" alt="스크린샷 2021-09-23 오후 2 14 54" src="https://user-images.githubusercontent.com/64299475/134457698-fefeab62-695f-4073-99a1-966ddbf4d5d3.png">

* **I-frame** : 주로 데이터 주고 받는 용도
* **S-frame** : 데이터 주고 받지 않지만 ACK 보내야할 때 사용
* **U-frame** : 통신링크 유지 관리 하는 사람 입장에서 필요한 정보 전송

### Piggybacking  (추가 공부 필요)
![slide5-l](https://user-images.githubusercontent.com/64299475/134458389-7cf47cdd-1c40-4543-b44e-5740c955cafc.jpeg)
* 분홍색박스 앞에 있는 것 : Sending
* 뒤에 있는 것: Receiving ACK

1. 0, 0 : Frame0 , ACK 0
2. 1, 0 : Frame1, ACK 0
3. 0, 2 :  Frame0, ACK2 (잘 받았으니 이제 2 보내줘)
4. 1, 2 : Frame1,  ACK2 (잘 받았으니 이제 2 보내줘)
5. 2, 2 : Frame2, ACK2 (잘 받았으니 이제 2 보내줘 - 끝)
6. 정상 동작

![image-91](https://user-images.githubusercontent.com/64299475/134458384-f1781a3c-47fa-4a84-958e-9fe9037bf5db.jpeg)

## DLC Example - PPP
### PPP (Point-to-Point Protocol)
* 휴대폰의 기본 매커니즘. 3계층 이상의 어플리케이션에 대한 것을 설정하고 유지관리하기 위함.
* 이 사용자가 합법적인지, 얼마만큼의 지원받으면 되는지 등의 관리 기능 갖고 있음.

### Frame format
![unnamed](https://user-images.githubusercontent.com/64299475/134458825-b7785a0c-21af-453d-bd00-0fc52d444420.gif)

* Dead 상태에서 PPP 동작하면 연결 작업 시작.
* 서로 요청하고자 하는 것을 맞춰나감. 옵션 맞으면 Authenticate(인증)단계 들어감. - 적합한지, 불법인지?
* 합법적인 사용자 아니면 다시 Dead
* 합법적인 사용자면 Network 단계로 들어감. (3계층 이상에서 잘 돌아가도록 config 잡아줌)

### Multiplexing in PPP
![forouzan-ppp-6-638](https://user-images.githubusercontent.com/64299475/134459425-a9fdbf00-455f-43b4-8db5-5f3a385eaf63.jpeg)
* Data-link layer 안에 CHAP, PAP, IPCP,… 존재.
* 내가 인증을 해야 한다? AP 써야 함. -> CHAP, PAP 중 내가 사용할 것의 코드 씀.
* 상위계층의 애들 실어 나르는 역할.
