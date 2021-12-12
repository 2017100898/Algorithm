# Virtual Memory Management
## Virtual Memory
* 메모리 체계에 접근할 때, Logical Memory를 Physical Memory에서 분리하여 **DRAM이 아닌 Virtual Memory에 접근**하는 것이다. Virtual Memory는 실제 DRAM의 크기와 다를 수 있다. 
* 이는 virtual address, 즉 logical address와는 다른 것이다.
* 모든 프로그램이 메모리 위에 올라갈 필요는 없고, Virtual Memory는 프로세스를 만드는데 있어 효율적이다.
* Virtual Memory가 10GB고, DRAM이 8GB라면, 나머지 2GB는 Disk(SSD)에 있다.
* Virtual Memory는 공간을 마음대로 사용할 수 있다는 장점 있지만, 느리다.

### Swapping
* **내가 사용하지 않는 프레임을 Main Memory에 놔두면 아깝기 때문에 Disk에 그대로 옮겨 저장해 둔다.**
* Swapping은 모든 프로세스가 할당 받은 모든 메모리를 Disk에 옮겨 놓고, 필요 시 다시 Main Memory에 옮겨두는 것이다.
* Swapping시 Context Switching Time은 매우 느리다. 따라서 요즘에는 Swapping을 잘 쓰지 않는다.

## Demand Paging
### Basic Concepts
* 프로세스는 페이지들의 연속된 집합이다.
* 우리가 어떻게 실행 파일을 Disk에서 메모리로 옮길 것이냐?
	1. 통채로 옮긴다. `- 편리하지만 공간을 비효율적으로 쓰게 된다. `
	2. 필요한 부분만 그때그때 옮긴다. *`- Demand Paging`*
* **Demand Paging 장점**
	* 입출력이 적고, 빠른 시간 안에 프로그램을 실행할 수 있다.
	* 더 적은 메모리가 필요하고, Multiprogramming의 Degree가 올라간다.
* Demand Paging는 페이지가 필요할 때 메모리를 할당 받는 것이다.
* `페이지 단위`로 Disk 위에 저장해둘 수 있고, 내가 필요할 때 다시 저장해둔 Frame 을 Main Memory로 가져온다.
* **Pager** : Demand Paging을 처리하는 알고리즘
* Heap은 위로 자라고 Stack은 아래로 자란다. 처음 프로세스 시작할 때는 Heap과 Stack 사이가 비어있다. 이처럼 사용하지 않는 큰 공간을 처음부터 물리적 메모리에 할당하는 것은 낭비다. **따라서, 처음에는 할당하지 않고 있다가 사용 해야할 때 Demand Paging을 통해 할당한다.**
* **Dynamically Linked Libraries (DLL)**
	* 주로 Function을 실행할 때 Function에 해당되는 코드를 메모리로 복사해서 사용한다.
	* Stub : Library 어디에 가서 가져와야 하는지에 대한 정보를 갖고 있는 것.
* 모든 페이지들이 Main Memory에 있는 것은 아니다.

### Valid-Invalid Bit
<img width="200" src="https://user-images.githubusercontent.com/64299475/142428922-8114b635-4c4f-40fe-b6ad-54f6e247e3a9.png">

* i는 메모리를 할당 받지 않은 페이지, v는 할당을 받은 페이지를 뜻한다.

### Page Fault
* **Page Fault**는, Logical address를 Physical address로 바꾸려고 **Logical address에서 Page Number를 갖고 Page Table에서 Frame 번호를 찾았는데, 알고 보니 아직 할당이 되어 있지 않아서 (또는 할당을 받았다가 다시 Disk로 가있어서) 부재중인 상태를 발견했을 때를 뜻한다.**
* Page Fault가 발생하면, 모든 일을 중단시키고 Disk에 저장되어 있는 것을 찾아서 다시 Page Table을 v로 수정하고, 다시 한 번 해보라고 명령을 내린다.

### Performance of Demand Paging
<img width="400" src="https://user-images.githubusercontent.com/64299475/142430612-7fbb2860-85aa-4331-8d52-da9a913eb21c.png">

* 지난 시간에 언급한 Hit Ratio는 높을 수록 좋지만, Page Fault Rate은 낮을 수록 좋다.
* page out : 자리가 없으면 기존의 것 하나 내보내야 함.

