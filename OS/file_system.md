# File System
## File and File System Concept
* 우리의 파일은 SSD 안에 있다.
* platter가 여러 개 쌓여있어서 한장 한장 정보를 기록할 수 있는 것이 하드디스크의 기본 구조이며, track과 sector로 공간을 나눠서 정보를 기록한다. sector를 여러 개 모아서 하나의 block이라 한다.
* HDD : 자기장의 극성을 이용해서 비트 정보를 저장한다.
* SSD : 전자의 개수로 비트를 저장한다.
* 이처럼 사실상 HDD와 SSD는 다르지만 운영체제 관점에서는, SSD와 HDD를 크게 구분하지 않는다.

### File Concept
* 모든 정보는 디스크에 File로 저장할 수 밖에 없다.
* *What is a File?*
	* 사용자의 관점에서는 **파일이란 저장 되어 있는 단위**이다.
	* 시작과 끝이 있는 하나의 덩어리, **데이터들이 sequence하게 있는 것**이다.
	* 파일의 특정한 **위치**는 **시작점으로부터의 거리로 나타낼 수 있고 이는 offset이라 한다.**
* *File System*은 파일을 다루는 방법이다.
	* 사용자 관점의 File을 디바이스에 어떻게 mapping 시킬 것인지, **즉 디스크에 어떻게 관리할 것인지 결정하는 것**이다.
	* 논리적인 주소가 물리적인 주소로 바뀌기 위해서는 Translate이 필요하며, 이 또한 File System의 역할 중 하나다. Translate 시에 앞서 설명한 offset을 사용한다.
	* 파일은 연속적으로 들어가 있을 수도 있고, 쪼개어져서 들어갈 수도 있다. 쪼개져있는 파일을 찾아오는 것도 File System의 역할이다.

### File Operation
* Create (파일 생성) : 디스크 공간을 할당 받고 File System을 업데이트 한다.
* Read/Write

### File Information
* **File Pointer** : 파일을 읽을 때는 어디를 읽을 건지 위치를 지정해줘야 한다.
* **File-open count** : File은 프로세스와 달리, 공유하는 경우가 매우 많다. 파일 기준으로, **몇 개의 프로세스가 해당 파일을 사용하고 있는지** 알아야 한다. 또한 실제로 **해당 파일이 Disk의 어디에 저장되어있는지**에 대한 정보도 저장을 해야 한다.

### File Types
* Unix, Linux, MacOS에서는 모든 것들을 다 파일로 다룬다. - `disk, directory, 바로가기 …` 
* Window는 확장자명으로 파일의 타입을 파악한다.
* Unix는 파일 앞단의 정보를 통해 파일의 타입을 파악한다.

### File System 🥕🐇⚡️
* **File System**은 크기가 한정된 **디스크에 파일을 어떤 식으로 저장하고 관리할 것인지에 대한 규칙 (방법론)**이다. 
* 따라서 File System은 한 가지가 아니며 운영체제마다 사용하는 File System도 다르다.
* File System은 Disk 상의 Data Structure라고 할 수도 있다. Disk에 여러 파일 시스템이 동시에 올라가 있을 수도 있고 이때 각 File System의 단위를 **Volume**이라 한다.

### File System Implementation
* **On-disk** : File System을 구현할 때는 Disk를 구분 지어서 사용하게 된다.
* On-disk File system `4 parts`
	* **Boot Control** : 디바이스를 처음 구동시키는 코드. 가장 상단에 위치하고 OS에 대한 정보 지닌다.
	* **Superblock** (or volume control block) : Volume details, 디스크 자체를 관리하기 위한 정보 지닌다.
	* **Metadata**  : 데이터를 위한 데이터. 파일을 관리하기 위한 데이터.
		* **Directory Structure** : 파일 위치 정보 (구조), 트리 구조로 나타낸다. 트리 안에는 FCB의 주소가 들어있다. 
		* **File Control Block (FCB)** :  `파일 정보, file id, 권한, 소유자, 크기, 파일의 위치…` FCB의 정보를 통해 파일을 찾을 수 있다.
	* **Data blocks** : 파일들이 블록 단위로 쪼개어져서 (또는 연속적으로) 실제 저장이 되어 있는 곳

