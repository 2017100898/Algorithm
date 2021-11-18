# 메모리 관리 기법 (Memory-Management Strategies)
* Logical Memory   
* TLB (Paging)  
* MMU  

## 메모리 (Memory)
* 모든 작업은 메모리에서 일어나고 있다. 메모리는 컴퓨터 시스템의 중심적인 역할을 수행한다.
* CPU는 메모리로부터 명령을 받고, 명령을 수행하고 다시 메모리로 값을 저장하는 방식으로 동작한다. 메모리는 CPU로부터 값을 주고 받을 수 있는 유일한 저장장치이다. 
* CPU는 Disk, network, printers 를 직접 제어하는 것이 아닌, **메모리를 통해 제어한다.**
* Stall : 메모리를 쓰는 동안 낭비되는 CPU 사이클
* `메모리를 어떻게 관리할 것인가?`
* 메모리는 계층적인 구조를 갖고 있다. 위로 갈수록 빠르고 비싸다.
* SRAM - Cache
	* 가장 비싸고 빠르고, 용량이 작은 메모리
* **DRAM - Main memory**
	* CPU와 Memory의 커뮤니케이션 시 사용
	* Dynamic random access memory
	* 내가 원하는 위치에 무작위로 접근할 수 있는 메모리 (이전까지는 불가능)
	* 충전이 필요하기때문에 느리다.
	* 1 byte (8bit) 씩 쌓여있는 구조다.
	* 주소값은 `물리적 주소`다.
	* DRAM은 CPU보다 500배 가량 느리다.
	* 따라서 우리는 사이에 자주 쓰는 것은 Cache에 옮겨두고 사용한다.
* Flash disk / memory
* Magnetic disk - Hard disk
* Ideal memory


### Sharing / Protecting the Memory
* Q1 : 어떻게 하나의 메모리를 여러 프로세스가 동시에 사용할 수 있는가? - Sharing
* Q2 : 여러 개의 프로세스가 서로 어떻게 보호하고 있는가? - Protecting
* Answer : 각 프로세스는 **Logical (or Virtual) Address**를 사용한다.
* **각각의 프로세스는 동일한 논리적 주소를 갖고 있다. 그러나 물리적 디바이스에서는 다른 주소에 있다.**

### Base and Limit Registers
* **Protection**
	* User 프로그램은 Kernel 공간에 침범할 수 없다.
	* User 프로세스는 다른 User 공간에 침범할 수 없다.
	* Kernel 프로그램은 User 공간으로 접근할 수 있다.
* 모든 프로세스는 메모리에서 분리된 메모리 공간을 갖고 있어야 한다.

> Base register : 프로세스가 시작하는 주소  
> Limit register  :  프로세스의 크기  
> 프로세스마다 두개의 값이 정의되어 있으면 Protection 구현이 된다.  

* base가 1000이고, limit : 500이면, 프로세스가 1000번지에서 1500 사이에 할당을 받고 있다는 뜻이다.
* 만약 base 보다 작거나, base + limit 보다 크면 다른 프로세스에 접근한다고 판단하고, **trap**을 발생시킨다.

### Logical vs Physical Address
* **Logical Address** : user process에게만 의미가 있는 주소값
	* 실제로는 1000, 1400 을 할당받았다고 해도, 프로세스는 본인의 주소값을 0, 400으로 알고 있으면 된다.
	* 모든 기계어는 주소 기반으로 동작한다.
	* logical address != physical RAM address이기 때문에, 프로세스 안에서의 상대적인 주소를 누군가는 물리적 주소값으로 변환을 해줘야 한다. `MMU (Memory-Management unit)`
* **Physical Address** 

## Memory-Management Unit (MMU)
* MMU는 프로세스 안에서의 상대적인 주소를 물리적 주소값으로 변환 해주는 **하드웨어**다.
* MMU는 CPU에 들어가 있다.
* **Relocation Register** : logical 한 주소를 physical 한 주소로 맵핑시키는 가장 간단한 방법
	* Logical Address에서 시작되는 만큼 더해줘서 physical address로 바꿔주는 방법