> Memory access time = 200 ns  
> Average page-fault time = 8ms (= 8,000,000 ns)  
> **EAT** = (1-p) * 200ns + p(8ns)  
> = (1-p) * 200 + p * 8,000,000 (ns)  
> = 200 + p * 7,999,800 (ns)  
> 만약 p=0.001이라면, **EAT = 8,200ns  (= 200ns * 41)**


* How to imporve EAT?
	* **Anticipatory paging** : Disk에서 필요한 부분만 가져오는 것이 아닌 미리 사용될 것 같은 것들도 함께 가져온다.
	* **Principle of Locality** : 코드의 흐름 상 다음에 사용할 것 예측할 수 있다.

## Page Replacement
### Basic Page Replacement
* Free frame이 있으면 그 자리에 넣어주면 되지만, 만약 모든 메모리가 사용 중이라면?
	* 대부분의 경우 비어있는 프레임이 없는 경우가 많다.
	* **Page Replacement** : 메모리가 꽉 차있을 때 하나를 Disk로 빼내고 그 자리에 할당하는 것이다.
	* Performance : 다*음에 사용이 될 가능성이 높은 페이지는 계속 가지고 있는 것이 좋다.* 사용이 되지 않을 것 같은 페이지를 잘 선별해서 내보내야 한다. `page out`
* **Page Replacement Algorithm** : 현재 메인메모리를 차지하고 있는 것 중 **어떤 page를 disk로** 내보낼 것인지 찾는 것.
	* disk 로 가게 되는 page를 `victim frame`이라 한다.
* 이후 Frame Table을 수정하고 프로세스를 다시 시작하면 된다.

### Modify (Dirty) Bit
* 모든 메모리가 꽉 차 있으면 두 번의 page를 옮겨야 한다.
	1. Victim frame to disk (page out)
	2. Demand page to memory (page in)
* *한 번 만으로 할 수는 없을까?* ⇒ `Modify Bit`
	* 어떤 Frame을 읽어올 때는 Modify bit를 0으로 설정, Frame 값 수정 시 bit를 1로 설정하는 방법이다. 
* Modify bit이 0인 page를 victim으로 설정하는 것이 좋다. 0인 Frame은 불러온 이후 사용이 안 된 것이기 때문에 그냥 삭제하면 되고, Page out을 하지 않아도 되기 때문에 시간을 줄일 수 있다.

### Benefit of Virtual Memory
* **Protection** : 하나의 논리적 주소를 가진 것이 다른 프로세스 공간에 접근할 수 없다.
* **Transparency** : 물리적인 메모리가 어딘지 몰라도 논리적인 주소만 알고 동작한다.
* **Resource Exhaustion** : 내가 갖고 있는 Resource를 최대한 활용 할 수 있다. 
	* Demand Paging

## Page Replacement Algorithms 🐿🥜✨
* 어떤 Frame을 Victim Frame으로 설정하느냐에 따라서 성능 차이가 많이 난다. 
* 다양한 선정기준에 따라 Page Fault 발생을 최소화 시키자!
* 1초에 1000번 사용되는 페이지와 1번 사용되는 페이지 중, 후자를 Disk로 보내는 것이 좋다.
* 물리적인 Frame이 많을 수록 Page Fault는 적게 일어난다. 

### FIFO Page Replacement
<img width="600" src="https://user-images.githubusercontent.com/64299475/143274490-4071f21c-d7fa-4af6-ac38-d288191f809c.png">

* 단순히 가장 먼저 할당 받은 프레임을 디스크로 보내는 방법이다.
* 그러나 FIFO에서는 Frame 갯수가 늘어났음에도 Page Fault가 늘어나는 상황이 종종 발생한다. - `Belady's Anomaly`

### Optimal Page Replacement
<img width="600" src="https://user-images.githubusercontent.com/64299475/143274484-45a4afed-6f30-4130-9259-8c1b2b595bb7.png">

* 앞으로 가장 사용이 안 될 프레임을 디스크로 보내는 방법이다. 이는 프레임 크기와 페이지의 sequence가 정해졌을 때, 가장 이상적인 값을 뜻한다.
* 그러나 우리는 미래에 어떤 페이지가 사용될지 다 알 수 없기 때문에 현실에서는 구현할 수 없다.
* 그러나 Optimal Page Replacement는 다른 알고리즘의 성능을 파악하고 싶을 때 사용할 수 있다. 어떤 알고리즘의 결과값이 Optimal Page Replacement와 같은 값이라면, 그것이 Best라고 판단할 수 있기 때문이다.