### Layered File System
* 여러 층으로 이루어져 있고, 본인이 맡은 역할만 하면 되는 레이어로 구성 되어 있다.
* 파일 시스템의 역할
	* **Logical File System** : Metadata 관리
	* **File Organization Module** : Translate logical block - physical block, free space 관리, 디스크 할당
	* **Block file system** : logical 한 주소를 물리적인 주소로 바꿔줌, buffer caches 관리
	* **I/O control** : 디바이스와 연결 되어 데이터 읽고 쓰는 역할

## File Operations
* 파일을 읽고 쓰기 이전에는 `Open()` 해야 한다.
* **Open()** : file 에 대한 metadata (FCB)를 메모리로 가져온다.
* Open 된 파일의 수가 많아지면 파일을 다뤄야 하고, 파일 다루기 위해 메모리를 갖고 있는 객체를 **File handle, File descriptor**라 부른다.
* **In-memory structure**
	* 속도: Main memory > Disk (필요로하는 메타데이터 메인메모리에 옮겨놓고 사용하는 것이 좋다)
	 * **Directory Structure Cache** : Directory Structure를 Caching 하기 위해 만들어진 구조체
	 * **Directory** : 매우 큰 트리구조, 디렉토리 단위로 정보를 나눌 수 있다.
	 * 원래는 Directory Structure에 가서 FCB에 대한 정보를 받아와서 FCB에 접근을 해야하는데, Directory Structure Cache가 있으면 바로 접근할 수 있다.
* **Create a File**
	1. system call 을 통해 disk 에 파일을 만든다.
	2. disk 메타데이터 공간에 새로운 *FCB*를 만든다.
	3. directory가 있으면 쓰고 없으면 불러와서 업데이트 해준다. (새롭게 만든 FCB 주소를 디렉토리에 추가)
	4. 이를 다시 disk로 저장한다.
* **Open a File**
	1. System-wide open-file table이 있는지 찾는다.
	2. 찾는다면 누군가가 사용하고 있다는 뜻이므로, 내 pre-process open-file table에서 FCB 주소로 directing 하면 되고, count++해준다.
	3. System-wide open-file table에 파일이 없으면 우선 그 파일에 해당하는 directory structure cache 부터 업데이트 해야 한다.
	4. FCB를 table로 옮겨놓는다.
	5. Directory 도 갖고와서 directory structure에 넣어준다.
	6. 이제 그 위치의 주소값만 알고있으면 된다.
* **Close a file**
	1. count가 하나씩 줄어들고, count 0이 되면 아무도 사용하지 않고 있다고 판단 할 수 있다.
	
### File System Implementation
<img width = "400" src="https://user-images.githubusercontent.com/64299475/144254559-fa83eb9c-6b05-4019-b643-ef93074a1812.png">

* `우리가 자주 사용하는 FCB도 메모리에 옮겨놓으면 더 빠르지 않을까?`

#### System-wide open-file table
	* 현재 열려있는 파일에 대한 테이블, 사용 시 FCB에 대한 정보를 복사해둔다.
	* **count** : 현재 몇 개가 이 파일을 사용하고 있는지에 대한 정보
	* FCB를 찾으러 파일을 가는 시간을 줄이기 위해 사용한다.
#### Per-process open-file table
	* 프로세스마다 Per-process open-file table을 갖고 있고, 이것은 system-wide open-file table의 위치를 가리키고 있다.

## File Access and Allocation Methods
### Sequential and Direct Access
* `Access : 파일을 우리가 어떻게 접근할 것이냐?`
* **Sequential Access** : 순차적으로 읽는 것
	* File pointer를 기준으로, current position 계속해서 오른쪽으로 가면서 read/write하는 접근 방식이다.
	* 대부분의 파일은 sequential 방식을 사용한다.
* **Direct Access** : 필요한 위치의 값 바로 읽는 것 
	* 앞과 뒤의 인과관계가 없는 파일에 접근할 때 사용하는 접근 방식이다.
	* database에서 많이 사용한다. 

### Contiguous, Linked and Indexed Allocation
* 파일을 실제로 어떻게 배치할 것이냐?
* Contiguous : 파일이 연속적으로 저장 되는 것
* Non-contiguous : 파일을 블록단위로 잘라서 각각 배치하는 것
* Allocation의 목표
	* 최대한 디스크 공간을 많이 사용하면 좋다. (활용도)
	* 빠르게 접근할 수 있으면 좋다.