### Address Binding
* Logical한 주소가 언제 Physical한 주소로 할당 및 배정이 되는지?
* **compile 할 때, load 할 때, Execution 할 때**
* **Compile Time**
	* Compile 하는 순간 물리적인 주소값으로 값이 바뀐다.
	* 현재의 환경에서는 메모리 지정해서 사용하는 것 불가능하다.
* **Load Time**
	* 프로그램 실행할 때는 SSD가 실제 메모리 위에 올라가고, 어디에 올라가는지 알 수 있다.
	* 그 메모리에 맞게 변수들의 주소값을 바꿔줄 수 있다.
	* 끝날 때까지 동일한 주소값에 있지 않을 수도 있다. 메모리가 커지면 더 넓은 메모리 있는 곳으로 복사할 수도 있는 문제가 생긴다.
* **Execution Time**
	* runtime, 그 코드 level에서 실행될 때 주소값을 바꾼다.
	
## Contiguous Memory Allocation
* **Memory Allocation** : 부팅 시 커널 메모리(OS)에 할당 되고, 남은 영역(유저 메모리)에서 프로세스들이 동작하게 된다.

### Multiple-partition Allocation

<img width="300" src="https://user-images.githubusercontent.com/64299475/141303603-d44f2eda-c864-4578-87be-06238be1c970.png">

* 메모리에 몇 개의 프로세스가 올라가있느냐에 따라서 Degree of Multiprogramming 결정된다.
* Variable-Paritition : 프로세스들이 차지하고 있는 크기(Partition)은 모두 다르다.
* **Hole** : 배치된 프로세스 사이 할당되지 않은 남은 공간
* Hole은 사용할 수 있는 공간이다.
* **External Fragmentation** : Hole이 여러 개로 나누어져있을 때는, 할당이 필요한 프로세스보다 total Hole이 크더라도 연속적이지 않는다면 할당을 할 수 없다. **이는 메모리를 매우 낭비하는 심각한 문제이며, Continuous Allocation의 단점이다.**
* 50-percent rule : N개의 블록의 할당을 반복하면, 절반정도가 Hole이 발생한다는 규칙 ⇒ 100MB의 프로세스를 할당하기 위해서는 150MB 메모리를 사용하게 된다. 실제로 사용한 것은 100MB, 50MB는 Hole이 된다.
* Internal Fragmentation

### External Fragmentation Solutions
* **Compaction** : Hole이 발생하면 Hole을 하나로 모으는 것
* Compaction을 하기 위해서는 기존의 프로세스들이 자리 이동을 해야 한다. `Relocation of Dynamic`
* Load Time시 모두 변환이 되면, Relocation 마다 바인딩을 다시 해야하는 불편함이 있다. `따라서, Only Contiguous Allocation 방법은 사용하지 않는다.`
* **Logical Memory는 붙어있어도, 물리적 메모리는 Noncontiguous Allocation을 사용하여 처리한다.**

## Paging
<img width="300" src="https://user-images.githubusercontent.com/64299475/141307366-dae7f313-0206-470c-b1bf-abfd1e146614.png">

<img width="300" src="https://user-images.githubusercontent.com/64299475/141307769-cb46755d-4d79-4516-a9a3-1a19aed66609.png">

* Noncontiguous Memory Allocation
* 물리적인 메모리를 가상의 크기로 모두 쪼개어 나눈다. 쪼갠 하나하나를 **frame**이라고 한다. 
* frame과 같은 크기의 Logical Memory를 **pages**라고 한다.

> Physical Memory의 단위⇒ **Frames**, Frames는 불연속적이다.  
> Logical Memory의 단위 ⇒  **Pages**, Pages는 연속적이다.  
> **Frames와 Pages의 크기는 같다.**  
> 각 Page는 물리적인 Frames의 어느 위치에 있다.  

