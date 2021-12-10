# IO Systems
## I/O 하드웨어
* Input/Output
* Basic I/O Hardware
	* I/O Device
	* Port : SSD와 PC를 연결하기 위해서는 USB를 꽂는다. 디바이스들을 연결할 수 있는 접점을 Port라고 한다.  Port는 레지스터로 구성되어있다.
	* Bus : 전기적인 신호가 흐를 수 있는 전선
	* Device controller : 디바이스를 제어할 수 있는 별도의 물리적 장치 (보통 메인보드에 붙어있다, Host adaptor)
* Device Controller : Registers (상태를 유지할 수 있는 회로), 하나의 chip으로 이루어져 있다. (serial-port controller for mouse, keyboard) 규격화된 프로토콜을 따르고 있다.

## How does processor communicate with I/O?
### Techniques for Performing I/O 🥜🐿🔥
* Programming I/O
	* Programming I/O는 device로 부터 CPU가 데이터를 받아서 메모리에 넣는다. 
	* **Direct I/O instructions**
		* CPU가 직접 디바이스를 컨트롤 하는 것
	* **Memory Mapped I/O** 
		* CPU가 메모리처럼 사용하는 것
* **Direct Memory Access (DMA)**
	* 디바이스가 직접 메모리에서 읽어가는 방식이다.

### Direct I/O (Isolated I/O)
* Memory Mapped I/O와 Direct I/O의 가장 큰 차이점은 `virtual 메모리와 디바이스가 같은 주소 공간에 있느냐? 별도의 주소 공간을 따로 가지는가?` 이며,  별도의 주소공간을 가지는 것이 Direct I/O 다.
* 주소 공간을 부를 때는 메모리에 접근하는 것과는 다른 방식을 사용해야하므로 별도의 special I/O instructions가 필요하고 느려질 수 있다. 

### Memory Mapped I/O
* Virtual Space 상에서 일정 부분을 디바이스에 할당하는 것을 말한다. 이를 통해, CPU 입장에서 메모리에 있는 데이터 값을 쓰는 것과 디바이스의 레지스터의 어떤 값을 쓰는 것을 같은 명령어로 수행할 수 있게 되므로 빠르다.

## How do we know I/O device is ready?
* Polling
* Interrupt-driven I/O

### I/O Port Registers
* Status register
	* **busy-bit** : 바쁜지 나타내는 비트 (0, 1)
* **Control register** : 명령을 집어넣는 것
	* command-ready bit : 어떤 데이터를 보낼 때 디바이스는 아무때나 보낼 수 있는 것이 아니며, 쓰고 있을 때 보낼 수는 없다. 명령을 수행할 수 있을 때 1, 없을 때는 0으로 표시한다.
* Data-in register
* Data-out register

### Polling
* 물어보고 사용할 수 있으면 사용하는 방법이다.
* Busy bit : 1이면 사용하지 못하고 0이면 사용할 수 있다.
* command-ready bit : 1이면 명령을 수행해도 되고 0이면 수행하지 못 한다.
* Polling 은 구현이 매우 쉽다. 작은 데이터를 보낼 때는 속도가 빠르지만 디바이스를 사용할 수 없는 시간이 오래 되면 CPU가 낭비된다.

> 1. Busy bit을 보고, 1이면 나중에 다시 온다.   
> 2. 0이면 host가 data-out register에 보내고 싶은 데이터를 쓴다. 다 쓰면 command-ready bit을 1로 변경한다.   
> 3. busy-bit 또한 1로 변경하고, data-out 을 수행한다.  
> 4. 다 내보내면 busy-bit과 command-ready bit을 0으로 바꿔준다.  

### Interrupt-driven I/O
* 명령을 다 수행할 동안 CPU는 다른 일을 하는 방법이다.
* `명령을 다 수행했는지 어떻게 아는가?` : CPU에는 interrupt line이 있고 그 line에 신호를 보낸다. `interrupt-request line`
* interrupt vector : 각 interrupt에 대해서 실제 핀의 주소를 알 수 있는 벡터

> 1. read command를 날리고 그 동안 CPU는 다른 일을 하고 있는다.  
> 2. I/O가 끝나면 I/O request를 날리고, I/O request가 들어오면 interrupt handler가 일을 수행한다.  

### Interrupt Handling Example : Page Fault
* Virtual memory 의 특정 페이지에 접근하려 했지만 그 페이지가 메인메모리에 있는 것이 아닌 디스크에 있을 때 발생하는 오류다.
* 처리 루틴 
	* save state of process in running
	* moves the process to waiting queue (wait state)
	* disk 에 있는 페이지를 fetch, 재시작

### Interrupt Handling Example : System Call
* `printf`
* round robin 방식

## Lot’s of I/O data
### Programmed I/O
* CPU가 어떤 명령을 내려서 데이터를 입출력 하는 방식을 말한다.
* 명령을 수행하는 동안 계속해서 CPU가 관여를 해야 한다.

### Direct Memory Access (DMA) 🌈⚡️🔥
<img  width = "400" src  ="https://user-images.githubusercontent.com/64299475/145532276-2c3bfbee-cb4b-49ac-b4f1-ce7b709914e9.png">

* Bypasses
* CPU 없이 컨트롤러와 메모리가 직접적으로 데이터를 주고 받는 방식을 말한다.
	* 실제로는 중간 매개체가 아예 없는 것이 아닌, CPU가 하는 일 중, 메모리와 컨트롤러 사이에서 데이터를 주고 받을 수 있도록 하는 역할을 DMA로 분리해서 이를 실현한다.

> 1. CPU가 메모리를 디스크에 써야한다하면 DMA에 명령을 내린다. 명령을 다 수행할 때까지 CPU는 그 일에 관여하지 않는다.  
> 2. DMA는 데이터를 블록 단위로만 전송할 수 있다. disk controller는 DMA transfer를 준비하고, DMA controller는 DMA 를 준비한다.  
> 3. C--을 반복해서 C=0이 될 때까지 DMA가 byte를 보낸다.  
> 4. C=0이 되면 CPU에 interrupt를 보낸다.  


## Application I/O Interface
* Wide variety of peripherals (주변장치)
	* different speed, formats, amounts of data
	* `OS는 복잡하고 다른 이 장치들을 어떻게 처리할까?`

### Device Drivers
* OS는 User가 디바이스 종류에 상관없이 제너럴하게 사용할 수 있게 한다.
* Device Driver은 명령을 그 device에 맞게 번역하는 코드다.
* **장점**
	* hardware에 independent 하다.
	* developer의 일이 간단해진다.
	* benefits hardware manufacturers
* Device Driver layer : kernel에서 명령이 내려왔을 때 디바이스 드라이버 상에서 컨트롤러로 줄 때 번역을 해서 준다.
* OS 입장에서 봤을 때는, data 전송 방법에 따라서 디바이스를 나눌 수 있다.
	* **Character Device** : 한글자씩 읽고 쓰는 방식, 적은 양의 데이터
	* **Block Device** : Block 단위로 데이터를 읽고 쓰는 디바이스, 많은 양의 데이터
		* Memory-mapped file
		* Direct Memory Access (DMA)
	
### Network Device (Socket)
* 네트워크를 이용한 디바이스

### Kernel I/O Subsystem
* Scheduling : 데이터를 읽고 쓸 때 어떤 순서로 할 것인가?
* Buffering
	* Buffer : 데이터를 모아두는 공간
	* Buffer는 `2개의 프로토콜, 미디어의 처리 속도가 다를 때`, 그리고 `미디어(영화 등)의 패킷 순서에 상관없이 재배치해서 스트리밍 할 수 있어야 할 때` 필요하다.


