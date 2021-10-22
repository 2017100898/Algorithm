# Synchronization (동기화)
* 프로세스, 스레드 협동 시 데이터 공유 ⇒ 문제 발생 ⇒ 해결 방법은 동기화

## Background
* 주된 원인 : resource sharing - IPC, multithreads, multiprogramming
* ex1. ATM 문제: 두 프로세스 동시에 일어나면 각각 갖고 있는 데이터 달라질 수 있다.
* ex2. producer-consumer 문제
	* producer : 데이터 계속 쓰는 것
	* consumer : 데이터 계속 받아가는 것
	* 꽉 찼는데 producer가 계속 쓸 수도 있고 데이터가 비었는데 consumer가 데이터 받아가려 할 수도 있다.
	
### Race condition
* producer 와 consumer는 코드상으로는 문제가 없는 것 같아도 동시 실행 과정에서 문제 발생할 수 있다. **코드는 내가 원하는 순서로 동작한다는 보장이 없고, context switching 언제 일어날지 모른다.**
* **Race condition**: 내가 원하는 곳까지 가지 않고 그 전에 context switching 일어날 수 있고, 따라서 내가 원하는 값과 결과값이 다르게 나올 수 있다.
* 우리가 코드를 짤 때는 불확실성을 제거 해야 한다.
* 방법: **critical section에 대하여 mutually exclusive access를 보장하면 된다.**
	* mutually exclusive access: 상호배제, 내가 있으면 다른 것 못 들어오게 막는 것.

## Critical Section Problem
* 프로세스들이 여러개가 있고 데이터 공유가 있다고 했을 때, critical section은 **코드의 일부**를 뜻 한다.
* shared data가 있다고 해서 반드시 critical section은 아니지만, **문제가 될 수 있는 부분이라면 critical section이 될 수 있다.**
* 내가 critical section을 실행하고 있으면 다른 프로세스나 스레드가 해당 변수에 관해 실행을 못 하도록 보호한다.
* critical section **앞 뒤에 입구와 출구를 만들어서** 내가 들어가면 다른 프로세스 접근 못 하도록 만들 수 있음.

```cpp
do{
	[entry section]
		critical section
	[exit section]
		remainder section
} while(true);
```

### critical section에 대해 보장해야하는 것
1. **Mutual Exclusion**
	* 하나의 자원에 단 하나의 프로세스만 입장하도록 해야 한다.
2. **Progress**
	* critical section에 아무도 없으면 들어갈 수 있어야 한다. (deadlock free)
3. **Bounded Waiting**
	* critical section 기다리고 있으면 언젠가는 들어갈 수 있어야 하며, **평생 기다리면 안 된다.(starvation free)**
	
## Software C.S :  Peterson’s Solution
* 알고리즘으로 코드로 구현하는 것.

### Algorithm 1
* Consider two Pi , i = {1,2}

#### Process P1
```cpp
do{
	wants[1] = true;
	while(wants[2]){;}
		critical section
	wants[1] = false;
		remainder section
} while(true);
```

#### Process P2
```cpp
do{
	wants[2] = true;
	while(wants[1]){;}
		critical section
	wants[2] = false;
		remainder section
} while(true);
```

* 위 방식대로 되면, critical section 비어있을 때도 둘 다 True가 되어서 둘 다 기다리는 상황 발생할 수 있다.
* **int not_turn 이라는 변수를 만들어서 둘 중 하나는 반드시 실행되도록 만들 수 있다.** `wants[j] && not_turn == i`
* 둘 다 critical section에 들어가는 일은 없으므로 Mutual exclusion 하다.
* Peterson’s algorithm은 느리고 비싸다. 즉, 자원의 소모가 많으며 2개의 프로세스에 대해서만 작동하는 단점을 지닌다.

## Hardware C.S
* **lock을 이용한 방식** : 누가 들어가면 이용 못 함.
* **Atomic** : 여러 operation이 하나의 명령처럼 수행 된다.


### TestAndSet
* 시도해보고 설정한다.
* 설명을 위해 코드로 나타낸 것. 이 역할을 하는 하드웨어가 있다.

```cpp
lock = FALSE;

do{
	while(TestAndSet(&lock)){ //여기 지나면서 lock은 TRUE로 바뀜
	[CRITICAL SECTION]
	}
	lock = FALSE
	[REMAINDER SECTION]

} while(TRUE);

boolean TestAndSet(boolean *target){ 
	boolean rv = *target;
	*target = TRUE;
	return rv;
} //이것은 하나의 instruction으로 실행되기 때문에 실행 중 끊기는 일은 없음
```


입력변수|return 값|return후 변수
---|---|---
FALSE|FALSE|TRUE
TRUE|TRUE|TRUE

### Mutex Locks
```cpp
acquire(){ //key를 얻는다.
	while(!available)
		;
	avaiable = false;
}

release(){ //다 수행 했기때문에 key 돌려준다.
	available = true;
}

do{
	[acquire lock]
		critical section
	[release lock]
		remainder section
} while(TRUE);
```

* key를 얻고 반납하는 두 함수로 구성되어 있다.

### 구현
```cpp
#include <pthread.h>

pthread_mutex_t mutex;

/* create the mutex lock*/
pthread_mutex_init(&mutex, NULL);
/* acquire the mutex lock*/
pthread_mutex_lock?(&mutex);
/* critical section */
/* release the mutex lock */
pthread_mutex_unlock(&mutex);
```