* **Page Table**  : 어떤 Page가 어떤 Frame에 현재 할당 되어있는지 나타내는 것
* Page Table은 Kernel 영역에 존재한다.

### Page Number and Offset 🐢
<img width="300" src="https://user-images.githubusercontent.com/64299475/141308388-0a9f3423-451c-44c5-a38b-21809ca4cbc2.png">

* **Page Number (p)** : Page 번호
* **Page Offset (d)** : 그 Page에서 몇 번째 byte인가?

> Page Offset  == Frame Offset  

* Logical Address 크기는 정해져 있고, Page Number와 Offset은 정하기 나름이다. OS에서 정의한다.
* Offset은 크기만 정해주면 자동적으로 설정되는 것이다.

> Logical Address Space 가 **2^m**일 때,   
> Offset을 n으로 정하면 Page Size (Frame Size)는 2^n이 된다.   
> Page갯수는 m-n이 된다.  

#### Paging in bits Example
<img width="450" src="https://user-images.githubusercontent.com/64299475/141310843-38dc5afa-1d0a-485a-978e-9850f9812598.png">

* 정해져있는 주소를 Frame의 크기에 따라서 잘라서, 나머지 부분을 Page 번호로 하고, Page 번호를 Frame번호에 맵핑한다.

### Why Paging?
* 실제 메모리 상의 값이 물리적 메모리에서는 서로 흩어져있을지언정, Logical memory 상에서는 연속적인 메모리로 사용자가 생각하고 사용할 수 있다.
* **Transparency** 
	* 투명해서 있는지 조차 모른다. 인지하지 못 한다.
	* 따라서 Paging 쓸 때는, 우리는 Logical 만 생각해주면 되고, 물리적 메모리 부분은 우리에게 보이지 않는다.
* **No external Fragmentation**
	* External Fragmentation이 없지만, Internal Fragmentation이 발생한다.
	* Internal Fragmentation는 프로세스 내부에 사용하지 못 하는 공간이 생기는 것이다. **프로세스 보다 더 크게 할당해줄 수도 있기 때문에, 할당을 받았음에도 안 쓰는 공간이 생길 수 있다.**  
	* Internal Fragmentation를 예방하기 위해서는 Frame(Page)의 사이즈를 촘촘하게 잡는 방법이 있다. 그러나 이는 Page 개수가 엄청나게 많아지는 새로운 문제를 발생시킬 수도 있다. `tradeoff` 
	* 보통은 4-8KB 정도를 사용한다.

### Contiguous vs Paging
* Contiguous는 Table이 필요없다. 프로세스의 주소 찾기 위해서는 MMU를 통해 물리적인 접근을 쉽게 할 수 있다.
* Paging 은 MMU에서 Frame번호를 찾는 과정이 필요하다.

### Free-frame management
* 새로운 메모리 할당 받기 위해서는 비어있는 프레임 받아야 한다.
* OS는 비어있는 프레임에 관한 정보를 갖고있어야 한다. `Free-frame list`

### Implementation of Page Table
* 모든 프로세스는 Page0부터 시작한다.
* 그러나 프로세스1의 Page0과 프로세스2의 Page0는 다르다.
* **따라서 각 프로세스는 개별의 Page Table을 갖고 있어야 한다.**
	* **모든 Page Table은 Main memory에 저장 되어 있다.**
	* Page Table Base Register (PTBR) : 어디에 있는가? 
	* Page Table Length Register (PTLR) : 얼마나 긴가?
	* CPU는 두 값(시작점과 길이)을 가지고 있어야 하며, Register에 저장해 둔다.
	* **Logical 주소 ⇒ (메모리 접근) ⇒ Physical 변환 ⇒ (메모리 접근) ⇒ Physical 접근** `Page Table을 위해 2번의 접근이 필요하다.`
	* 이는 시간이 오래 걸린다는 단점이 있다.


