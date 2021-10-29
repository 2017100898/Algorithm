# Process
## Process Conecept
* **Process **는 프로그램과 다른 개념으로 **OS 관점에서의 job과 task** 이다. 프로그램이 실행되어 돌아가고 있는 동적인 상태를 뜻하며 OS로부터 메모리 할당 받는 작업의 단위이다.
* **Program**은 정적인 상태로 파일 시스템에 존재하는 실행파일(.exe)을 뜻한다. Program은 실행되지 않을 수 있다.
* **Processor**는 Hardware로 컴퓨터 운영을 위해 명령어들을 처리하는 논리회로다.  (CPU, GPU: Processor chip)

### Process in Memory
* hw1.cpp에서  hw1.exe로의 변환은 기계가 알아들을 수 있도록 단순 번역한 것이다. (0101000011) 
	* hw1.exe는 SSD 어딘가에 들어있다.
* 프로그램을 실행 시키면 DRAM (main memory) 에 공간 할당 받고 번역된 코드(명령어) 가 CPU로 복사돼서 올라간다.
	* 여기서 할당 받은 공간이 **Process Memory**다. 프로그램을 **실행할 때마다 별도의 메모리공간 할당 받아서 코드 복사 되고 작업 수행**한다. 처음에는 작은 메모리를 할당하고  필요 시 늘린다.

### Main Memory
<img height = 300, src="https://user-images.githubusercontent.com/64299475/138258192-58503c21-dac8-4ead-a653-c6ee81a7b107.png">

#### Kernel Memory
* 커널 영역은 시스템 운영에 필요한 메모리로, 운영체제가 올려져 있으며 유저는 함부로 커널 영역에 접근할 수 없다.

#### User Memory

* 유저 영역은 프로그램이 동작하기 위해 사용되는 메모리 공간을 뜻한다.

* **Text** : Program code가 들어가는 공간
* **Data** : 전역 변수가 들어가는 공간
* **Heap** : 동적할당이 들어가는 공간  `int *p = malloc(3000);`
* **Stack** : function에 관련된 모든 변수가 들어가는 공간

### Process Management
* 프로세스는 여러 개가 있기 때문에 관리를 해야 한다. 프로세스를 관리하기 위해 프로세스의 부가적인 설명을 관리하는 별도의 정보들의 집합이 필요하다. 
  * 이것이 **PCB (Process Control Block)** 이다.
  * PCB는 struct 처럼 Process State, Process number, Program counter, registers, memory limits, list of open files 등이 들어있다. 

### PCB
<img height = 300, src="https://user-images.githubusercontent.com/64299475/138258612-5c2942eb-65e8-46b8-9cb2-4c2c174252eb.jpg">

* PCB는 OS가 프로세스를 유지 및 관리하기 위해 갖고 있는 구조체다.
* Process State: running, ready, waiting, etc.
* Program counter (PC) : 다음 명령 주소

### Process State
* 좀더 효율적으로 프로세스를 관리하고 CPU 할당하기 위한 공간이다.
* **new** : 프로그램 클릭 시의 상태
* **ready** : CPU 할당 받을 수 있는 자격 있는 프로세스들 모여있는 곳
	* **ready queue** : queue 형태로 프로세스들이 기다리고 있다. CPU 기다리는 Process 들의 그룹이다.
	* _한 번에 ready 할 수 있는 프로세스의 수는 OS가 정한다._
* **running** : 실행되고 있는 프로세스
* **waiting** : ready queue에 들어가지 못 하고 기다리고 있는 것
	* CPU를 줘도 작업을 수행하지 못 하는 프로세스들은 wait 상태에 머무른다.
* **terminated** : 끝나고 나가는 것
* I/O device queue : 모든 device 마다 queue가 다 있다. device 할당 받을 때까지 queue에서 기다린다.

## Process Scheduling
> Ready queue에 있는 프로세스들 중에 어떤 프로세스를 **Dispatch** (CPU 할당) 할지 결정하는 코드를 뜻한다.

