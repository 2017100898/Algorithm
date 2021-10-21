# Queue
![queue-insert-item](https://user-images.githubusercontent.com/64299475/138326422-67ac4373-363c-404e-bfcf-46786074f0dc.gif)
![queue-delete-item](https://user-images.githubusercontent.com/64299475/138326413-babe1a15-bcca-405f-b9dc-4d178835bc71.gif)

* Logical Level :  한쪽으로 넣고 반대쪽으로 뺀다  `FIFO (First In First Out)`

## Queue Operation
### Transformers
* MakeEmpty
* Enqueue : 넣는다
* Dequeue : 뺀다
### Observers
* IsEmpty
* IsFull

## Circular Queue
![Circular-queue_1](https://user-images.githubusercontent.com/64299475/138327979-02899149-fac0-4bcf-a5b0-40567f143736.png)

* 끝에 다다르면 다시 앞으로 보내지는 것. 원래는 f < r 이지만, 되돌리면 뒤에 것 숫자가 더 작아질 수 있다.
* 	Full일 때와 Empty일 때 둘 다 `rear + 1 == front` 이므로 front 한 칸 앞을 가리키도록 한다.

