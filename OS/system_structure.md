# System Structure
* multitasking, interrupt, protection, system calls, process

## OS Service to User
* UI
	* CLI, GUI
* User program execution
* I/O operations
* File-system manipulation
* Communications
	* network control
* Error detection

## OS service to resource management
### Resource allocation
* Resource : 컴퓨팅을 하기 위해 필요한 모든 것
	* CPU, memory, storage, graphic card…
	* 시간적인 개념도 포함된다.

### Protection
* 보호 (내부적)

### Security
* 보안 (악의적 외부침입 방지)

## Basic Operations
### Primitive OS
<img width="343" alt="스크린샷 2021-10-21 오후 6 44 47" src="https://user-images.githubusercontent.com/64299475/138253471-6d113335-4fb2-4c7d-b4fb-ba1aacf7797d.png">

* Primitive : 가장 기본적인 동작에 대한 의미적 표현 요소
* 가정
	* System runs one program at a time
	*  No bad users or programs (often bad assumption)
* 문제 : Poor Utilization, 중간 중간에 CPU 노는 시간 많기때문에 resource 낭비

### Multitasking
<img width="396" alt="스크린샷 2021-10-21 오후 6 44 57" src="https://user-images.githubusercontent.com/64299475/138253458-5abecd16-885a-4615-8342-6396f4aaa9c7.png">

* Idea : 동시에 multiple jobs을 처리한다.
	* When one process blocks (waiting for disk, network, userinput, etc.) run another process.
* resource 그때그때 필요한 곳에 효율적으로 배분한다. I/O device 와 CPU 시간 공유
* CPU에 전달할 structure는 반드시 메모리에 있어야 한다.


## What does OS do?
* CPU는 오직 한 번에 하나의 프로세스만 지원한다.
* OS가 하는 일
	1. Process Management (Create/run/terminate processes)
	2. Memory Management
	3. I/O Management
	4. Protection
		* 어떻게 보호하느냐?

## Process Management ✔️
* 프로세스는 실행 중인 프로그램, 또는 OS에서 관리하는 작업의 단위이다.
* hw1.exe ⇒ 프로그램 (코드를 기계어로 번역한 것)
	* 실행하기 위해서는 메모리에 올라가야 CPU와 통신 가능하다.
	* 따라서 코드가 그대로 복사가 되고, 작업 공간까지 함께 할당이 된다.
* 공간까지 포함한 메모리의 구조를  `프로세스`라고 한다.

### Memory Management
* Memory : byte들의 집합
* CPU: 메모리의 명령을 읽고, 데이터를 읽어서 연산 수행을하고, 그 결과값 다시 메모리에 쓰는 것
* Multitasking:  메모리 자체에 프로세스가 여러 개 있는 것
* Virtual Memory Management: 메모리는 크기가 작기 때문에 프로세스 형태 그대로 디스크에 저장하기도 한다. (다시 쓸 때 그대로 복사하기 위해)
	
### File & Storage Management
* File 과 Disk (mass-storage) 다루는 것도 OS의 중요한 역할이다.

### I/O Subsystem
* Device Controller (in I/O Device)
	* 파일 입출력 시 밑에 파일이 어떤 disk 이든지 OS는 동일한 역할을 할 수 있도록 하는 소프트웨어
* Device Driver (in OS)
	* OS가 외부 장치 사용하기 위하여 각각의 디바이스를 컨트롤 할 수 있도록 하는 소프트웨어

### I/O Subsystem contd
* OS 는 어플리케이션에서 디바이스 직접 건드리지 못 하도록 중간에 막고 있다.
* 어플리케이션은 요청만 가능하다. (scanf…)

#### 데이터의 업데이트를 확인하는 방법
1. Polling
	* while문을 계속 돌면서 계속 체크하는 것.
	* 구현 쉽다는 장점
2. **Interrupt** (매우 중요한 역할!)
	* 들어오면 얘기해달라고 요청하는 것.
	* OS는 디바이스의 입력을 마냥 기다릴 수는 없다. - OS는 Interrupt를 컨트롤한다.
	* Interrupt 처리하는 부분 추가해줘야 한다는 단점

### What OSs Do for the exe?
1. Cmd 실행
2. 명령 번역, 명령 파싱
3. disk 에서 프로그램 위치정보 찾음 (File system 사용)
4. 프로그램 메모리로 복사 및 공간 확보
5. 프로세스 만듦
6. 출력

## Interrupt 🐢
* CPU와 I/O 디바이스 동시에 사용되는 일 잘 없다.
* 어떤 프로세스가 I/O device 사용할 때, CPU는 그동안 멈춰 있다. ⇒ 그동안 다른 일 하면 효율적이다.
1. Hardware Interrupt
	* 키보드에서 키를 누르거나 하면 Interrupt 발생시킴.
2. Software Interrupt
	* exception : 하면 안 되는 일 했을 때 (ex. 0으로 나누는 것)
	* **system calls** : 어플리케이션은 하고자 하는 것 요청한다. but OS가 제공하는 함수 실행하기 위해서는 OS에서 정의한 모드가 바뀌어야 한다.
* 따라서 Interrupt 가 발생하면 모든 일이 중단 되고 Interrupt handler 실행 된다.

### Interrupt handling
![99E6CE3A5B549FDE17](https://user-images.githubusercontent.com/64299475/138256514-2c78455c-d768-4c7e-85c3-1d836c7f1978.png)

* OS도 소프트웨어이기 때문에, 메모리 어딘가에는 OS 올라가 있다.
* 메모리에서 OS 영역과 사용자 영역을 분리시켜 놨다. (Protection)
* Interrupt 날아오면 다른 영역은 중지 되고 Kernel space 코드 실행 되어야 한다.
	* **Kernel space**: 컴퓨터 운영체제의 핵심으로 시스템의 모든 것을 완벽하게 제어한다. 메모리 중 유저영역을 제외한 부분을 뜻한다. system call을 통해 접근 가능.
	* **Interrupt vector**에 해당 interrupt 걸렸을 때 어떻게 처리해야 하는지 적혀 있음.
	* 이 코드를 Interrupt service routine이라고 함
	* 종료 후 원래 실행하던 코드 다시 실행