* **Contiguous Allocation**
	* 파일이 연속된 블록으로 되어있을 때, 그 블록들을 실제 물리적인 공간에서도 연속적으로 할당하는 것이다.
	* directory는 파일의 starting location과 length를 갖고 있으면 된다.
	* **장점**
		* **Direct Access에 적합하다.**
	* **단점**
		* 새로운 파일이 있으면 space를 찾아서 할당해줘야 한다.
		* External Fragmentation - 홀의 크기가 작아져서 그것보다 큰 파일을 집어넣을 수 없어서 발생하는 문제, 주기적 compaction 해야 한다.
		* file size extension에 취약하다. - 파일은 크기가 계속해서 변한다. 그럴 때마다 새로운 곳을 찾아서 계속 복사하던가 미리 예측을 해놔야하는 단점이 존재한다.
* **Linked Allocation** (Non-contiguous)
	* Linked List 방식을 이용하는데, node 대신 block을 이용해서 구현한다.
	* 나의 다음 블록이 누구인지에 대한 정보를 갖고 있다.
	* 디렉토리의 위치에 대한 정보는 시작 블록과 마지막 블록만 갖고 있으면 된다.
	* **장점**
		* No External Fragmentation
		* sequence access에 적합하다.
	* **단점**
		* Direct-access 방식에는 비효율적이다.
		* 블록을 100% 파일을 위해 사용할 수 없다. 블록의 일정 부분은 다음 블록에 대한 정보를 저장하는데 사용해야하기 때문이다.
		* 첫번째 블록이 손실되면 뒤의 파일을 모두 사용하지 못하는 위험성이 존재한다.
	* **FAT (File Allocation Table)**
		* FAT는 link만 따로 모아둔 테이블이다. 테이블만 메모리로 옮겨서 사용할 수 있으므로, 메모리에서 특정 블록의 위치를 빠른 시간 안에 찾아내고, disk 에서는 한번에 접근할 수 있다.
		
* **Indexed Allocation** (paging 과 유사, inode)
	* 어떤 공간 자체를 indexing 하기 위한 정보만을 담아놓는 디스크 블록으로 하나 할당해 주는 것이다. (index block)
	* 디렉토리는 앞서 설명했던 start, length가 아닌파일에 대한 인덱스 블록에 대한 정보만 갖고 있으면 된다.
	* **장점**
		* No External Fragmentation
		* Direct access 쉽게 할 수 있다.
	* **단점**
		* index table도 공간을 차지하기에 공간적 효율성이 떨어진다.
		* Index block의 크기 결정이 중요한 관점이 될 수 있다. 인덱스 크기가 너무 커질 때의 구현 방법은? `Mapping`
			* Linked Scheme : Linked block의 공간이 부족하면, 마지막의 주소는 다음 블록을 가리킨다.
			* Two-level index : root는 다음 인덱스 블록에 대한 주소만 담고 있다. 그 주소로 이동하면 또 새로운 블록이 나타나는 방법이다.
			* Combined Scheme : 작은 파일은 Direct block 사용하고 큰 파일은 Indirect(Indexed) block을 사용하는 것이다.

### Access Performance for Allocation Methods
* Performance 기준
	* 빠른 것
	* 공간 효율성
* **Contiguous Allocation** : 접근은 한 번만 하므로 access time이 매우 짧고 Sequential/Direct Access에 적합하다. 그러나 external fragmentation 때문에 공간 효율성이 좋지않다.
* **Linked Allocation** : sequential access에는 좋지만 direct access엔 안 좋다.
* **Indexed Allocation** : index가 메모리에 있으면 Sequential/Direct Access에 적합하다. 메모리에 있지 않다면, 여러번 왔다갔다 해야하므로 느리다.
* 작은 파일에 있어서는 Contiguous Allocation을 하다가, 커지면 Indexed 로 바꾸는 방법도 있다.

## Free-Space Management
* Disk space에 우리가 사용할 수 있는 공간을 관리하기 위해서는 free-space list 정보, 즉 사용할 수 있는 블록에 대한 정보를 갖고 있어야 한다.
* 구현 방법
	* Bit Vector : 각 블록에 대해서 사용할 수 있는지 없는지를 0,1로 나타내는 것
	* Linked List : 빈 공간 자체를 Linked List 방식으로 구현하는 것

### Bit Vector (n blocks)
* n 개의 블록이 storage에 있다고 하면, n개의 bit로 해당 블록이 비어있는지 표현하는 것이다.
* 0 : block[i] is free
* 1 : block[i] allocated
* ex. 0001101011010
* **단점**
	* Bit map 자체도 별도의 공간이 필요하다.
