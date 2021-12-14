# Make: Networking
* 네트워크의 오픈소스화, open source software, hardware

## Internet of Thing (IoT)
* **RFID** : 물건을 실어나를 때 사람의 개입 없이 물건의 정보 인식을 자동화 할 수 있다.
* **IoT**는 네트워크로 연결 되고 이때까지 사람이 만든 것보다 더 많은 정보를 양상할 것이다.
* IoT 예시 : 네트워크 웹캠, E-Lock, Smart 전구,…
* Apple은 apple 기기끼리의 호환성이 매우 좋고 디바이스 자체가 apple의 비즈니스 모델이다.
* 하지만 Google은 관점이 다르다. 집 안의 기기들끼리의 통신하는 것에는 큰 영향력이 없다. *Google chromecast*
* AI 스피커, 애플워치 등 IoT는 특정분야에서 의미를 보이고 있고 기술적으로 소프트웨어, 프로세스, 네트워크를 이런 물건에 넣는 것이 점점 더 쉬워지고 있다.

## Physical Computing
<img width="500" src="https://user-images.githubusercontent.com/64299475/144702965-32e271c5-9b01-4f6b-b945-b5d98e3f25bf.png">

* **Physical Computing** 은 interactive physical system이다. sensor가 detect 하면 motor를 돌리거나, 불을 켜는 등 하드웨어를 제어하는 방법이다.
* 환경이 구축되면 사람이 하던 일을 자동화할 수 있게 되었다.
* 아두이노, 라즈베리파이의 등장으로 접근성이 더 좋아졌다.


## Cyber Physical System (CPS)
<img width="500" src="https://user-images.githubusercontent.com/64299475/144703029-7c12babf-a436-494c-a36f-fa380f525cd7.png">

* CPS는 컴퓨터를 기반으로 monitoring, controlling 되며 디자인, 기계학 등 다양한 학문이 섞여야 하므로 Trans-disciplinary 하다.
* CPS는 스마트팩토리 등 규모가 큰 시스템에서 운영된다.
* 네트워크와 네트워크가 연결된 기기들 간의 협업이 매우 중요해졌다.
* Physical Computing이 단순히 센서를 통해 입력 받아 반응을 하는 것이라면, CPS는 공장 수준의 컴퓨터가 서로 협업, 커뮤니케이션, 정보 분석까지 수행 해야 한다.

## Open Source DIY Networking
* 아두이노는 디지털, 아날로그 입력을 받아 출력(모터, 불빛 등)을 내보낸다. 아두이노는 운영체제가 없기 때문에 매우 단순한 프로세스, 프로그램만 작동 가능하다.
* 오픈 하드웨어는 소프트웨어의 발전에 의해 발전하기 시작했다. (Ex. 라즈베리 파이 위에 Linux가 올라가서 Wireless wifi가 되는 것, PrivateBox)
* OpenWRT : Wifi router 만들 수 있도록 하는 오픈소스 소프트웨어다. OpenFlow로 가능하게 되었다.
* The Serval Mesh : 안드로이드 휴대폰끼리의 네트워킹, 안드로이드 밑에는 리눅스가 있다.
* iOS도 iOS7 부터는 apple 기기끼리 mesh networking 이 가능하다. 
* TOX : Instant messaging, voice, video,… 모두 가능하며 이는 peer-to-peer로 이루어진다. 서버가 없다. 따라서 근거리에 같은 네트워크에 있을 때만 가능하다.
* Open network : 오픈 소프트웨어와 하드웨어를 통해 open network를 만드는 것. 내 컨텐츠에 다른 기업들이 접근하지 못 하게 할 수 있다.
* Open Source Basestation (기지국) :  Open BTS (2G), 오픈소스화된 이동통신 기술을 이용해 이동 통신을 직접 만들 수 있다.
* Range Networks’ Professional Development Kit

## Specialized OS for IoT
* 정말 작은 하드웨어를 지원하는 운영체제가 기존에 없다가 등장했다.
* Zephyr (Linux) - size가 매우 작고 처음부터 IoT를 위해 만들어졌다.

## OCP Telecom Infra Project
* 5G 이동통신 OCP TIP의 소프트웨어는 인공지능, 운영 자동화, E2E-NS (end-to-end network slicing), openRAN 을 만들 수 있다.
* Fixed wireless : 무선인데 고정된 지점으로 초고속으로 날리는 것, wifi zone을 만들 수도 있다.
* Open/R : Routing 알고리즘 개발하기 위한 환경 제공한다. real-time, RTT-Based cost metrics (주변 라우터들과 통신 후 어디로 보내야할지 판단), fast convergence, drain/undrain operations
	* 주변 기기들과 정보 주고 받고 라우팅 테이블을 만들고 이를 하드웨어 Switch로 내리는 기능을 지닌다.
	* Ad hoc network (Open/R은 주변 기기들끼리 network 스스로 만들고 연결하고 트래픽을 주고 받는 것이 목적이었다.)
