# Deadlocks
* Multiprogramming을 위해 Process 개념 도입 ⇒ 마치 동시에 수행하는 것처럼  작업 수행
* 데이터 공유할 수 없는 문제 생김 ⇒ [스레드 (Thread)](https://github.com/2017100898/TIL/blob/main/OS/thread.md) 등장
* Thread 데이터 공간 공유하다보니까 데이터 불일치 현상 발생 ⇒ [동기화 (Synchronization)](https://github.com/2017100898/TIL/blob/main/OS/synchronization.md) 기법  등장
* 동기화 ⇒ Critical section ⇒ 하나의 작업만 들어갈 수 있도록 함 ⇒ deadlock 문제 발생
* **deadlock은 매우 중요한 문제다.**

## Deadlock Concept
### Deadlock Problems
* example 1 
	* P0이 A를 갖고 있고 B를 기다리는 상황
	* P1이 B를 갖고 있고 A를 기다리는 상황
* example 2
	* P1이 disk drive 점령 중, 반납하기 위해 network card 필요
	* P2이 network card 점령 중, 반납하기 위해 disk drive 필요

### Dining-Philosophers Problem
* 5명의 철학자들이 원탁에 앉아 있을 때, 중간에 메인 요리가 있다고 하자.
* 철학자 사이 사이에 포크가 5개가 있고, 철학자는 밥을 먹기 위해 자신의 양쪽에 있는 포크 두 개를 잡아야 한다.
* 철학자는 생각하거나 밥을 먹거나 둘 중에 한 행위만 가능하다.

```cpp
do{
	wait(forks[i]);
	wait(forks[(i+1)%5]);
	//eat
	signal(forks[i]);
	signal(forks[(i+1)%5]);
	//think
} while(TRUE);
```

* 모든 철학자가 동시에 밥을 먹기 시작하며, 왼쪽 포크를 먼저 집었을 때, 모든 철학자는 오른쪽 포크를 잡지 못 하는 문제 발생.  ⇒ 무한히 기다려야 한다.
* OS는 이런 상황을 해결해줘야할 필요가 있다.
* **Deadlock Prevention** : 아예 이런 상황 발생하지 못 하도록 OS 설계하는 것
* **Deadlock Avoidance** :  회피하는 알고리즘, 그때 돼서 조치 취하는 것

##  System Model
* Prevention과 Avoidance를 하기 위해서, **시스템 자체에 대한 상태를 직관적으로 분석**하기 위해서 System model 사용한다.
* System Model: **Process, resource의 상태를 그래프로 표현한 것**
* Physical resource types: I/O devices, memory space, CPU cycles
* Logical resource types: semaphores, mutex locks, and files
* **resource type** : resource가 무슨 종류냐? (printer)
* **Instance** : 같은 resource 타입 몇 개가 있느냐? (printer 3개)
* Process는 resource type에게 자원 요청한다.  어떤 printer를 쓰냐는 상관 X
* 상관이 있어야 할 땐 각각의 resource type, 각각의 instance로 정의해둘 수 있음.
* **request** : 자원 요청 (system call)
	* open(), malloc(), wait(), acquire()
* use
* **release** : 자원 다 썼다! (system call)
	* close(), free(), signal(), release()
* 내가 지금 자원을 사용할 수 없으면 wait() 상태에 머무름 - 절대로 깨어나지 못하는 상황이 deadlock

## Deadlock Characterization
* **4 필요조건 for deadlock** (이 중 하나만 만족시키지 못 하더라도 deadlock 발생 안 함)
	1. **Mutual Exclusion** : 자원 사용 중일 때 다른 작업은 그 자원 사용 불가
	2. **Hold and wait** : 무언가를 갖고 있는 상태에서 다른 것을 기다린다
	3. **No preemption** : 강제로 다른 프로세스가 자원 가질 수 없을 때
	4. **Circular wait** : P0 -> P1 -> P2 -> PN -> … -> P0 서로 기다리는 관계 

### Resource-Allocation Graph
<img width="300" src="https://user-images.githubusercontent.com/64299475/138082494-7f3a2a18-bac1-49bb-8d6c-bad27df5adce.png">

* Process, Resource type, instance을 이용해서 상황 나타내는 것
* P1은 R2 리소스 할당 받음.  R2는 인스턴스 2개. R1에 request.
* P2는 R1, R2 갖고 있고 R3 request.
* P3는 R3 갖고 있음.
* Mutual Exclusion : O (가정)
* Hold and wait : O (자원 갖고 있는 상태에서 자원 요청)
* No preemption : O (가정)
* Circular wait :  X (화살표 따라갔을 때 Circular 형태)
* 만약 P3가 R2요청했을 때는 Circular wait 이므로 Deadlock 상황이라고 얘기할 수 있다.
* Circular wait에 포함되어있는 resource 의 instance가 여러개면 deadlock이 여러개가 될 수 있음.
* **no cycle -> not deadlock**
* **cycle -> 1 instance -> deadlock**
* **cycle -> n instance -> deadlock / not deadlock**
	* 그러나 어떻게든 deadlock 걸리지 않는 것이 목적이기 때문에 cycle 만들지 않는 것이 중요하다.

## Methods for Handling Deadlocks
* Deadlock Prevention : Deadlock이 절대 생기지 않도록 하는 것
* Deadlock Avoidance : Deadlock 발생할 것 같으면 조치 취하는 것
* Deadlock Detection : Deadlock의 사후 처리 (Deadlock 발견)
* Deadlock Recovery : Deadlock의 원상복귀
* 현재의 OS들은 Deadlock을 **무시**하고 없는 것처럼 동작한다. `Ostrich Algorithm`

### Deadlock Prevention
* Deadlock이 절대 생기지 않도록 하는 것.
* **4 Conditions 중에 한 가지만이라도 성립하지 않도록 함.**
	* No Mutual Exclusion? 현실적으로 실현가능성 없다.
	* No Hold and Wait? 
		* Total allocation : resource 쉬게 되는 현상 발생
		* Low resource utilization, Starvation 발생할 수 있음
	* Allow Preemptive? 출력하고 있는데 다른 Process가 뺏으면 문제 발생
		* Critical Section : atomic, 한 번에 실행하는 것 보장하기 위함인데 다른 Process가 뺏으면 문제 발생함
	* **No Circular wait? 가능**
		* resource 마다 번호를 줘서 Hold, request 할 때 **내가 갖고 있는 resource 보다 높은 번호만 request할 수 있다는 조건** 걸면 circular 발생하지 않음.

### Deadlock Avoidance 🐢
* Deadlock을 회피하기 위해서는 추가적인 정보가 필요하다.
	* CPU 스케쥴링 할 때 Burst time 예측해서 부여하는 것처럼, **Process가 어떤 Resource를 몇 개나 사용할지 알고있다고 가정 후 Deadlock Avoidance를 구현**한다.
	* `ex. P1은 2개의 hard disk를 사용할 것이다.`
	* Circular-wait을 절대로 발생하지 않도록 만드는 것이 목적이다.
* 자원의 요청이 왔을 때, **Deadlock 발생할 것 같으면** 허용하지 않는다.

#### System Model
* **State** (resource 배분에 대한 상태)
	* Available : 사용 가능한 resource 몇 개인가?
	* Allocated : 이미 할당된 resource 몇 개인가?
	* Needed : 프로세스마다 몇 개가 더 필요한가?
* _OS는 모든 현재 상태를 다 알고 있다고 가정한다._
* Worst case를 기준으로 한다.
	* Worst case: Process가 필요한 만큼 다 가져야 된다고 가정한다.
	* Maximum 충족되지 않으면 Process 끝나지 않는다고 가정한다. `Non-preemptive`
	* request - use - release
	
####  Safe Sequence🥕
* **Safe** : Deadlock이 절대 발생할 수 없는 방법이 **적어도 1가지 이상 있는 상황**  `at time interval`
	* `계속해서 Safe State를 유지하게끔 자원을 할당하자!`
* **Safe Sequence** : Deadlock 없이 끝낼 수 있는 실행 순서
* Unsafe state : Deadlock에 빠질 수도, 빠지지 않을 수도 있는 상황이며, 고려하지 않아도 된다.

#### METHODS
* **Resource-Allocation Graph**
	* **Claim** : request가 되는지 확인**만** 하는 절차
	* 단일 그래프에서는 Cycle이 발생하면 100% Deadlock이다.
	* 따라서, request로 Cycle 형성되기 전에 Claim으로 각각의 상황을 시뮬레이션 해보고 판단한다.
* **Banker’s algorithm**
	* Instance가 여러 개인 경우에 적용하는 알고리즘이다.
	* 어떤 프로세스가 자원 요청하면 할당될 때까지 기다려야 한다.
	* 2개의 서브 알고리즘으로 이뤄져 있다.
		* **Safety algorithm** : Safe Sequence 가 존재하는지 찾는 것
		* **Resource-Request algorithm** : 어떤 request 왔을 때 resource 줬다고 가정하고, 시뮬레이션을 해보는 알고리즘
	
> n = number of process  
> m = number of resources types  
> Available : 사용가능한 갯수 (m vector로 표현)  
> Max : maximum으로 사용할 수 있는 값 (nxm 표로 표현)  
> Allocation:  모든 프로세스마다 현재 할당 받은 갯수 (nxm 표로 표현)  
> Need : 프로세스마다 필요한 자원 개수 (nxm 표로 표현)  

#### Safety Algorithm
1. 각 프로세스마다 Finish 값을 만든다.
2. **Finish==False인 것 중에서 Need ≤ Work**가 있는지 찾는다. 즉 끝낼 수 있는 Process가 있는지 찾는다.  못 찾으면 Deadlock
3. 찾으면 **Work = Work + Allocation**, **Finish = True**
4. 모든 프로세스에 대해 2-3 단계를 반복하면 System이 Safe state라고 판단한다. 반복하지 못 하면 unsafe 라고 판단한다.

#### Resource Request Algorithm
<img width="300" src="https://user-images.githubusercontent.com/64299475/140618592-a05ac6a5-6bcb-496d-9360-6e23ffe8a7b1.png">

* 먼저 **Request ≤ Need**인지 확인한다.
* 이어서 **Request ≤ Available** 인지 확인한다.
* Request를 수용했다고 가정하고,  `Available = Available - Request` , `Allocation = Allocation + Request`, `Need = Need - Request` 를 시행한 뒤, 이 상황도 여전히 Safe한지 판단한다.

### Deadlock Detection
* Wait-for-graph를 통해서 Deadlock 을 탐지한다.
* Instance (Resource)를 제외하고 Process 끼리의 상황을 그래프로 나타내서 Cycle이 생기는지 판단한다.
* Algorithm을 자주 돌리면 Overhead가 크다.
* 반대로 자주 하지 않으면 어떤 프로세스로 인해 Deadlock이 발생했는지 알기가 어렵다.

### Recovery from Deadlock
* **Process Termination**
	* 엉킨 프로세스를 종료시킴으로써 Deadlock을 없앤다.
	* 이는 간단하지만 손실이 크다. 따라서 부분적으로 하나씩 종료시킬 수도 있다. `Partial Termination`
	* 이때, 비용이 적은 프로세스를 타겟을 먼저 종료시킬 수도 있다.
* **Resource Preemption**
	* Resource를 뺏어서 다른 프로세스에 할당한다.



