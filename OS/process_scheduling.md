# Process Scheduling
<img height="200" src="https://user-images.githubusercontent.com/64299475/138259286-983938ac-1cdd-438d-a7c3-da98a8d28035.png">

* Process Scheduling에는 long-term scheduling과 short-term scheduling이 있다.
* 중요한 논제는 **그래서, 누구에게 CPU를 할당할 것인가?** 이다.

## Basic Concepts
### Multitasking
* CPU는 프로세스 번갈아가면서 사용한다. **언제 어떤 프로세스 할당해 주느냐에 따라서 효율이 결정** 된다.
* 할당하는 대상이 *프로세스든 스레드든* 개념적으로 달라지는 것은 없다.

### CPU Scheduling
* **ready queue에 있는 프로세스들 중에서 누구에게 CPU 할당할 것인지**를 결정하는 것
	* **Issue1: 누구에게 줄 것인가?**
	* **Issue2: 얼마나 오랫동안 할당할 것인가?**
* CPU Scheduler : 누구에게 CPU 할당할 것인지 **결정**하는 코드
* **Dispatcher** : 프로세스한테 CPU **할당하는 것**
	1. context switching 해준다.
	2. user mode 로 바꿔준다.
	3. 프로세스 메모리에 해당 하는 주소로 점프하고 PC setting한다.

### CPU & I/O Bursts
* **Bounded**는 프로세스의 경향, 프로세스마다 정해지는 것이다. (CPU/IO)
* **Bursts**는 현재 CPU를 사용하느냐? I/O를 사용하느냐? 각각의 상황에 대해 왔다갔다 하는 것이다.

> **CPU Burst time : CPU를 사용하는 시간**  

* *Process execution 은 CPU와 I/O bursts 의 연속이다.*


## Scheduling Criteria (기준)

* 스케쥴링의 목표는 **시스템의 성능 향상**이다.
* **시스템 성능의 기준**
	1. CPU 활용 : 떨어지지 않고 높게 유지되는 것이 good.
	2. Throughput : 같은 시간에 많은 일 수행하면 good.
	3. Turnaround time (process) : 같은 일을 함에 있어 수행 시간 짧으면 good.
	4. **Waiting time** : ready queue에 머물러 있는 시간만 계산해서 짧으면 good (일반적으로 많이 사용된다.)
	5. response time : 클릭하고 처음으로 CPU 할당 받을 때까지의 시간 (1회), 짧으면 good
* 어떤 환경인지에 따라 기준 정하는 것이 좋다.

### Process and State Transition
<img width="500" src="https://user-images.githubusercontent.com/64299475/138409958-b0e58c60-801c-4fa1-9a0e-111a553a6760.png">

> Ready queue에 있는 프로세스들 중에 어떤 프로세스를 **Dispatch** (CPU 할당) 할지 결정하는 코드 (OS module) 

1. **running ⇒ waiting** : 새로운 프로세스 dispatch 해야 한다. (CPU가 비었기 때문)
2. running  ⇒ ready: dispatch 해도 되고 안 해도 된다. (필수가 아니라는 뜻으로, 새로운 프로세스 반드시 정해지 않아도 되고 해당 노드를 빼지 않고 다시 ready  ⇒  running 가능하다.)
3. waiting  ⇒ ready :  dispatch 해도 되고 안 해도 된다. (필수가 아니라는 뜻으로, 해당 프로세스가 반드시 CPU 써야하는 것 아니면 일단 기다리고 있어도 된다.)
4. **terminate** : 새로운 프로세스 dispatch 해야 한다.

## Preemptive vs Non-Preemptive 🐢
### Preemptive (= 빼앗는다, 쫓아낸다)
* 어떤 프로세스에 CPU를 할당한 뒤, 그 프로세스가 반납하지 않아도 OS가 CPU 뺏을 수 있다.
* 요즘에는 대부분 이 방식을 사용하며 더욱 효율적이다.
* Preemptive scheduling
	* 장점: Low response time
	* 단점: High context switch overhead, race conditions (실행되는 순서에 따라 결과값 달라지는 것)
