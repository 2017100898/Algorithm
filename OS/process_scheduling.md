# Process Scheduling
* long-term scheduling
* short-term scheduling
* 그래서, 누구에게 CPU를 할당할 것인가?

## Basic Concepts
* Multitasking: CPU가 프로세스 번갈아가면서 사용, 언제 어떤 프로세스 할당해 주느냐에 따라 효율 결정 됨.
* 대상이 프로세스든 스레드든 개념적으로 달라지는 것은 없다.

### CPU Scheduling
* ready queue 에 있는 프로세스들 중에서 누구에게 CPU 할당할 것이냐?를 결정하는 것
	* issue1: 누구에게 줄 것인가
	* issue2: 얼마나 오랫동안 할당할 것인가
* CPU Scheduler : 누구에게 CPU 할당할 것인지 **결정**하는 코드
* Dispatcher : 프로세스할 때 CPU **할당하는 것**
	1. context switching 해줌
	2. user mode 로 바꿔줌
	3. 프로세스 메모리에 해당 하는 주소로 점프, PC 셋팅

### CPU & I/O Bursts
* Bounded: 프로세스의 경향, 프로세스마다 정해지는 것 (CPU/IO)
* Bursts: 현재 CPU를 사용하느냐? I/O를 사용하느냐? 각각의 상황에 대해 왔다갔다 하는 것

> **CPU Burst time : CPU를 사용하는 시간**  

* Process execution 은 CPU와 I/O bursts 의 연속이다.


## Scheduling Criteria (기준)
* 목표: 시스템의 성능 향상
* 시스템의 성능?
	1. CPU 활용 - 떨어지지 않고 높게 유지되는 것이 good
	2. Throughput  - 같은 시간에 많은 일 수행하면 good
	3. Turnaround time (process) - 같은 일 수행 시간 짧으면 good
	4. **Waiting time** - ready queue에 머물러 있는 시간만 계산, 짧으면 good (일반적으로 많이 사용)
	5. response time - 클릭하고 처음으로 CPU 할당 받을 때까지의 시간 (1회), 짧으면 good
* 어떤 환경이냐에 따라 기준 정하는 것이 좋음 

### 성능평가
1. running -> waiting : 새로운 프로세스 dispatch 해야 함
2. running -> ready: dispatch 해도 되고 안 해도 됨 (새로운 프로세스 정해지 않아도 됨, 다시 ready -> running)
3. waiting -> ready :  dispatch 해도 되고 안 해도 됨 (새로운 프로세스 정해지 않아도 됨, 다시 ready -> running)
4. terminate :새로운 프로세스 dispatch 해야 함

## Preemptive vs Non-Preemptive 🐢
### Preemptive (= 빼앗는다, 쫓아낸다)
* 어떤 프로세스 CPU 할당 -> 프로세스가 반납하지 않아도 OS가 CPU 뺏을 수 있음
* 요즘에는 대부분 이 방식, 더욱 효율적
* Preemptive scheduling
	* 장점: Low response time
	* 단점: High context switch overhead, race conditions (실행되는 순서에 따라 결과값 달라지는 것)
* Immediately take care of Interrupts
* Use time-sharing

### Non-Preemptive
* 어떤 프로세스 CPU 할당 -> 프로세스가 반납하기 전까지 OS 기다릴 수 밖에 없음
* Non-Preemptive scheduling
	* 장점: Low context switch overhead
	* 단점: longer mean response time

## Scheduling Algorithms 🌈
* scheduling algorithm == policy
	* 무엇을 중요시 하느냐?
* Various algorithms
	* First-come, First-served : 선착순
	* shortest-job-first (SJF) : 짧은 것부터
		* shortest remain job first (SRJF) : 현재 시간 기준 남아있는 것중 빠른 것 (중간에 일이 생길 수 있음)
	* priority scheduling : 중요도, 우선순위
	* round-robin scheduling : 돌아가면서 차례대로
	* earliest deadline first scheduling : 급한 것부터

### First-come, First-served 
* Non-preemptive scheduling : 선점 불가
* ready queue에 먼저 들어온 것이 먼저 할당

> Process	CPU Burst Time  
> P1		24  
> P2		3  
> P3		3  

* Waiting time : P1 = 0, P2 = 24, P3 = 27
* Average waiting time : 17
* 들어온 시간에 따라 Average waiting time 달라질 수 있다.
* Not good for time-sharing systems: Non-preemptive이기 때문에 사용중인 프로세스 중지 불가하기 때문
* **Convoy Effect** : 앞에 있는 프로세스가 지연돼서 뒤에 있는 것들도 모두 지연되는 현상
	
### Shortest-Job-First (SJF)
> Process	CPU Burst Time  
> P1		6  
> P2		8  
> P3		7  
> P4		3  