### Page Table in Main Memory
* 메모리에 왔다갔다 하는 것은 낭비를 만들 수 있다.
* 따라서 메모리에 많이 접근하는 것은 치명적인 단점이 될 수 있다. **여기서는 Caching을 사용할 수 있다.**
* MLU에서 사용하는 `Cache` 의 이름은 `TLBs (Translation look-aside buffers)`라고 한다.

### TLBs (Caching)
* TLBs는 MMU의 용량이 작고 전용으로 사용하며, 엄청 빠른 Cache이다.
* 페이지에 대한 프레임의 정보를 갖고 있고, 조금이라도 테이블 내의 참조 번호를 읽어오는 것을 빨리하기 위해 만들어졌다.
* TLBs를 통해 Paging의 치명적인 단점 어느정도 보완할 수 있다.

> TLBs는 일종의 도박이다.    
> 이는 TLB에 내가 찾고자 하는 주소가 있을 경우에만 가능하고,     
> 없으면 오히려 다시 메모리에 접근해야 하므로 시간이 더 많이 걸릴 수 있다.  

> **TLB hit**  : TLB에 원하는 주소가 있을 때    
> **TLB miss**  : TLB에 원하는 주소가 없을 때  

###  Effective Access Time (EAT) 🐿✨⚡️
<img width="500" src="https://user-images.githubusercontent.com/64299475/141987593-f8394d0c-eeaa-42f9-a82b-3ddf4e7608b9.png">


* CPU에서 **메모리에 접근하는 시간**과 **TLBs에 접근 하는 시간**, **Hit Ratio** (TLB Hit의 확률) 을 통해서 Effective Access Time을 계산할 수 있다.

### Memory Protection
* Page도 우리가 접근하지 못 하는 메모리에 대해서 Protection을 수행할 수 있다.
* Page Table에서 `Valid-invalid bit` 개념을 도입하여, **할당 받은 데이터만 Valid 를 주고 접근할 수 있도록 한다.** 그외의 데이터는 접근할 수 없다.
	* Invalid : 프레임이 할당되어있지 않을 때는 프레임을 할당해주고 다시 접근하는 과정이 필요하다.

### Shared Page
* Shared Page는 두 개의 프로세스가 물리적인 메모리의 어떤 부분을 공유하는 것이다.
* 이는 `페이지에 대한 프레임 번호를 동일하게 두면 된다.`
* **모든 Page Table에서 같은 페이지가 같은 프레임을 가리키도록 하는 것이다.**

### Why Paging?
* Protection to memory
* Shared memory

## Structure of the Page Table
* 32Bit : 2의 32승 개의 address를 표현할 수 있다.
* 페이지의 크기 4KB : 2의 12승 Bit가 필요하다.
* 프레임의 개수 = address space - page size 
	* 2^64 : address space
	* 2^12 : page size
	* 2^52 : number of frame
* Page Table은 그 크기만큼 연속적으로 메모리에 할당이 되어 있다. 공간이 없으면 이것은 문제가 되고, 이를 위해 등장한 개념이 Hierarchical Paging이다.

### Hierarchical Paging
<img width="400 " src="https://user-images.githubusercontent.com/64299475/141991116-e339b652-a1cf-4300-a4ed-3b3138f9fb3d.png">
<img width="300" src="https://user-images.githubusercontent.com/64299475/141991957-53185f7d-5605-43cf-a20e-91d33a30f648.png">

* 두 번 참조하는 Hierarchical Paging은 페이지 테이블 수는 오히려 늘어나지만, **연속적인 메모리가 필요없게 된다는 장점이 있다.**

### Hashed Page Table
<img width="400" src="https://user-images.githubusercontent.com/64299475/141991968-7f39357f-7803-47e4-8dfc-b1e3ef3fa40b.png">

* Hash Table을 만들면 검색 시간을 향상할 수 있다.
* Linked list의 개념이다.

