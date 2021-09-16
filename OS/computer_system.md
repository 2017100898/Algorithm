# Computer System
## Organization, Architecture
## 연산장치 vs 기억장치
### 폰노인만 구조
* 연산장치와 기억장치는 분리되어 있으며, 연산장치는 기억장치에서 데이터를 로딩해서 처리 후, 다시 기억장치로 가져다 놓는다.
* 하지만 사람은 연산 및 기억장치가 분리되어있지 않다.
* CPU와 Memory. 거의 대부분의 OS의 기능을 Memory 관리에 집중한다.

### System BUS
1. 두 Device 연결된 전선 (데이터 이동 통로)
2. 통신 규약 

### 연산장치
* 어떤 Input 들어왔을 때 Output 내준다.
* 병렬 처리
* CPU, Graphic card 

### 기억장치
* 일정한 기간동안 정보 유지하고 있다.
* Memory: DRAM, HDD, SSD (같은 기능을 한다.)
* 모든 메모리들이 정보 기억 및 저장하고, 내가 그 정보를 기억, 수정, 삭제 가능하다.

### CPU
* OS 관점에서 CPU는 신경쓰지 않아도 된다. 시키는 일만 처리를 한다. (like 자판기)

## 기억장치의 종류
### Memory
* 정보(프로그램과 데이터)를 담는다. Memory는 CPU에 정보를 전달해서 동작한다. 
* DRAM (Main memory): CPU에 명령과 데이터 직접 전달한다. 빠르다. 전원 꺼지면 정보 사라진다. 휘발성.
* SSD (Secondary) : CPU와 직접 만나지 못 한다. 비록 느리지만 전원이 꺼지더라도 정보 계속 남아있다. 비휘발성.
* disks (Secondary) : 요즘에는 많이 쓰지 않는다. 
* 정반대의 특성이 상호보완적이다.
* Booting : SSD내에 Windows가 SSD -> DRAM -> CPU 한 줄 한 줄 실행되는 것. But 처음 위치 알려주는 것 필요 (Bootstrap)

### DRAM
* Dynamic Random Access Memory
* DRAM : 어떤 정보를 저장하기 위해서는 계속 충전을 해줘야 한다. 속도가 SRAM에 비해 느리다.
* SRAM (Static) : 충전을 해 주지 않아도 저장 가능, 회로 더욱 복잡. 비용이 더 비싸다.

### Caching
* 자주 쓰는 데이터만 DRAM에 옮겨서 CPU와 Direct로 연결시켜 효율을 높이는 것이 Caching concept이다.

### Multi(core) Processor
* 여러 작업을 보다 효율적을 한 번에 처리하기 위해 2개 이상의 코어를 탑재하여 만든 프로세서
* 여러 개의 주 CPU 를 가진다.
* 장점
	* 성능 향상 (Increased throughput)
	* 규모의 경제 (Economy of scale) : 여러 컴퓨터를 사용하는 것보다 경제적이다.
	* 신뢰도 향상 (Increased reliability) : 작동 중 CPU 하나 멈춰도 작동하므로 안정적으로 사용할 수 있다.
* Type
	* Asymmetric Multiprocessing : 비대칭
	* Symmetric Multiprocessing : 대칭 - 주로 사용

## Below Your Program
### Bit
* Binary digit, 이진수의 하나의 자리수 (0,1)
* N개의 b로 나타낼 수 있는 정보의 수는?
* N bits : 2^N개의 정보를 나타낼 수 있다.

### ASCII
* 사람의 약속으로,  특정한 숫자를 한 문자에 할당한 것.
* 1byte로 나타낸다.

### Byte
* 8 bits = 1 byte 
* 데이터의 가장 작은 단위
* 메모리 주소의 가장 기본 단위

### Word
* 컴퓨터가 일을 하는 단위
* 1 word = 4 byte = 32 bit

## Memory
* 1110001110011101 : 8개 단위로 끊어서 저장, 2개의 방에 나뉘어서 저장 된다고 생각할 수 있다.
* 한 방에 8개의 bit, 즉 1 byte가 저장되어있다.
* 메모리는 지울 수 없다.

### Data Storage (Write)
* 메모리 셀의 개별 비트를 0 또는 1로 설정하고 이전 내용을 삭제한다.

### Data retrieval (Read)
* 다른 저장 지역에 대한 특정한 메모리 셀의 내용을 복사한다.

## SW 
### Application SW
* word processor, media player, web browser…
* 하드웨어가 없으면 아무동작 할 수 없다. 매개체는 OS다.

### System SW
* OS
* Compiler
	* High-level language (ex. C code) 를 assembly language (ex. add A, B)로 바꿔주는 것이다.
	* assembly language를 binary language (ex. 10010101)로 바꾸는 것은 **Assembler**이다. 
	
- - - -

## User Interface
### CLI 
* shell, 명령 프롬포트

### GUI 
* 사용자 친화적인 데스트탑 인터페이스
* Microsoft Windows는 CLI command shell이 포함된 GUI

## Computing Environments
### Stand-alone
* Personal Computer

### Network Computers
* 최근에는 Clouding으로 많이 사용 중

### Wireless Networks (무선통신)
* 모바일 컴퓨터는 무선 네트워크를 통해 서로 연결 된다.

### Distributed System
* Network을 통한 시스템 구축 및 작업의 분산

### Virtualization
* 운영체제를 다른 OS 내의 어플리케이션으로 실행할 수 있다.
* VMware, Virtual Box..

### Cloud Computing
* 인터넷을 통해 서버, 스토리지, 데이터베이스, 네트워킹, 소프트웨어 등의 컴퓨팅 서비스를 제공하는 것.
* Public, Private, Hybrid Cloud…
* SaaS, PaaS, IaaS

### RTOS (Realtime OS)
* 정해진 시간 내에 내 명령 수행이 보장 되느냐?

## Open-Source OS
### 4th Generation (1980- )
* Architectural Advances
	* 더 작고 빠른 마이크로 프로세서
	* 더 크고 빠른 스토리지
	* 개인용 컴퓨터
	* CPU 작업이 I/O 장치로 오프로드
* Modern OS Features
	* GUI
	* Multimedia
	* Internet & web
	* Networked, Distributed…