* P4 - P1 - P3 - P2 순서
* Average waiting time : 7 (실행시간은 제외, Only wait time)
* **Non-preemptive SJF**
	* 실행 중인데, 나보다 짧은 애가 들어오더라도 **바꾸지 않는 것**
* **Preemptive SJF (= Shortest Remaining Time First)**
	* 실행 중인데, 나보다 짧은 애가 들어오면 **바꾸는 것**
	* **시간 비교 기준 : 원래의 내 시간 X 현재 남은 내 시간 O**
* **장점**
	* Average waiting time이 짧다.
	* ready queue가 빨리 줄어든다.
	* response 빠르다.
* **단점**
	* **Starvation (굶주림)**
		* 시간이 긴 Process는 계속해서 CPU 기다려야 함.
		* aging으로 해결 가능 - 오래 기다린 프로세스들 우선 순위 높여지는 것. 대기 시간에 따른 가중치.

#### CPU Burst Prediction
* CPU가 실행되기 전에 사용 시간을 어떻게 아냐?
* CPU time 은 **예측한 값**
	* 통계적 수치를 기반으로 함. (일정 범위 내, moving average)
	* Simple Moving Average : 모두 동일하게, n개의 평균의 연속
	* Weighted Moving Average : 값마다 weight 줌. 나눌 때도 weight 으로 나눔.
	* Exponential Moving Average : Weight 종류 중 하나, Weight을 Exp로 주겠다.


### Round-Robin (RR)
* Preemptive scheduling
* FIFO : ready queue에 먼저 들어온 프로세스가 CPU 먼저 사용하는 형식
* **Time quantum** : 하나의 프로세스마다 얼마만큼의 시간을 부여?
	* q를 길게 잡으면 FCFS와 다를 바가 없다.
	* q를 짧게 잡으면 Context switching time 시간 너무 많이 걸림
	* 10~100ms 정도로 잡는 것이 가장 좋음 (이때 context switch time: 10 microsec)
* **장점**
	* CPU 독점 방지
	* response time 짧다 (응답 중요한 시스템에서 잘 사용)
* **단점**
	* Context switching 하는 데에 시간을 많이 들일 수 있다.

> example ) Time Quantum = 4  
> 4초씩 사용 하고 (4보다 작은 것은 본인의 시간 만큼만) 반납 후 가장 뒤로 감  

#### Multilevel Queue
* Ready queue 2개 만들어서 각각의 Queue마다 CPU 수행되는 시간 먼저 할당한 뒤 queue마다 다른 스케쥴링 적용 가능. 


## Advanced Scheduling
### Multiple-Processor Scheduling
* CPU 내의 core가 늘어나면서, 스케쥴링 방법도 변함.
* **Affinity Scheduling**
	* 이전에 사용한 CPU 다시 사용하는 것
	* core/CPU 마다 cahce를 따로 쓰기 때문에 사용한 CPU 다시 사용하는 것이 효율적
* **Load balancing**
	* 사용할 수 있는 CPU 있으면, 내가 썼던 CPU 쓰려고 기다리는지 않고 작업 배분하는 것
	* Affinity Scheduling과 반대되는 개념
	* 적절히 조화되는 것이 좋음

#### Multicore Processors
* Hyper-Threading : 실제로는 **두 개 이상의 스레드 하나의 코어에 할당** 됨
* CPU 내부에서도 계산하는 unit (ALU) 말고도 cache들 있다.
	* 어떤 값 읽고 쓸 때 연산 장치 쉴 때가 있음. 모든 하드웨어가 쉬지 않도록 그동안 다른 thread 수행 함.
	
### Real-Time CPU Scheduling (실시간)
* RTOS : 정해진 시간 내 Job의 수행 완료가 보장되는 것
* time t: CPU burst time
* deadline d : 수행 보장 시간
* period p : 수행되는 빈도

> 예를 들어 전방 장애물 감지 스레드가 있을 때,  
> 1초마다 1번 씩 (p) 실행 되고, CPU 0.2초 소요 (t)되고  
> 0.8초 안에는(d) 반드시 실행 되어야 한다고 한다.  

#### Rate Monotonic Scheduling
* 자주 수행 되는 것에 우선권 주는 방법
* rate = 1/p : p가 짧아질 수록 rate 높아짐
* Shorter periods = higher priority
* Longer periods = lower priority
* 하지만 **t1+t2 > p1**일 때, deadline 판단 없이 Rate Monotonic Scheduling을 진행해서 **t2가 덜 실행 되었는데 다시 t1을 실행시키면, t2의 deadline이 초과할 수 있다.**

#### Earliest Deadline First Scheduling (EDF)
* period : p1 = 50, p2 = 80
* CPU burst : t1 = 25, t2 = 35
* 스케쥴링 해야하는 시점에서 누가 가장 deadline 급한지 판단, 그 프로세스한테 CPU할당하는 방법이다. 
*  **t1+t2 > p1**일 때, **t2의 deadline 급하면 p1 넘더라도 t2 실행시키는 방법.**