### Inverted Page Tables
<img width="400" src="https://user-images.githubusercontent.com/64299475/141992091-4b9518b7-140c-4089-9db6-7a3a4985daa0.png">

* Inverted Page Tables는 페이지 번호에 프레임 번호를 적어주는 것이 아니라, 실제 물리적에 첫 번째 프레임을 누가 사용하고 있는지 적어주는 것이다.
* `어떤 프로세스의 어떤 페이지가 프레임을 사용하고 있는가?`
* Table자체는 프레임에 대한 테이블 하나밖에 없다.
* 이는 Shared Memory는 아니다. 따라서 실제로는 사용되지 않는다.

## Segementation
* Segmentation 은 사용자의 관점에서 메모리를 나누는 것을 뜻한다. 메모리 공간을 규격이 아닌, Stack, Queue, Data, Text 등 논리적 단계에 따라 잘라서 Physical Memory에 넣는 메모리 관리 기법이다.
* Segment의 집합을 프로그램이라고 하고, Segment는 사용자의 관점에서 연관성이 있는 코드의 집합을 뜻한다. `Function, Object, Method, Stack...`
* Process의 Logical Address는 Segment 번호와 Offset으로 분리를 해서 표기한다.
* Segmentation Table을 통해 논리적인 주소로 바꿔줄 수 있다. 모든 Segment 는 크기가 제각각이므로 Continuous Allocation 을 사용하고,  이를 위해 **Base**(시작주소)와 **Limit**(크기, 길이)를 알아야 한다.
* Segment table base register (STBR)
* Segment table length register (STLR)

### Architecture
* **Relocation** 
	* dynamic
	* by segment table
* **Sharing**
	* 같은 Segment 끼리 공유 가능
	* Shared segements
	* same segment number
* **Allocation**
	* first fit (필요한 메모리보다 큰 홀 찾으면 바로 할당) / best fit (모든 홀 조사 후 필요한 메모리 크기와 가장 적합한 홀에 할당)
	* external fragmentation
* **Protection**
	* Validation bit을 통해 Protection
	* read, write, execute 권한 Segment 단위로 설정 가능
	* Segment 길이 모두 다르기때문에 메모리 할당에 문제 있을 수 있다.


### Segmentation Example
<img width="500" src="https://user-images.githubusercontent.com/64299475/141999714-2de4ed6b-fca3-4009-8ce2-2a89f16a2612.png">


> * Logical address
>	* s:2, d:100
> * Physical address
>	* 4400 ( 2 : 4300, limit 보다 offset 작으므로 4300 + 100 =4400)

> * Logical address
>	* s: 1, d:500
> * Physical address?
>	* **trap ( 1 : 6300, limit 보다 offset 크므로 trap 발생)**

### Segmentation의 장점
* 논리적인 단위로 나누기 때문에 단위가 커지거나 작아질 때 핸들링하기 쉽다.
* 같은 특성을 지닌 Segmentation 끼리  Protection, sharing을 하기 때문에 에러가 발생할 확률이 낮다.

### Segmentation의 단점
* 서로 다른 Segment 안에 있는 값을 주소로 접근하기 어렵다.
* Large segment tables (그래도 Page table 보다는 작다)
* Contiguous Allocation을 하기 때문에 **External Fragmentation** 이 발생할 수 밖에 없다.

### Paging vs Segmentation
<img width = "500" src= "https://user-images.githubusercontent.com/64299475/142004470-00a4c0ab-4b72-41ac-ac1c-cd26207fe3e7.jpeg">


* **Hybrid Approaches** (Segmentation + Paging)
	* 최초의 논리적인 단위는 서로 다른 특성끼리 나눈다. `Stack, Queue, Data, Code...`
	* 메모리에 할당을 할 때는 Paging 을 사용한다.
	* 이를 통해 두가지의 문제를 해결할 수 있다.
	* 하지만 메모리에 3번 접근해야하는 단점이 있다. 그래도  External Fragmentation을 통한 손해보다는 낫다.