* [Process Scheduling](https://github.com/2017100898/TIL/blob/main/OS/process_scheduling.md)은 CPU 할당 및 New에서 Ready로 가도록 스케쥴링 하는 것이다.
* **concurrently**이란, 우리가 느끼기에 동시에 실행되는 것으로, 실제로는 CPU가 한 번에 처리할 수 있는 것은 하나의 프로세스 뿐이다.
* **parallel**은 실제로 CPU core에서 동시에 실행되는 것을 말한다.
* **context switch**는 CPU가 프로세스 할당 받아서 사용하다가 다른 프로세스가 CPU를 할당 받도록 하는 프로그램을 뜻한다.
	* context switch를 너무 자주하면 context switch 하는 것만으로도 시간이 많이 소요된다.
* Multiprogramming의 목적은 CPU가 놀지 않게 하는 것이다.
	* Time-sharing : 시간 나눠서 프로세스 선택하는 것

### Type
<img height = 200, src="https://user-images.githubusercontent.com/64299475/138259286-983938ac-1cdd-438d-a7c3-da98a8d28035.png">


#### Long-term Scheduler (or job scheduler)
* **어떤 프로세스를 ready queue에 넣어줄 것인지** 를 결정하는 것이다. 
* ready queue에 들어가는 순간 메모리 할당되고 주소값 받는다. 이때부터 실질적인 프로세스라고 볼 수 있으나 잘 쓰지 않는다.
* **프로세스를 적절히 섞어주는 것이 long-term scheduler의 역할**이다.
	* **I/O bound process** : device 많이 쓰는 프로세스
	* **CPU bound process** : 계산 많이 하는 프로세스
#### Short-term Scheduler (or CPU scheduler)
* **ready queue 내의 수많은 프로세스 중 누가 다음 번에 CPU 사용할 것인지**를 결정하는 것이다.

## Operations on Processes
### Process는 어떻게 만들어지는가?
* **프로세스는 다른 프로세스가 만든다.** Process는 다른 프로세스를 **만들 수도, 지울 수도** 있다.
* **부모 프로세스는 자기의 프로세스를 그대로 복사해서  트리구조로 자식 프로세스를 만든다.**
	* 이러한 구조는 관리하기에 굉장히 용이하다.
	* 최초의 프로세스는 init process다. 부팅 시 init process 밑으로 굉장히 다양한 자식 프로세스가 생성 된다.
* 부모는 자식 프로세스를 **fork()** 명령으로 만들어 낸다.  `fork() -> exec() system call`
	* fork() 하는 순간 메모리가 그대로 복사 된다.
	* 그대로 복사되면 똑같은 일을 하는 것이 2개 생기고 다른 일을 할 수가 없을까?
		* **복사 되고 나서 pid(process identifier) 값은 서로 달라진다.** pid는 fork에 대한 return 값을 뜻한다.
		* 부모는 자식 프로세스의 pid를 받고 대기하며, **자식 프로세스는 pid 가 0가 된다.**
		* **pid == 0 이면 새롭게 다른 코드를 갖고 와서 실행해야 한다.**
		* 부모가 죽으면 자식도 죽는다. 부모가 자식 끝날 때까지 기다린다. -  `wait`
		* 부모가 자식 프로세스 죽일 수 있다. - `kill`
		

![image](https://user-images.githubusercontent.com/64299475/136413514-4430349a-f9cc-4550-85f9-1094e7ee74bf.jpeg)

### Question1
```c
#include <stdio.h>
#include <unistd.h>
int main()
{
   /* fork a child process */
   fork();

   /* fork another child process */
   fork();

   /* and fork another */
   fork();

   return 0;
}
```

* 총 몇 개의 프로세스가 만들어지는가?
	* **총 8개의 프로세스** 만들어졌다가 종료된다.

### Question2
<img width="300" alt="image" src="https://user-images.githubusercontent.com/64299475/136414757-76c73a10-2f44-4a3d-8afb-39e603afa5e8.png">

* pid of parent and child are **2600 and 2603**
* fork()가 실행되면서,
	* A : 자식의 pid == 0 
	* B : 자식의 pid1 == 2603 `getpid()`
	* C : 부모의 pid == 2603
	* D : 부모의 pid1 == 2600 `getpid()`

### Question3
<img width="300" alt="image" src="https://user-images.githubusercontent.com/64299475/136416078-d08bc7fe-ec4e-43e9-838f-d7a2829e94f5.png">

* 전역변수는 data에 들어간다.
* fork() 하면서 자식 프로세스 그대로 복사 한다.
* 부모 입장에서는 wait 실행한다.
* 자식 입장에서는 자신의 value+=15 실행한다.

> 결과값  
> parent : 5  
> child : 20

## Interprocess Communication (IPC)
* 프로세스가 여러 개 있을 때는, `다른 프로세스로부터의 침범` 문제가 생길 수 있다.
	* 이 문제를 해결 하도록 **할당받은 공간 외에 사용하지 못 하도록** 만든다. (protection)
	* 하지만 이러한 대처는 **다른 프로세스에게 데이터 전송 못 하는 새로운 문제 발생**한다.
	* 따라서 문제를 해결하기 위해 `interprocess communication (IPC)` 를 제공한다. IPC는 프로세스 간 통신을 뜻하며 호출해서 사용할 수 있고 관리는 OS가 한다.

### Communications Models
<img width="400" alt="image" src="https://user-images.githubusercontent.com/64299475/136418152-07e32483-79aa-45d1-85d3-37f38ec5f5f4.png">

#### Shared Memory
* **두 개의 프로세스 공간이 아닌 별도의 User space 제공**한다. User space에서 읽고 쓰는 것이 가능하다.
* **Producer-consumer problem**
	* Producer: 공간에 정보 제공하는 것
	* Consumer: 정보 가져가는 것
	* 메모리는 비어있을 수 없고 항상 어떤 값으로 가득 차 있기 때문에 **내가 아무것도 안써도 Consumer는 끊임없이 가져갈 수 있다. 반대로 Consumer가 아직 안 읽었는데 데이터를 덮어쓸 수도 있다.** (circular queue)
	* 이 문제 해결하기 위해 [`Synchronization`](https://github.com/2017100898/TIL/blob/main/OS/synchronization.md) 가 도입 되었다.
	
#### Message Passing
* 보낼 Message있으면 OS 공간에 저장해놨다가 요청 시 **택배처럼 전해준다.**
	* Microkernel structure 가 많이 쓴다.

#### Synchronization (동기화)
* **동기화**란 항상 데이터가 일관적으로 유지되는 것이다. Buffer에 in, out을 만들어서 _다 썼는지_ 그리고 _다 읽었는지_ 판단할 수 있다.
* **Blocking** : 끝난 것을 확인할 때까지 기다리는 것
* **Non-blocking** : 기다리지 않으며 주면 끝나는 것
