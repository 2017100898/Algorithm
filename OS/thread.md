# Thread
* [프로세스 (Process)](https://github.com/2017100898/TIL/blob/main/OS/process.md)의 단점을 해결하기 위해 Thread가 도입 되었다.
* **메모리 안에서 실제로 실행되고 있는 단위**
	* Process 안에서 작업들을 여러 개의 Thread로 나눠서 개별적으로 수행한다고 볼 수 있다.

## Process
* **공간적으로 메모리에 할당된 작업 공간**
* SSD에 들어있는 코드를 실행하면 DRAM에 올라가고 메모리 상에 공간을 할당 받는다. 또한 이것을 관리하기 위해서 PCB 구조체가 Kernel 메모리에 생성 된다.
* CPU 할당 - I/O device 효율적으로 하기 위해서 state 존재.
* OS는 각각의 프로세스의 state 바꿔가면서 최대한 자원을 효율적으로 사용하고, 모든 프로세스들이 가장 빠른 시간 안에 처리할 수 있도록 스케쥴링 한다.
* 프로세스는 다른 프로세스의 공간들을 침범할 수 없다. 공간 따로 할당 받거나 Kernel에게 메시지를 준다.


### Single Threaded Process
### Multi Threaded Process
<img width="379" alt="스크린샷 2021-10-21 오후 7 35 52" src="https://user-images.githubusercontent.com/64299475/138261310-c931166b-0666-4b08-b8c2-b61344702b28.png">


* code, data, file 공유하고 registers, stack, Progam Counter 개별적으로 존재한다.
* **Resource Sharing** : IPC(OS 허락) 보다 공유가 쉽다.
* **Lighter Weight Process** : creation, deletion 빠르다. 메모리 복사 시간 필요 X
	* **Context-switching** faster than process-switching : CPU가 현재 사용하고 있는 register 값들 밖으로 내보내고 다른 작업의 context 다시 CPU에 올리는 것.
	* Process switching : cache flush까지 포함되기 때문에 느림

## Thread를 왜 사용하는가? 🤷‍♀️
* 하나의 프로세스가 다른 프로세스를 만들어내기 위해서 Fork 를 한다.
	* fork : memory 복사 (OS.kenrel)
	*  서로 다른 프로세스이기 때문에 **데이터 공유 불가**
		* 데이터 공유를 위해 IPC 이용
* 비슷한 기능을 하는 프로세스들이 있을 때, 과연 전체 메모리를 다 복사해야 되는가? 그렇게 하지 않는 방법은? 
	* stack, heap, data, text 중
		* **stack** 반드시 개별적으로 구현 필요
		* heap 공유 가능
		* data 공유 가능
		* text 공유 가능
	* **Program Counter** (PC, 현재 프로그램이 실행되고 있는 위치) 별도 필요
* 하드웨어 발달함에 따라 **프로세스 자체의 단점**들이 부각 됨.
	* 각각의 Process는 각각의 PCB를 갖고 있어야 하고, **새로운 프로세스를 만드는 일이 매우 비싸다.** (많은 resource - hardware, time)
	* Process들은 자신의 주소를 모른다. 
	* 병렬적으로 실행할 때 같은 메모리를 사용하고 싶어도 잘 안 된다. 그럴 때마다 IPC 사용하면 부가적인 시간 필요하다.

### What can we do?
* Share 가능
	* Same Code 
	* Same Data
* Share 불가
	* CPU registers
	* stack
	* Program Counter

## Thread Control Block(TCB)
<img width="233" alt="스크린샷 2021-10-21 오후 7 42 48" src="https://user-images.githubusercontent.com/64299475/138262275-bb93adfc-010d-46fe-8aab-a39e51702390.png">

* **PCB 안에 TCB들이 연결되어 있다.**
	* Process 안에 Thread 있기 때문.
	* 요즘에는 TCB들을 ready queue 안에 넣는다.

## Benefits of Multithread
* Process는 반드시 하나의 CPU 만을 사용했으나, Thread가 여러 개 있으면 **Thread 별로 다른 CPU를 할당**받아 사용할 수 있다.
* 개별적인 CPU 할당 받아서 **실제로 Parallel 하게 작업 수행할 수 있게 됨.**

### Non-blocking system call
* 일부의 Thread가 block 되더라도 나머지 CPU 계속해서 사용 가능하기 때문에 더욱 효율적이다. 
* Better Responsiveness to the user

### Example
* Web server
	* (일반적으로) Client 요청 - Server 응답
	* Client 요청할 때마다 프로세스 복제해서 응답하는 것 너무 비효율적이다.
	* Multithreaded 를 통해 해결할 수 있음.


## Multicore Programming
* Concurrent 은 illusion을 뜻하고, 각각이 개별적으로 빠른 시간안에 반복적으로 수행된다. (Single-core : 하나의 Core는 하나의 작업 밖에 못 함)
* Parallel은 실제로 같은 시간 안에 동시에 수행되는 것 (Multi-core)

## Multithreading Models ✔️

### Kernel Thread

<img width="425" alt="os4-3" src="https://user-images.githubusercontent.com/64299475/138264230-261e9385-b047-467a-ad96-d895c75f743a.png">

* 실제로 OS에서 제공하는 기능의 Thread
* system call로 호출
* 각각의 TCB 갖고 있음
* **장점**
	* multi-core에서 수행될 수 있다.
	* Concurrency : blocking 당해도 다른 Thread 사용 가능
* **단점**
	* OS가 결국 관여를 해야하기 때문에 context switching 일어나고 CPU 빼앗기게 됨. (하지만 프로세스보다 훨씬 빠름)

### User Thread

<img width="414" alt="os4-2" src="https://user-images.githubusercontent.com/64299475/138264239-896574f1-26c6-4906-a776-fddf9cd5ec16.png">

* OS 관점에서는 하나의 Thread이지만 실제로 프로그램 내부에서는 시간 돌아가면서 쓰는 것.
* 최대한 효율적으로 Switching 해서 사용하겠다. - OS 관여 X
* **장점**
	* Kernel thread 보다 훨씬 빠르다
* **단점**
	* OS 관점에서는 Single-thread. 하나 block 되면 나머지들도 다 Block될 수 있음. 

## Thread Library
### POSIX
* UNIX 계열의 OS들이 따르는 표준 협약
* **pthreads** : creating, detaching, joining…

```c
int pthread_create(pthread_t *tid, const pthread_attr_t *attr, void *(*func)(void *), void *arg);
```

* **tid**: thread의 id가 들어갈 변수
* **attr**: User thread? Kernel thread?
* **func**: 어디 함수부터 시작할 것인지
* **arg**: 함수의 argument

#### fork & pthreads
* **fork**: 실행되는 순간 2개로 갈라져서 같이 실행
* **pthread_create**: func에서부터 시작, global variable 공유 됨.

## Synchronization
* 하지만 Thread가 memory를  공유하는 것때문에 문제가 발생할 수 있다. 
	* **어떤 Thread가 먼저 실행될지는 아무도 모른다.** 경우마다 다른데, 실행되는 순서마다 결과값이 달라질 수 있다.
* 이 문제를 해결할 수 있는 것이 [`synchronization (동기화)`](https://github.com/2017100898/TIL/blob/main/OS/synchronization.md)
* `pthread_join()` : 끝날 때까지 기다리는 것