* Interrupts를 즉시 처리한다.
* time-sharing을 사용한다.

### Non-Preemptive
* 어떤 프로세스에 CPU를 할당하면 그 프로세스가 반납하기 전까지 OS 기다릴 수 밖에 없다.
* Non-Preemptive scheduling
	* 장점: Low context switch overhead
	* 단점: longer mean response time

## Scheduling Algorithms 🌈
* scheduling algorithm는 *policy*이다.
	* 무엇을 중요시 하느냐에 따라 처리 순서가 달라진다. 
* Various algorithms
	* First-come, First-served : 선착순으로 처리하는 방법
	* shortest-job-first (SJF) : 짧은 것부터 처리하는 방법
		* shortest remain job first (SRJF) : 현재 시간 기준 남아있는 것 중 빠른 것부터 처리하는 방법
	* priority scheduling : 중요도, 우선순위에 따라 처리하는 방법
	* round-robin scheduling : 돌아가면서 차례대로 처리하는 방법
	* earliest deadline first scheduling : 급한 것부터 처리하는 스케쥴링 방법

### ✔️ First-come, First-served 
* Non-preemptive scheduling : 선점이 불가하다.
* **ready queue에 먼저 들어온 것이 먼저 할당되는 방법**이다.

|Process|CPU Burst Time|
-----|----
|P1		|24|
|P2		|3  |
|P3		|3  |

> Waiting time : P1 = 0, P2 = 24, P3 = 27  
> Average waiting time : 17
* **들어온 시간에 따라 Average waiting time 달라질 수 있다.**
* Non-preemptive이기 때문에 사용중인 프로세스 중지 불가하기 때문에 time-sharing systems에는 적합하지 않다.
* 앞에 있는 프로세스가 지연 돼서 뒤에 있는 것들도 모두 지연되는 **Convoy Effect**가 발생할 수 있다.
### ✔️ Shortest-Job-First (SJF)

|Process|CPU Burst Time|
-----|----
|P1		|6	|
|P2		|8  |
|P3		|7  |
|P4		|3  |

> P4 - P1 - P3 - P2 순서  
> Average waiting time : 7 (실행시간은 제외, Only wait time)

* **Non-preemptive SJF**
	* 실행 중에 나보다 짧은 프로세스가 들어오더라도 순서를 **바꾸지 않는 것**이다.
* **Preemptive SJF (= Shortest Remaining Time First)**
	* 실행 중에, 나보다 시간이 짧은 프로세스가 들어오면 **바꾸는 것**이다.
	* **시간 비교 기준은 원래의 내 시간이 아닌 현재 남은 내 시간이 된다.**
* **장점**
	* Average waiting time이 짧다.
	* ready queue가 빨리 줄어든다.
	* response 빠르다.
* **단점**
	* **Starvation (굶주림)**
		* 시간이 긴 Process는 계속해서 CPU 기다려야 한다.
		* 이는 *aging*으로 해결 가능하다. 오래 기다린 프로세스들에 우선 순위를 높이는 것으로 대기 시간에 따른 가중치를 부여한다.

#### CPU Burst Prediction
* *CPU가 실행되기 전에 사용 시간을 어떻게 아냐?* CPU time 은 **예측한 값**이다.
  * 이는 통계적 수치를 기반으로 한다. (일정 범위 내, moving average)
  * Simple Moving Average : 모두 동일하게, n개의 평균의 연속으로 나타낸다.
  * Weighted Moving Average : 값마다 weight를 주고 나눌 때도 weight 으로 나누는 개념이다.
  * Exponential Moving Average : weight 종류 중 하나로, weight을 Exp로 주는 개념이다.


