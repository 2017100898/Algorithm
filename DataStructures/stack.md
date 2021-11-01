# Stack (스택)

<img height = "200" src="https://user-images.githubusercontent.com/64299475/138322065-329a5286-8cd7-42ff-aeb6-d6ccd884eaec.gif">

* Stack : 쌓여있는 자료구조
* 동전을 새로 쌓으려면 아래가 아닌 위로 쌓아야 한다.
* Logical Level :  한쪽으로만 넣고 뺄 수 있는 `LIFO (Last In First Out)` 구조

#### Stack ADT operation

* MakeEmpty : Stack을 비운다.
* IsEmpty : 비었는지 안 비었는지 확인한다.
* IsFull : 가득 찼는지 아닌지 확인한다.
* Push(ItemType newItem) : Item을 제일 위에 넣는다.
* Pop : 제일 위에 있는 item을 꺼낸다.
* Top : 제일 위에 있는 item return한다.

> Stack은 `top` pointer가 필요하며, 이는 현재 가장 위에 있는 것 포인팅한다.  
> ItemType은 generic하게 만들기 위해 사용된다.  
> Stack 비어있는데 Pop을 실행하면 underflow, 공간 없는데 Push 하면 overflow 가 발생한다.