### Busy waiting in Mutex
* 첫 번째 프로세스만 일단 지나가고 나머지는 while 문 실행 중...  계속해서 CPU 쓰고 있음 ⇒ **Busy waiting** (= spinlock)
* 자원 낭비의 단점 존재하지만, waiting state로 만들면, 언제 또 다시 CPU 할당 받을지 모르고 context switching 일어남. 금방 내 차례 오면 그냥 spinlock이 효율적.

## Semaphore
* Mutex와 유사하지만 **Multi개의 진입을 허용함.**
* wait()과 signal()로 이루어져있음.

```cpp
wait(S){ //S = 1
	while(S <= 0) //second process S=1 될때까지 기다림
		; //busy wait
	S--; // S = 0
}

Signal(S){
	S++; // S=1
}

do{
	wait(S);
	[Critical Section]
	signal(S);
	[Remainder Section]
} while(TRUE);
```

* Binary Semaphore :  0, 1 사용하는 자원 수가 1
* **Counting Semaphore** :  사용하는 자원 수가 2개 이상

### Semaphore with Block Operation
* **Avoid busy waiting**
* **block()** : 코드 사용할 수 없는 경우 waiting queue로 가서 대기, CPU 반납, signal 호출 시 모든 프로세스 ready queue로 간다.
* wakeup()

```cpp
wait(S){
	S.value--;
	if(S.value < 0){
		add this process to waiting queue
		block();
	}
}

signal(S){
	S.value++;
	if(S.value<=0){ //wait 하고 있는 Process가 있는지 판단
		remove a process P from the waiting queue
		wakeup(P);
	}
}
```

* S = 2 일 때, P1 이 지나가면 S=1, P2이 지나가면 S=0이다.
* P3은 S=-1, P4는 S=-2 이므로 S.value < 0 이 된다.
* P3와 P4는 waiting 상태로 들어가게 됨.
* signal 호출 시 S = -1이 된다. ⇒ **음수값은 지금 waiting queue에 있는 것이 있다는 뜻** ⇒  따라서 wakeup() 해줘야 함.

### 구현
```cpp
#include <semaphore.h>
sem_t sem;

/*Create the semaphore and initialize it to 1*/
sem_init(&sem, 0, 1);

/*acquire the semaphore*/
sem_wait(&sem);
/*critical section*/
/*release the semaphore*/
sem_post(&sem) //=signal
```

* **Problem 1 : Deadlocks and Starvation**
	* P0 은 P를 다 쓰고 S를 기다리고, P1은 S를 다 쓰고 P를 기다리고 있을 때 deadlock 발생.
* **Problem 2 : Priority Inversion (우선순위 역전)**
	* Process L , M , H 있다고 가정할 때, 우선순위는 L < M < H
	* L이 R갖고 있을 때, H가 wait(R) 중인데, M이 CPU 점령 중. L은 M보다 낮아서 실행 안 됨. 결국 H도 계속 기다림.
	* 해결하기 위해 *Prioirty-inheritance protocol* 사용
		* H가 wait(R)이면, L도 H로 바꿈. 
* **Problem 3 : Incorrect use of semaphores**
	* signal -> wait ?
		* 자원보다 더 들어오게 될 수 있다.
	* wait -> wait ?
		* S 감소만 시키고 deadlock 발생할 수 있다.

## Classic Problems of Synchronization
### Bounded-Buffer Problem 
* 공유버퍼문제, Producer-consumer problem
* Semaphore 써서 해결 가능하다.

> Semaphore mutex = 1  
> Semaphore full = 0 (차있는 크기)  
>  Semaphore empty = N (비어있는 크기)  

#### Producer process
```cpp
do{
	wait(empty); //empty--, 0이 아닐때만 내려감
	wait(mutex);
	[Critical Section]
	[add an item to buffer]

	signal(mutex);
	signal(full); //내가 쓴 것 full++
}while(TRUE);
```

#### consumer process
```cpp
do{
	wait(full); //full--, 0이 아닐때만 내려감
	wait(mutex);
	[Critical Section]
	[add an item to buffer]

	signal(mutex);
	signal(empty); //empty++
}while(TRUE);
```


### Readers-Writers Problem
* readers: update 하지 않는다.
* writers : 수정 가능하다.
* 문제: 읽는 것은 여러명이 동시에 해도 되지만 쓰는 것은 오직 한 사람만 가능하다.
* reader가 읽고 있으면 writer 접근 불가능
* writer 쓰고 있으면 reader 접근 불가능

> Semaphore wrt = 1  
> Semaphore mutex  = 1  
> int readcount = 0  

#### writer process
```cpp
do{
	wait(wrt);
	//writing is perfomed
	signal(wrt);
}while(TRUE);
```

#### reader process
```cpp
do{
	wait(mutex); //Critical section으로 만들기 위해 mutex 있음.
	readcount++;
	if(readcount == 1)
		wait(wrt); 
	signal(mutex); //Critical section으로 만들기 위해 mutex 있음.

	wait(mutex);
	readcount--;
	if(readcount == 0)
		signal(wrt); // 마지막 애는 wrt lock 해제 후 나감
	signal(mutex);
}while(TRUE);
```

