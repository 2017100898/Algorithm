# Cloud Computing
## Introduction to Cloud Computing
### General Idea of Cloud Computing
<img width="500" src="https://user-images.githubusercontent.com/64299475/143434165-44a47c12-c8e5-4db7-b6a0-b2e35a2b479c.png">

* **클라우드 컴퓨팅(Cloud Computing)** 은 지구 어딘가에 컴퓨터, 디스크, 네트워크가 물리적으로 있고 운영 또한 되고 있으나, 그것을 사용하는 유저에게는 보이지 않는 컴퓨팅 방법이다.
* 유저는 클라우드 컴퓨팅을 필요할 때 필요한 만큼 쓰고, 그에 걸맞는 댓가를 지불하기만 하면 된다.

### Why Cloud Computing?
* **CPU와 네트워크를 빌려주는 회사**와 **사용하는 회사(개인)가 다르다**고 가정해 보자.  `Public Cloud Computing`
* **빌려주는 회사**는 이미 컴퓨터를 많이 가지고 있는 큰 회사다. 그러나 이들은 수많은 컴퓨터를 매일 그리고 하루종일 쓰는 것이 아니기에 분명 **사용하지 않는 시간이 있다.** 따라서 컴퓨터가 많아도 효율이 떨어지는 것이다. 이 컴퓨터들을 쓰지 않을 때, 작은 회사 또는 개인에게 이 컴퓨터를 빌려주게 되면, 회사는 컴퓨터를 낭비하는 시간을 줄이고 경제적으로도 이득을 볼 수 있다.
* **사용하는 회사**는 벤처 회사 등 본인의 서비스를 앞으로 몇 명이 사용할지도 모르고 수많은 컴퓨터를 사기에도 비용 측면에서 부담스러운 회사다. 따라서 이들은 큰 회사의 컴퓨터를 빌려씀으로써 문제를 해결할 수 있고, 수요가 급증하는 순간에도 빠르게 대처할 수 있다.

### Cloud Computing Types 🐢⚡️✨
#### XaaS
<img width="300" src="https://user-images.githubusercontent.com/64299475/143438235-29d432f2-cddb-4889-a0a6-9a106ca7387f.png">

* **IaaS (Infrastructure as Service)**
	* Amazon Web Service (AWS)
	* 가장 근본적이고 날 것의 것을 제공한다. - **Hardware, Virtualized Instance (Virtual Machine), OS(Guest OS)**, 물리적인 Hardware을 빌려주는 것은 아니고 그 위에서 돌아가는 가상 머신을 빌려주는 것이다.
	* 필요할 때 가장 기초적인 인프라를 제공하고, 그 위에 해당하는 OS service, Application 등은 본인이 알아서 해결해야 한다.
* **PaaS (Platform as Service)**
	* Microsoft Azure
	* Google App Engine
	* **가상머신부터 OS service, Frameworks까지 제공한다.** 마찬가지로 그 위에 올라가는 Application은 본인이 해결을 해야하기 때문에 보통 개발 능력이 있는 사람들이 사용하는 서비스다.
* **SaaS (Service as Service)**
	* Gmail System
	* Microsoft Office Live/Online
	* **바닥부터 서비스까지 모두 제공한다.** 사용자는 서비스를 바로 쓸 수 있고 사용한 만큼 비용을 지불하기만 하면 된다.

### Public or Private
* 빌려주는 자와 빌려쓰는 관계에 의해 정의된다.
* **Public cloud computing solutions**
	* 컴퓨터를 빌려쓰는 자가 빌려주는 회사 소속이 아닌 경우를 뜻한다.
	* Amazon, Mircrosoft, Google
* **Private cloud computing solutions**
	* 컴퓨터를 빌려쓰는 자가 빌려주는 회사 소속인 경우를 뜻한다.
	* 회사 내에서 컴퓨터를 관리하는 부서가 필요한 부서에게 제공하는 경우다.
	* **OpenStack**
* **Hybrid cloud computing solutions**
	* Public과 Private를 섞을 수도 있다. **일반적인 기간에는 Private**하게 쓰다가, **서버가 폭증하는 순간에만 Public**으로 돌려서 다른 회사의 컴퓨터를 빌려쓴다. (학교의 수강신청 기간, 테스트 기간 등이 이에 해당한다.)
	* 하지만 기술적으로 Hybrid를 구현하는 것은 굉장히 어렵다. 회사마다 PaaS의 형태가 매우 다르기 때문이다.
	
## Public Cloud Services
### Amazon Web Service (AWS)
* Amazon은 자사가 필요해서 만든 소프트웨어들을 다른 사람들에게 빌려준다. AR, VR, Block Chain, Game, IoT, ML, Robot, DB 등까지 제공한다.

### Microsoft Azure
* 마이크로소프트는 기업용 소프트웨어에 특화되어 있다. 따라서 제공하는 소프트웨어들이 주로 비즈니스, 기업에 초점이 맞춰져 있다.

