# List
## Unsorted List
* List : Data Element 사이에 1차원적인 관계(Linear Relationship) 가지는 것.
* Unsorted List :  data element 사이의 순서 존재 X

## Unsorted List Operation
### Transformers
* MakeEmpty : List 비우기
* InsertItem : List에 새로운 Item 넣기
* DeleteItem : 이 Item 지우기
  * Item 지우고 가장 뒤에 것을 그 자리에 채우고 length—;

### Observers
* IsFull : List 꽉 찼는지
* LengthIs : 몇 개 들어있는지
* RetrieveItem : 어떤 Item 가져와줘

### Iterators
* ResetLists : 제일 앞으로
  * currentpos = -1;
* GetNextItem : Item 순차적으로 보고 싶을 때, 다음 것 달라
  * currentpos++;
  * item = info[currentpos];


## Sorted List

* Sorted List : data element 사이의 순서 가지는 리스트

## Sorted List Operation
* Insert
  1. 가장 먼저 위치를 찾는다.
  2. 가장 뒤에서부터 1칸씩 뒤로 간다.
  3. 빈 공간에 숫자를 집어넣는다.
  4. `length++;`
* Delete
  1. 지울 숫자의 위치를 찾는다.
  2. 지워진 숫자 바로 뒤에서부터 한칸씩 앞으로 이동한다.
  3. `length—;`