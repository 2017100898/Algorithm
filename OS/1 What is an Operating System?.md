# What is an Operating System?
* 운영체제는 컴퓨터를 계속 운영하기 위해서 고안된 시스템이다.
* 운영체제는 100% **소프트웨어**다.
* 윈도우를 제외한 대부분의 운영체제는 UNIX를 기반으로 한다.

### OS 종류
* UNIX, Android, iOS, Window, DOS, Linux...
* Real-Time OS : VxWorks, pSOS

### 컴퓨터와 User
* 웨어러블, 로봇, 태블릿, 차,... 등 모든 것이 컴퓨터다.
* 유저란 사람 뿐만 아니라 컴퓨터를 사용하는 모든 것이다.


### Simple Concept

<img width="226" alt="스크린샷 2021-09-06 오후 1 45 15" src="https://user-images.githubusercontent.com/64299475/132226087-a842a843-ed09-43e3-b834-c348ed667fdc.png">


* Developer: 여러 디바이스에서 사용 가능한 어플리케이션을 만들고 싶다.
* User: 여러 디바이스에서 동시에 사용하고 싶다.
* Application: 여러 명이 동시에 접속해서 사용했으면 좋겠다.
* 결국에는 전자회로를 구동하기 위해 코딩을 하는 것이다.
* 전자 장치를 제어하는 일은 매우 어렵다! 고로 우리는 OS의 API들을 사용한다.

### OS의 목표
* 하드웨어를 제어하고 어플리케이션을 만들 수 있게 환경을 제공한다.
* 사용자가 하드웨어와 소통할 수 있도록 중간자 역할을 한다.
* **OS는 효율성을 위한 프로그램이다.**

### OS의 역할
1. **Abstraction**
	1. 개발자가 하드웨어에 관계 없이 develop 할 수 있게 해 준다.
		* 조건1: 운영체제가 제공하는 기능만 이용해서 어플리케이션 개발 가능
		* 조건2: 운영체제가 시키는 대로만 가능 (프로그램 제어권 가짐)
2. **Managing**
	1. 하드웨어의 복잡함을 해결시켜주고 여러 어플리케이션의 충돌을 막아준다.