### Google
* 구글은 자체 하드웨어인 Tensorflow Processor가 있기 때문에, 유저들이 이 하드웨어 위에서 소프트웨어를 설계할 수 있도록 한다. MMORPG Game server 또한 제공하고 있다.

### Apple
* 애플은 위 회사들과는 다른 관점이다. 애플은 그들의 기기와 컨텐츠를 파는 것이 중요하기 때문에 애플 기기끼리만 쉽게 연동할 수 있는 클라우드(iCloud)를 만들었다.

## Cloud Computing APIs
* EC2, S3는 사실상 업계의 표준이다.

### EC2 (Amazon Elastic Compute Cloud)
* virtual computer를 빌리는 인터페이스다. 대부분 웹서비스를 위해 많이 빌려쓴다.
* CPU, 캐쉬, 코어, virtual computer의 위치 등까지 선택을 해야 한다. 모니터링까지 가능하다.
* 기능은 GPU graphics Instance, I/O, Storage, Cache Memory, auto scaling 등 다양하다.
* Amazon Machine Images (AMIs) : 이미지 또한 커스터마이즈 해놓아서 받을 수 있다.

### S3 (Amazon Simple Storage Service)
* 단순하게 Storage를 관리하는 서비스다. REST, SOAP, BitTorrent
* 아마존이 쓴 후 검증이 된 것을 제공한다. 

## Thin Client 
* Thin Client는 _웹브라우저만_ 켤 수 있는 컴퓨터다. 이런 컴퓨터는 웹브라우저만 사용할 때 사용하고, 일반적으로 웹브라우저 바깥의 운영체제에 무언가를 쓰는 것을 금지한다. 이러한 Thin Client는 웹상으로 대부분의 서비스가 돌아가는 세상이 되었음을 시사한다.
* Microsoft office의 웹버전 워드, 엑셀, 파워포인트 등
* 가장 유명한 Thin Client는 [Google Chromium OS](https://www.chromium.org/) 다.
* Firefox OS, FlinsOS
* POS System

## Private Cloud Solutions
* 사내의 인프라를 사내의 다른 조직이 사용하는 것을 뜻한다. 사내 인프라 위에 사내 어플리케이션이 올라가는 것이 특징이다.

### 오픈스택 (OpenStack)
* OpenStack은 클라우드 컴퓨팅을 본인의 회사에서 구축할 수 있도록 하는 오픈소스 솔루션이다. 즉 _Private Cloud 환경 구축을 위한 Solution_이다.
* 프로세서, 네트워크, 저장소를 빌려주는 소프트웨어이며, 유저는 API를 통해 빌려쓸 수 있다.
* 오픈 스택을 기반으로 데이터분석, 인공지능, 알고리즘 등의 규모가 커졌다.

## Beyond Cloud Computing
### Non Virtual Machine Approach
<img width="400" src="https://user-images.githubusercontent.com/64299475/143546459-667a6543-73de-4cc2-af96-6867629ff805.png">

* **IaaS - VM** : 빌려주는 회사는 OS위에 Hypervisor을 깔아놓고, 빌리는 회사들은 그 위에 Guest OS와 본인의 어플리케이션을 올려서 사용한다.
* **Private Cloud** : 대부분의 회사는 개발 환경이 통일 되어 있다. 따라서 OS를 굳이 변경하지 않아도 되기에 Private Cloud에서는 기존의 VM을 따르지 않고 **Container Technology 기반의 데이터센터 개발 및 운영환경**을 사용한다.
* Container는 지금 돌아가는 OS 위에 Package로 프로그램을 설치할 수 있고, 지울 때도 깔끔하게 지울 수 있다는 장점이 있다. 서로의 영역 또한 침범하지 않고 가볍다는 특징이 있다.
* 반대로 가상 머신은 성능 저하를 일으킬 수 있다.
* **Docker** : 돌아가는 프로그램이 어떤 OS 위에서 돌든 상관 없이 컨테이너를 실행시킬 수 있게 하는 소프트웨어 (개발, 운영)
* **Kubernetes** : Container-orchestration. 많은 컴퓨터 위에서 관리 및 제어 할 수 있는 소프트웨어. 수만개의 소프트웨어들이 유기적으로 돌아가도록 한다. (운영)
* Cloud Native Computing Foundation : 소프트웨어의 설계부터 수만개의 컴퓨터에 맞도록 하는 회사다. Linux 산하의 Foundation.
* **Cloud Native** : Container, Microservices (돌아가는 프로그램을 잘게 쪼개서 CPU를 분배하는 것), Continuous delivery (굉장히 빨라진 개발환경-CI/CD),  DevOps
* **Edge computing** : 디바이스 대신 해주는 일은 중앙이 아닌 디바이스의 근처에서 해주는 방법이다. 즉, 작은 데이터센터들이 유저들 가까이로 들어가는 것이다. - StarlingX
	* 그러나 외부로 나가야하기 때문에 보안의 문제가 발생하고, 서버와 소프트웨어가 작다. 신뢰성과 용량확장에도 에러가 있을 수 있다.
* Software-Defined Cars