### LRU Page Replacement
<img width="600" src="https://user-images.githubusercontent.com/64299475/143274464-76aeccf8-9b58-48a7-a619-54d0e9730251.png">

* Least Recently Used Algorithm
* **Page를 사용 하지 않은 시간이 길면 길 수록 disk로 갈 확률이 높아지는 알고리즘이다.**
* LRU Algorithm을 구현할 때는, **Counter** (timestamp) 와 **Stack**을 사용한다.

#### Counter
* 모든 페이지는 Counter를 갖고 있다. 시간은 계속해서 Update를 하고, **가장 적은 값을 가지는 Page (즉, 가장 과거에 사용했던 Page)를 Replace 한다.**
* Counter 사용 시 단점
	* 프레임이 많을 때는 계속해서 각 Counter를 Search 해야 한다.
	* 어떤 메모리 참조를 할 때마다 Update해줘야한다는 단점이 있다.

#### Stack
* **Stack은 Page가 사용될 때마다 가장 위로 올리는 개념**이다. Replace시에는 가장 아래에 있는 Page를 선택한다.
* Array로 구현 시 메모리 복사 비용이 굉장히 크므로, Stack은 **Linked-list로 구현** 한다.
* Stack 사용 시의 단점
	* Doubly Linked-list의 6개의 포인터를 바꿔줘야한다.
	* 비용이 많이 든다.


### LRU Approximate Algorithm (Reference bit)
#### Second-Chance (clock) Page-replacement Algorithm
<img width="400" src="https://user-images.githubusercontent.com/64299475/143276726-817def53-b3ce-4864-8519-b54c2bae1294.png">

* 처음에는 모두 0으로 셋팅이 되어 있고, 어떤 페이지가 참조될 때 1로 만들어준다.
* next victim 포인터가 계속 돌아다니다가, bit가 1인 페이지는 0으로 수정하고 패스 하고, bit가 0인 페이지를 만나면 그 페이지가 page out 된다.

#### Counting Algorithm
<img width="400" src="https://user-images.githubusercontent.com/64299475/143278081-34d3aba1-8b3c-44f0-a206-b2592a4e9a99.png">

* **LFU Algorithm** : 얼마나 많이 사용되었는지 **카운팅** 해서 가장 적게 사용된 Page가 page out 되는 알고리즘이다.
* **MFU Algorithm** : 가장 많이 사용된 Page를 내보내는 알고리즘이다. 이미 사용할 만큼 했으니 나가도 된다는 관점이다.
* *기간이 아닌 빈도수를 기준으로 Victim을 정하는 것이 핵심*이다.
* **Aging 기법** : Counter에 대한 bit들을 사용 시 가장 왼쪽에 1값을 주고, 사용하지 않을 시 매번 1비트씩 오른쪽으로 shift 시키는 방법이다. 즉, 절반으로 깎는다. (첨부 사진)

## Sharing and Memory Mapped Files
* Shared Library : 프로세스마다 라이브러리를 사용할 때, 같은 주소로 공유하여 사용할 수 있다.
* fork() : 프로세스를 복사하여 생성해 내는 것이다.
* **Copy-on-write** : **처음에 fork 할 때는 두 프로세스가 같은 물리적 메모리를 공유하는 것이다.** 처음에는 굳이 달라야하는 이유가 없기 때문이다. 값이 달라지는 순간 물리적인 공간에서도 복사하여 개별 할당을 할 수 있다.
* Memory-Mapped File : 파일을 다룰 때, 메모리에 올려서 메모리에서 읽고 수정한다. 다 쓰면 Close 후 disk에 저장한다.
* File sharing via Memory-Mapped files: 여러개 프로세스가 같은 파일을 쓸 때도, disk file은 메모리에 올리고, 여러개의 프로세스들은 그 메모리를 공유하는 방식으로 파일을 사용한다. 이 경우 [동기화](https://github.com/2017100898/TIL/blob/main/OS/synchronization.md)가 필요하다.
* Memory-Mapped I/O : 모든 레지스터들을 메모리의 특정 공간에 맵핑 시켜서 메모리 위에서 읽고 쓰는 방식으로 디바이스를 조절한다.


