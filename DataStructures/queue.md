# Queue (큐)

<img height = "200" src="https://user-images.githubusercontent.com/64299475/138326422-67ac4373-363c-404e-bfcf-46786074f0dc.gif">

<img height = "200" src="https://user-images.githubusercontent.com/64299475/138326413-babe1a15-bcca-405f-b9dc-4d178835bc71.gif">

* Logical Level :  한쪽으로 넣고 반대쪽으로 빼는  `FIFO (First In First Out)` 구조

  

## Queue Operation

* Transformers

  * MakeEmpty
  * Enqueue : 넣는다
  * Dequeue : 뺀다

* Observers

  * IsEmpty

  * IsFull

    

## Circular Queue

<img height = "240" src="https://user-images.githubusercontent.com/64299475/138327979-02899149-fac0-4bcf-a5b0-40567f143736.png">

* 끝에 다다르면 다시 앞으로 보내지는 구조다. 원래는 f < r 이지만, 되돌리면 뒤에 것 숫자가 더 작아질 수 있다.

* `rear = (rear+1)%maxQue` 처럼 maxQue의 modular 연산을 통해 Circluar Queue를 구현할 수 있다.

* Full일 때와 Empty일 때 둘 다 `rear + 1 == front` 이므로 두 상태의 구분을 위해 **reserve 공간을 생성하고 front 한 칸 앞을 가리키도록 한다.**

* front와 rear의 초기화

  * Original : front = 0, rear = -1

  * Reserved : front = -1, rear = -1

    

> reserved cell 추가 시,
>
> Full의 판단 : rear+1 == front
>
> Empty의 판단 : rear == front



## Counted Queue

* length 멤버 변수를 추가해서 item의 개수를 빠르게 파악할 수 있도록 하는 Queue 구조다.
  * Enqueue 시에 length++한다.
  * Dequeue 시에 length--한다.
* Enqeue와 Dequeue가 사용될 때마다 length 연산을 해야하기 때문에 length를 추가하는 일은 비용이 많이 든다. 
* Queue의 길이를 바로 파악할 수 있는 LengthIs() 함수를 자주 사용할 때 유리하다.