* **장점**
	* Contiguous 한 free block을 찾는 것이 매우 간단하다.

### Linked List
* Linked allocation과 같은 방식으로, Free-space List를 서로 링크를 거는 것이다.
* **단점**
	* traversing 이 느리다.
* **장점**
	* 어차피 사용하지 않는 블록만 이용하므로, 공간이 낭비되지 않는다.
	* Contiguous free block을 찾기가 어렵다.
	
## Protection
* **File Protection은 접근 하는 것에 대한 권한을 주는 것**이다. 
* Controlled Access : 무엇을 할 수 있게, 누구한테 권한을 줄 것이냐?
	* Read, Write, Execute, Append, Delete, List…
	* Mode of access : read, write, execute (rwx)
	* Owner(파일을 만든 사람), Group(몇몇 사람들), Universe (모든 사람)
	* user 각각에게 각각의 mode를 따로 설정해줄 수 있다.
* Access List : rwx|rwx|rwx 순서대로 owner, group, universe
* ex. -rw-rw-r— , drwx——— (d는 디렉토리라는 뜻, 무시), -rw-r—r— …

## Efficiency and Performance
* 빨라야 되고, 공간 낭비를 적게하는 것이 좋다.
* 메인 메모리와 디스크는 속도 차이가 엄청 크다.
* **Improving Performance**
	* Buffer Cache / Page Cache
	* Synchronous / Asynchronous writes
	* Free-behind / read-ahead

### Buffer Cache
* Disk 관점에서는 DRAM이 Cache이다.
* **Buffer Cache는 블록을 메모리에 복사해두는 것**이다.

### Page Cache
* **Page Cache는 파일에 있는 내용을 주소를 줘서 페이지로 Caching 하는 것**이다.

### I/O without a unified Buffer Cache
* memory-mapped I/O 할 때는 Page cache - buffer cache - file system 순서
* 나머지 I/O 는 buffer cache-file system 순으로 찾아본다.
* 이처럼 같은 내용을 담는 Cache가 2개 있는 것을 **Double caching**이라 한다.
* 요즘에는 buffer cache를 없애고 Page cache로 많이 사용하고, buffer cache가 Page cache의 일부분을 사용한다.
* 두 개의 캐쉬를 하나로 통합한 것 : **unified buffer cache**

### Synchronous Writes
* 두 개의 매체가 있을 때, Write 작업이 끝났다는 것을 확인한 뒤 다음 단계로 넘어가는 것이 synchronous 라 한다.
* **synchronous 가 안정성이 더 높다.**

### Asynchronous Writes
* Write 작업 명령을 내린 뒤, 기다리지 않고 다른 일을 하고 있다가, 작업이 끝나면 알림을 받는 것을 asynchronous 라 한다.
* **asynchronous는 데이터의 일관성이 동기화 되지 않고 시간적 차이가 있지만 읽고 쓰는 속도 자체를 빠르게 할 수 있다.**

### Page Replacement Algorithms
* sequential access를 할 때, LRU는 좋지 않다. 

### Free-behind
* 내가 현재 n번 페이지를 사용하면 n-1번 페이지를 지우는 것이다.

### Read-ahead
* 내가 현재 n번 페이지를 사용하면 그 다음에 읽을 페이지 (n+1)를 미리 불러오는 것이다.

### Virtual File System
* VFS는 system call 로 파일을 다룰 때, 여러 개의 파일 시스템이 공존하고 있어도 user가 어떤 명령어를 입력하면 **OS가 각각의 파일 시스템에 맞게 명령어를 변환** 해서 구동시키는 것이다.

### Reliability
* File system은 결국 파일이 storage에서 memory로 올라가서 작업을 하고 다시 storage에 저장되는 것이다.
* 따라서 **이 두 개체 사이에 consistency가 맞아야 한다.**
* **항상 Reliability 를 고려해서 File system을 구현해야 한다.**

### Log strutted file system
* File을 write 할 때, 별도의 로그를 남겨두는 것이다.
* Journaling file system

### Sun network file system (NFS)
* 다른 PC의 디렉토리를 내 PC의 디렉토리에 붙이는 것이다.
* 둘은 network 로 연결되어 있기 때문에 network file system이라 한다.