### ✔️ Round-Robin (RR)
* **Preemptive scheduling**
* FIFO - ready queue에 먼저 들어온 프로세스가 CPU 먼저 사용하는 형식이다.
* **Time quantum** : 하나의 프로세스마다 얼마만큼의 시간을 부여할 것인지를 결정하는 요소다.
	* q를 길게 잡으면 FCFS와 다를 바가 없다.
	* q를 짧게 잡으면 Context switching time 시간 너무 많이 걸린다.
	* 10~100ms 정도로 잡는 것이 가장 좋다. (이때 context switch time: 10 microsec)
* **장점**
	* CPU 독점을 방지할 수 있다.
	* response time 짧다. 따라서 응답 중요한 시스템에서 잘 사용할 수 있다.
* **단점**
	* Context switching 하는 데에 시간을 많이 들일 수 있다.

> ex. Time Quantum = 4  
> 4초씩 사용 하고 (4보다 작은 것은 본인의 시간 만큼만) 반납 후 가장 뒤로 간다.

#### Multilevel Queue
* Ready queue 2개 만들어서 각각의 Queue마다 CPU 수행되는 시간 먼저 할당한 뒤 queue마다 다른 스케쥴링 적용 가능하다.


## Advanced Scheduling
### Multiple-Processor Scheduling
* *CPU 내의 core가 늘어나면서,* 스케쥴링 방법도 다양화 되었다.
* **Affinity Scheduling**
	* 이전에 사용한 CPU 다시 사용하는 방법 뜻한다.
	* core/CPU 마다 cahce를 따로 쓰기 때문에 사용한 CPU를 다시 사용하는 것이 효율적이다.
* **Load balancing**
	* Load balancing이란 사용할 수 있는 CPU 있으면 내가 썼던 CPU를 쓰려고 기다리지 않고 작업을 배분하는 것을 뜻한다.
	* 이는 Affinity Scheduling과 반대되는 개념이며, 두 방법이 적절히 조화되는 것이 좋다.

#### Multicore Processors
* Hyper-Threading : 실제로는 **두 개 이상의 스레드가 하나의 코어에 할당** 된다.
* CPU 내부에서도 계산하는 unit (ALU) 말고도 cache들 있다.
	* 어떤 값을 읽고 쓸 때 연산 장치가 쉴 때가 있다. 모든 하드웨어가 쉬지 않도록 그동안 다른 thread 수행한다.
	
### Real-Time CPU Scheduling (실시간)
![991DDC3B5B01B9C311](https://user-images.githubusercontent.com/64299475/138412207-2512b274-7c92-470b-92f3-40757b56a2ea.jpeg)


* **RTOS : 정해진 시간 내 Job의 수행 완료가 보장되는 것**
* time t: CPU burst time
* deadline d : 수행 보장 시간
* period p : 수행되는 빈도

> 예를 들어 전방 장애물 감지 스레드가 있을 때,  
> 1초마다 1번 씩 (p) 실행 되고, CPU 0.2초 소요 (t)되면  
> 0.8초 안에는(d) 반드시 실행 되어야 한다고 한다.  

#### Rate Monotonic Scheduling
* **자주 수행 되는 것에 우선권 주는 방법**이다.
* rate = 1/p : p가 짧아질 수록 rate 높아진다.
* Shorter periods = Higher priority
* Longer periods = Lower priority
* 하지만 **t1+t2 > p1**일 때, deadline 판단 없이 Rate Monotonic Scheduling을 진행해서 **t2가 덜 실행 되었는데 다시 t1을 실행시키면, t2의 deadline이 초과할 수 있다.**

#### Earliest Deadline First Scheduling (EDF)
* period : p1 = 50, p2 = 80
* CPU burst : t1 = 25, t2 = 35
* 스케쥴링 해야하는 시점에서 누가 가장 deadline 급한지 판단하고 그 프로세스한테 CPU할당하는 방법이다. 
*  **t1+t2 > p1**일 때, **t2의 deadline 급하면 p1 넘더라도 t2 실행시키는 방법**이다.
