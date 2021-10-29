# DLC Layer (Data Link Control Layer)
<img width="300" src="https://user-images.githubusercontent.com/64299475/138284596-cbbe1b42-251b-42a2-800c-9d9332e3c9c0.png">

## DLC Basic
* [MAC subLayer](https://github.com/2017100898/TIL/blob/main/Network/mac_layer.md) : **공유매체에 여러 단말기가 접속할 때 에러 및 충돌**을 방지하기 위한 제어를 수행한다.
* DLC subLayer : **Physical Layer에서 에러 발생했을 때, 어떤 방식으로 검출하고 복구할 것인지**를 결정한다.
* **에러 컨트롤 및 복구 문제 해결을 위한 Layer다.**
* flow control & error control

### Framing
* 보내는 정보는 결국 *형태*를 갖춰야 한다. 
* Framing이란 Layer 3 ([Network Layer]((https://github.com/2017100898/TIL/blob/main/Network/network_1.md)))가 보낸 데이터에 추가적으로 Layer 2(DLC)가 넣어야할 데이터를 넣고, 필요시 사이즈를 자르는 행위들을 일컫는다.
* 따라서 보내고자 하는 데이터가 Layer 3 으로부터 왔을 때, 에러검출 및 복구, 흐름제어를 하기 위해서 추가적으로 필요한 정보를 집어 넣는 것을 뜻한다.

### A frame in a character-oriented protocol
* 문자 지향 프로토콜(character-oriented protocol)에서 전송되는 데이터는 ASCII와 같은 8비트 문자다.
* A에서 B로 보내는 정보를 **byte / bit 중 어떤 걸로 처리할 것인지가 가장 큰 차이**를 나타낸다.
* 한 프레임을 다음 프레임에서 분리하기 위해 프레임의 **시작과 끝에 8비트(1바이트) 플래그가 추가**된다.

<img width="441" src="https://user-images.githubusercontent.com/64299475/133818261-7393ab66-8d13-4615-be13-da923f8f97c6.png">

* physical layer 가 A-B를 연결하고 있을 때, 사용자가 유의미한 정보를 주고 받지 않아도, Physical Layer끼리는 training (왜곡, 변형 등의 상황에서의 값 파악)을 위해 끊임없이 무언가를 주고 받고 있다. 
* 하지만 **이때, DLC가 전송한다면 지금부터는 트레이닝을 위한 것이 아닌 사용자가 전송한 것이므로,**  정보에 **Flag** 패턴을 담는다.

### Byte Stuffing and Unstuffing
<img width="441" alt="스크린샷 2021-09-18 오전 12 59 09" src="https://user-images.githubusercontent.com/64299475/133818658-41c6560a-0d58-4821-9215-ac1b5eddde30.png">

#### Stuffing
1. 사용자가 보내는 데이터에 flag와 같은 패턴이 우연히 들어가게 될 수도 있다.
	* 패턴이 같은 데이터 앞에 특수코드 (ESC)를 붙여줌으로써 flag와 데이터를 구별 가능하다. 
2. 사용자가 보내는 데이터에 ESC가 우연히 들어가게 될 수도 있다.
	* ESC 앞에 ESC를 한 번 더 넣어서 특수코드가 아님을 알려준다.

#### Unstuffing
* Frame 수신하면 다시 ESC를 Unstuffing 하여 원래 데이터를 복원한다.

### Bit Stuffing and Unstuffing
<img width="441" alt="스크린샷 2021-09-18 오전 1 04 55" src="https://user-images.githubusercontent.com/64299475/133819469-1b6bfb7b-ce2c-4642-808f-a80f8d05f019.png">

#### Stuffing
* 그림에서는 Flag가 01111110 일 때를 얘기한다.
* 이럴 때는 flag 패턴이 나오지 않게 하기 위해서, 데이터에 1이 5개가 등장하면 무조건 0을 하나 집어넣는다.

#### Unstuffing
* Frame 수신하면 다시 0을 Unstuffing 하여 원래 데이터를 복원한다.

### Flow Control (흐름제어)
![img-7](https://user-images.githubusercontent.com/64299475/138421024-b81312b0-a409-4756-a813-31aa991bf109.png)

* Flow Control는 서로 다른 속도로 작동하는 Receiver와 Sender가 통신할 수 있도록 하는 기술이다.
* Receiving node 가 데이터 잘 받았으면 Sending node에게 피드백을 줌으로써 Sending node가 데이터 받았음을 파악할 수 있다.

### Connection
* **Connection oriented**: 2계층부터는 Logical한 SW적인 작업이다. 이들은 **연결 설정, 연결 유지, 연결 해제**라는 과정을 꼭 포함하고 있어서 복잡하다.
* Connectionless:  상대방을 고려하지 않고, 보내고 싶을 때 보낸다. 설정, 유지, 흐름제어, 에러제어 등의 과정을 거치지 않는다고 볼 수 있다.
* 하지만 둘 다 데이터를 주고 받는다.

## Simple Protocol
<img height="250" src="https://user-images.githubusercontent.com/64299475/138452379-5c528228-67c7-477f-ab52-80c81a137883.jpeg">



* Sending node와 Receiving node는 Network Layer와 Data-link Layer로 이루어져 있다. 
* Sending node의 network layer가 보낼 것이 있을 때, Data-link Layer에 내리고 (패킷 전달), Sending node의 Data-link Layer는 Framing 후, logical 한 링크를 통해 Receiving node에 전송한다. 
* Receiving node는 Unframing 후, 데이터를 Network Layer로 올린다. Sending node Data-link에서 Receving node의 Data-Layer에 Frame을 전달할 때는 약간의 시간이 걸린다.
* Flow control, Error control 하지 않고 송신단이 보내고 싶은 것이 있을 때 바로 전송을 하고 수신단은 잘 받는다.
* 이는 자연계에서는 불가능하다.

### FSM for the simple protocol
#### 상태천이도 (STD)
<img height="250" src="https://user-images.githubusercontent.com/64299475/138886723-6eaf465a-8cba-4020-badc-dae6bbdfc5d1.png">



* 위 상태천이도에서의 Ready는 기다리는 상태임을 나타낸다.
* Packet came from network layer는 이벤트, Make a frame and send it을 액션이며, 이벤트와 같은 상태가 되면 액션을 수행하면 된다. 액션 수행 후 상태는 다시 Ready다.
* **Ready ⇒ 이벤트 ⇒ 액션 ⇒ Ready**
* Start는 프로그램이 최초로 살아날 때의 시작 상태를 말한다.

### 사다리 그림 / Message Sequence Chart
<img width="387" alt="스크린샷 2021-10-22 오후 9 22 45" src="https://user-images.githubusercontent.com/64299475/138452892-0637038a-716b-449c-86dd-8990aa0b1b4a.png">

* Message Sequence Chart는 **장치들 간 (hw나 sw간) 메세지를 주고 받는 것을 시간에 따라 나타낸 다이어그램**이다.
* Network ⇒ Data-link : 시간 차가 거의 없기에 일직선이다.
* Data-link ⇒ Data-link : 어느정도 시간이 걸린다.

## Stop-and-Wait Protocol
<img height="300" src="https://user-images.githubusercontent.com/64299475/138453054-441c19f7-7304-4baf-adf7-a3358cd0a10a.jpg">

<img height="300" src="https://user-images.githubusercontent.com/64299475/138453327-af6b2b64-8128-4048-becf-a7411837df94.png">


* 에러가 났다는 것을 아는 경우
	1. 메시지가 말도 안 되게 변형되어 왔을 때 (CRC)
	2. 수신자가 메시지를 아예 못 받았을 때
	
### 방법론
<img height="200" src="https://user-images.githubusercontent.com/64299475/138453674-50e66655-4448-4102-9262-22981be9dfcc.png">

* data의 까만 부분 (CRC)은 Flag 등을 붙일 부분이다.
* code 값이 data를 기준으로 sending node의 data-link에서 계산이 된다.
* Receiving data는 code를 받아서 본인도 CRC 값 (code)을 계산해본다.
* 계산한 값을 상대방이 보낸 데이터와 비교해 본다. 같으면 잘 보존 되어서 왔다는 뜻. `네가 보낸 값 이거 맞아?`
* 메시지를 잘 받았으면 Sending node에게 ACK code를 돌려준다.

1. 보내고 ACK 올 때까지 기다린다. (stop - wait)
2. 제대로 ACK 오면 잘 보낸 것이고, ACK 안 오면 에러났다고 판단하며, 정해진 횟수만큼 재전송 한다.

### FSM for the stop-and-wait protocol

### Message Sequence Chart
<img width="414" alt="스크린샷 2021-09-23 오후 12 57 16" src="https://user-images.githubusercontent.com/64299475/134452946-727f2626-70fb-4d0e-aa74-c72eaa44eb6f.png">

1. Packet1
	* 파란색 타이머는 타이머를 스타트 하고 Frame 전송하는 것을 나타낸다.
	* ACK을 receiving ⇒ sending node로 전송하고, ACK을 잘 받으면 타이머 멈춘다.
2. Packet2
	* Frame 중간에 날아간 상황이다.
	* Sending node의 데이터 링크는 타임아웃되었으며, 리스타트 후 재전송한다.
	* 이전과 똑같은 Frame copy본을 보낸다.
3. Packet3
	* 메시지를 잘 받았는데 ACK이 없어진 상황이다. 타이머는 타임아웃 및 리스타트 되었으므로 메시지를 재전송한다.
	* 여기서_**문제는 receiving node 입장에서 메시지를 2번 받았다는 것이다. network 레이어에 올라가면 안되는데 . duplicate하게 올라갔다.**_
	* 이러한 문제점때문이 개선이 시도 되었다.



### Message Sequence Chart 개선점
<img width="414" alt="스크린샷 2021-09-23 오후 1 05 00" src="https://user-images.githubusercontent.com/64299475/134453129-6b7f858f-241e-4857-94c2-7aeb9a94aed6.png">

* 앞서 말한 Duplicate  문제를 해결하기 위해 **주고 받는 Frame에 번호를 달기 시작한다.**
	* 처음에는 0, 두번째 패킷 1
	* 첫 번째 패킷을 Frame0로 보냈을 때 이것을 잘 받은 receiving node는 ACK1 보낸다. `1번 Frame 달라는 뜻이다.`
* **번호는 0 아니면 1로도 충분**하다.

### Piggybacking
* 일반적으로 보내는 쪽이 Frame 보내고 받는 쪽 ACK 보낸다.
* 즉, ACK 메시지 별도로 존재한다는 뜻이다. 또한, 대부분의 통신시스템은 **송수신 둘 다** 한다.
* **받는 쪽에서 보내는 쪽으로 다시 보낼 데이터 있으면 ACK 따로 보내지 않고 Frame 메시지에 구겨서 함께 보낸다.** *메시지의 개수 매우 중요하다.*

## Go-Back-N Protocol
<img width="487" alt="스크린샷 2021-09-23 오후 1 25 21" src="https://user-images.githubusercontent.com/64299475/134454455-85fd9b25-ddb5-4266-8bb8-151cb1b41185.png">

* Stop-and-wait의 문제점은 보내는 데이터가 많아질 수록 전송 시간이 오래 걸리고 통신링크의 *효율이 떨어진다*는 것이다.
* 통신 링크가 놀고있는 시간 제대로 활용해 봐야한다. 무작정 **기다리는 것이 아닌 ACK가 없더라도 보내는 쪽에서 미리 정한 숫자만큼의 메시지를 일단 보낸다.** 
* **S(size), 즉 send window size** 는 상대방으로부터 ACK 없어도 보낼 수 있는 메시지의 range를 말한다. 사진 상의 회색부분으로, 15개를 가리킨다. `2^m - 1`
* **S(f)**는 메시지 보냈으나 ACK 안 온 첫번째 메시지 가리키며, 위 사진에서의 주황색은 응답이 안와서 ACK 기다리고 있는 것들을 나타낸다.
* **S(n)**는 다음에 보낼 메시지 가리킨다.
* Circular Ring : Ring 형태의 순환 구조

<img height="300" src="https://user-images.githubusercontent.com/64299475/134455602-9849bb59-fd6d-4e6c-b64c-b315c5ffd86d.png">



> **왜 2^m-1인가?**  
> 2^m 쓰면 receiver의 ACK sender에 하나도 도착하지 않아도,   
> **다시 보낸 Frame0가 이전것인지 새로운 것인지 구별하지 못 한다.**  


### Message Sequence Chart for Go-Back-N Protocol
<img width="450" src="https://user-images.githubusercontent.com/64299475/134455960-26a4216a-ec2f-4d24-b1db-7ea8effb27a7.png">

* Go-Back-N Protocol에서 수신단은 버퍼 1개만 가진다.
* ACK2 Lost 되어도 3, 4를 받았으면 괜찮다.
* 하지만 Frame1 Lost 되었으면 Reciever는 뒤에 것을 받았어도 action을 취하지 않는다.
* 따라서 Sender는 Frame1부터 다시 전송한다.

## Selective Repeat Protocol
* Go-Back-N 문제점은 **Frame 2, 3번이 성공적으로 도착했어도 1번이 도착하지 못했으면 모두 재전송 해야 한다** 는 것이다.
* 모두 버리지 말고 잘 살려볼 방법은? `선택적으로 Error 난 것들에 대해서만 재전송 하는 것!`
* Go-Back-N과의 차이점
	1. 수신단의 버퍼 커졌다.
	2. ACK message 위에 못받았음을 말하는 메세지인 NAK가 생겼다.

### Sender
<img width="450" src="https://user-images.githubusercontent.com/64299475/134456546-f13d6617-748e-4578-b0ea-5f0bd3a64a41.jpeg">

* S(size), Window size : **2^(m-1)**

### Receiver
<img width="450" src="https://user-images.githubusercontent.com/64299475/134456544-118052f0-b2d7-48c8-bb55-c09a4f8cc4d3.jpeg">

* Selective Repeat Protocol에서는 수신단이 여러 개의 버퍼를 가질 수 있다.
* R(n)은 받아야할 다음 프레임을, 사진 상에서의 빨간 색은 이미 받은 프레임을 나타낸다.
* 에러가 나면 비우고 잘 받았으면 채우는 형식이다.
*  R(size), Window size : **2^(m-1)**

###  Message Sequence Chart for Selective Repeat Protocol
<img width="482" src="https://user-images.githubusercontent.com/64299475/134456927-9e214ade-7dce-4eec-bde1-3c81bd430150.jpeg">

* Sender가 NAK 받으면 1번만 선택적으로 재전송한다.
* ACK4 : `이제 4번부터 주면 된다!`

## DLC Example - HDLC
### HDLC (High level Data Link Control)
* Stop-and-Wait protocol을 사용하는 비트 지향 프로토콜이다.
* 전화선을 이용한 데이터 통신 (ATM, 소규모 매장의 신용카드, FAX…)

<img width="400" src="https://user-images.githubusercontent.com/64299475/134457698-fefeab62-695f-4073-99a1-966ddbf4d5d3.png">

* **I-frame** : 주로 데이터 주고 받는 용도로, 데이터에 대한 확인 보낼 때 사용한다.
	* control 0으로 시작하는 Frame
* **S-frame** : 데이터 주고 받지 않지만 ACK 보내야할 때 사용하며, 흐름제어를 한다.
	* control 10으로 시작하는 Frame
* **U-frame** : 통신링크 유지 관리 하는 사람 입장에서 필요한 정보 전송하고, 설정 및 관리 역할을 한다.
	* control 11로 시작하는 Frame


### Piggybacking 
<img width="480" src="https://user-images.githubusercontent.com/64299475/134458389-7cf47cdd-1c40-4543-b44e-5740c955cafc.jpeg">





* 분홍색박스 앞에 있는 것은 Sending을 나타내고 뒤에 있는 것은 Receiving ACK이다.

  1. 0, 0 : Frame0 , ACK 0

  2. 1, 0 : Frame1, ACK 0

  3. 0, 2 :  Frame0, ACK2 `잘 받았으니 이제 2 보내줘`

  4. 1, 2 : Frame1,  ACK2 `잘 받았으니 이제 2 보내줘`

  5. 2, 2 : Frame2, ACK2 `잘 받았으니 이제 2 보내줘 - 끝`

  6. 정상 동작

     

<img width="480" src="https://user-images.githubusercontent.com/64299475/134458384-f1781a3c-47fa-4a84-958e-9fe9037bf5db.jpeg">



## DLC Example - PPP
### PPP (Point-to-Point Protocol)
* Connection-oriented
* 휴대폰의 기본 매커니즘이다. 3계층 이상의 어플리케이션에 대한 것을 설정하고 유지관리한다.
* 이 사용자가 합법적인지, 얼마만큼의 지원받으면 되는지 등의 관리 기능 갖고 있다. (인증)

### Frame format
<img width="480" src="https://user-images.githubusercontent.com/64299475/134458825-b7785a0c-21af-453d-bd00-0fc52d444420.gif">



* Dead 상태에서 PPP 동작하면 연결 작업을 시작한다.
* 서로 요청하고자 하는 것을 맞춰나가고 옵션 맞으면 Authenticate(인증) 단계 들어간다.
* 합법적인 사용자인지 판단한 후 만약 아니라면 다시 Dead한다.
* 합법적인 사용자면 Network 단계로 들어간다. 3계층 이상에서 잘 돌아가도록 config 잡아준다.

### Multiplexing in PPP
<img width="480" src="https://user-images.githubusercontent.com/64299475/134459425-a9fdbf00-455f-43b4-8db5-5f3a385eaf63.jpeg">

* Data-link layer 안에 CHAP, PAP, IPCP등 다양한 보안 인증 방법이 존재한다.
* 내가 인증을 해야 한다면 AP를 써야 한다. CHAP, PAP 중 내가 사용할 것의 코드를 쓰면 된다.