# Stack
![stack](https://user-images.githubusercontent.com/64299475/138322065-329a5286-8cd7-42ff-aeb6-d6ccd884eaec.gif)

* Stack : 쌓여있는 것
* 동전 새로 쌓으려면 아래가 아닌 위로 쌓아야 함
* Logical Level :  한쪽으로만 넣고 뺄 수 있음 `LIFO (Last In First Out)`

## Stack ADT operation
* MakeEmpty : 비워라
* IsEmpty : 비었는지 안 비었는지
* IsFull : 가득 찼는지 아닌지
* Push(ItemType newItem) : 넣는 것
* Pop : 꺼내는 것
* Top : 제일 위에 있는 item return

> Stack Pointer 필요 `int top;`: 현재 가장 위에 있는 것 포인팅   
> ItemType : generic하게 만들기 위함.  
> Stack 비어있는데 Pop : underflow  
> 공간 없는데 Push : overflow  

