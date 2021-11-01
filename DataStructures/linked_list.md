# Linked List
* Linked List는 포인터끼리의 연결성을 중시한다.
* Linked List에서는 동적할당으로 입력 들어올 때마다 공간을 잡아주기 때문에 주소값이 계속해서 다르다.
* 장점
  1. Dynamic memory allocation : 필요할 때마다 memory 받아 쓴다.
  2. Efficient insertion-deletion : 끼워넣기만 하면 돼서 효율적이므로, 삭제 및 추가가 많은 경우 이득이다.
  3. 낭비 되는 공간이 없다.
* 단점
  1. 에러가 발생할 확률이 높고, 접근 시간이 오래 걸린다.
     * 따라서, 원소 전체에 접근해야 하는 일이 많은 경우는 사용을 지양하는 것이 좋고, Array를 쓰는 것이 오히려 효율적일 것이다.

## Node

* info: 노드의 정보를 담는 데이터
* next: 다음 노드 가리키는 포인터

## StackType

```cpp
class StackType
{
public:

  StackType();
  ~StackType();
  bool IsFull() const;
  bool IsEmpty() const;
  void Push(ItemType item);
  void Pop();
  ItemType Top();
  void ReplaceItem(ItemType oldItem, ItemType newItem);

private:
  NodeType* topPtr;
};

struct NodeType
{
  ItemType info;
  NodeType* next;
};
```

#### Add Item

<img height="100" src="https://user-images.githubusercontent.com/64299475/138510011-7267fb3d-abeb-4e80-97ea-07c3d0ade60f.gif">

```cpp
void StackType::Push(ItemType newItem){
  if (IsFull())
    throw FullStack();
  else
  {
    NodeType* location; //새로운 노드 만들기
    location = new NodeType;
    location->info = newItem; //노드 정보 넣어주기
    location->next = topPtr; //topPtr(이전 노드)를 다음 노드로 연결 (다음 Pop 될 item)
    topPtr = location; //topPtr 변경 (topPtr부터 Pop)
  }
}
```

#### Delete Item

<img height = "80" src="https://user-images.githubusercontent.com/64299475/138510003-d884e072-09c5-4717-b1d6-cd4e038ace31.gif">

```cpp
void StackType::Pop(){
  if (IsEmpty())
    throw EmptyStack();
  else
  {  
    NodeType* tempPtr; //빈 노드 만들기
    tempPtr = topPtr; //topPtr 복사하기
    topPtr = topPtr->next; // topPtr 다음 노드를 topPtr으로 설정 (다음 Pop 될 item)
    delete tempPtr; //복사해둔 것 삭제
  }
}
```

## QueueType

* rear 과 front pointer로 변경한다.
* qFront == NULL 또는 qRear == NULL 이면 비어있다고 판단한다.

```cpp
template <class ItemType>
class QueType
{
public: 
    QueType();
    QueType(int max);
    ~QueType();
    void MakeEmpty();
    bool IsEmpty() const;
    bool IsFull() const;
    void Enqueue(ItemType newItem);
    void Dequeue(ItemType& item);
    void ReplaceItem(ItemType oldItem, ItemType newItem);

private:
  NodeType<ItemType>* front;
  NodeType<ItemType>* rear;
};

template <class ItemType>
struct NodeType
{
  ItemType info;
  NodeType* next;
};

```



#### Add Item

```cpp
template <class ItemType>
void QueType<ItemType>::Enqueue(ItemType newItem){
  if (IsFull())
    throw FullQueue();
  else
  {
    NodeType<ItemType>* newNode; //새로운 노드 만들기
    newNode = new NodeType<ItemType>;
    newNode->info = newItem; //아이템 정보 담기
    newNode->next = NULL; //다음 정보는 지금은 모르니까 NULL로 표시
    if (rear == NULL) //만약 큐에 끝 노드 존재 안 하면
      front = newNode; //front를 현재 노드로 설정하기
    else // 존재하면
      rear->next = newNode; //일단 끝 노드의 next를 나로 설정하기 (끝 노드 다음 내가 Pop 될 것이기 때문)
    rear = newNode; //끝 노드는 나로 설정하기
  }
}
```

#### Delete Item

```cpp
template <class ItemType>
void QueType<ItemType>::Dequeue(ItemType& item){
  if (IsEmpty())
    throw EmptyQueue();
  else
  {
    NodeType<ItemType>* tempPtr; // 빈 노드 만들기
    tempPtr = front; //첫 노드 (삭제되어야할 item) 복사하기
    item = front->info; //(return 해줄수도 있으니) item은 front의 정보로 설정
    front = front->next; // 이제 front는 나 다음에 있는 노드 (다음 Pop 될 item)
    if (front == NULL) //만약 다음 노드가 없으면,
      rear = NULL; //끝노드도 없다고 판단
    delete tempPtr; // 복사해둔 것 삭제하기
  }
}
```

## Unsorted List

* 값 찾기 위해서는 임의의 변수 1개 `location` 이 필요하다.
* 한 노드씩 지나가면서 맞는지 아닌지 확인해야하는데 자유롭게 이동 가능한 포인터가 없다.

```cpp
template <class ItemType>
class UnsortedType{
public:
  UnsortedType();     
  ~UnsortedType(); 
  bool IsFull() const;
  int  LengthIs() const;
  void MakeEmpty();
  void RetrieveItem(ItemType& item, bool& found);
  void InsertItem(ItemType item); 
  void DeleteItem(ItemType item);
  void ResetList();
  void GetNextItem(ItemType& item);

private:
  NodeType<ItemType>* listData; // 제일 앞 노드 포인트
  int length;
  NodeType<ItemType>* currentPos; // 지금 어디까지 봤는지 기록하는 포인터
};

template<class ItemType>
struct NodeType
{
    ItemType info;
    NodeType* next;
};
```



#### Add Item

```cpp
template <class ItemType>
void UnsortedType<ItemType>::InsertItem(ItemType item){
    NodeType<ItemType>* location; // 새로운 노드 만들기
    location = new NodeType<ItemType>;
    location->info = item; //새로운 노드에 정보 넣기
    location->next = listData; // 다음 노드는 listData가 포인팅하고 있는 노드
    listData = location; //이제 listData는 나를 가리킨다
    length++; //lenght+1
}
```

#### Delete Item

* Delete Item 실행 시, 반드시 찾아야하는게 List 내에 있어야 한다.

```cpp
template <class ItemType>
void UnsortedType<ItemType>::DeleteItem(ItemType item){
    NodeType<ItemType>* location = listData; //첫 노드가 가리키고 있는 노드가 location
    NodeType<ItemType>* tempLocation; //빈 위치 (삭제를 위함)
    if (item == listData->info) //listData가 가리키고 있는 첫노드의 정보가 item과 일치한다면
    {
        tempLocation = location; // 그 노드 tempLocation으로 복사
        listData = listData->next; //첫노드의 다음 노드가 첫노드가 된다
    }
    else // 일치하지 않는다면
    {
        while (!(item==(location->next)->info)) //다음노드의 정보가 item과 같아질 때까지 while문 돌림
            location = location->next; //한 노드씩 location이 됨

        tempLocation = location->next; //다음노드의 info가 item과 같아지면 다음 노드 temp에 복사 
        location->next = (location->next)->next; //다음다음 노드가 다음노드가 되고
    }
    delete tempLocation; // temp는 삭제
    length--;
}
```

#### Find (RetrieveItem)

```cpp
template <class ItemType>
void UnsortedType<ItemType>::RetrieveItem(ItemType& item, 
    bool& found){
    bool moreToSearch; //더 찾을지 판단하는 변수
    NodeType<ItemType>* location; // 자유 이동가능한 location 변수

    location = listData; //첫 노드가 location이 된다
    found = false; //우선 found 변수를 false로 설정
    moreToSearch = (location != NULL);

    /*위치 찾기*/
    while (moreToSearch && !found) // 더 찾지 않아도 될 때까지 반복문 수행
    {
        if (item == location->info) //location info가 item와 같으면 
        {
            found = true; //찾았다고 판단
            item = location->info; //반환값은 info가 된다
        }
        else //location info가 item와 다르면
        {
            location = location->next; //다음 노드로 이동한다
            moreToSearch = (location != NULL); //location이 NULL이 아니라면 더 찾는다
        }
    }
}
```

## Sorted List

```cpp
template <class ItemType>
class SortedType{
public:
  SortedType();     
  ~SortedType();  
  bool IsFull() const;
  int  LengthIs() const;
  void MakeEmpty();
  void RetrieveItem(ItemType& item, bool& found);
  void InsertItem(ItemType item);
  void DeleteItem(ItemType item);
  void ResetList();
  void GetNextItem(ItemType&);

private:
  NodeType<ItemType>* listData;
  int length;
  NodeType<ItemType>* currentPos;
};
template<class ItemType>
struct NodeType
{
    ItemType info;
    NodeType* next;
```

#### Add Item

```cpp
template <class ItemType>
void SortedType<ItemType>::InsertItem(ItemType item)
{
  NodeType<ItemType>* newNode; //새로운 노드
  NodeType<ItemType>* predLoc; //이전 노드 가리키는 변수
  NodeType<ItemType>* location;  //지금 위치 저장하는 변수
  bool moreToSearch; //더 찾을지 판단하는 변수

  location = listData; //첫 노드가 location이 된다
  predLoc = NULL; //이전은 존재하지 않으므로 일단 NULL
  moreToSearch = (location != NULL); 

/*위치 찾기*/
  while (moreToSearch) 
  {
    if (location->info < item) //location 노드의 정보가 찾는 값보다 작을때
    {
      predLoc = location; //pred를 location 위치로 설정
      location = location->next; //location은 한칸뒤로 이동
      moreToSearch = (location != NULL);
    }
    else //location 노드의 정보가 찾는 값보다 크거나 같을 때
      moreToSearch = false;//멈춘다
  }

/*삽입하기*/
  newNode = new NodeType<ItemType>; 
  newNode->info = item;//newNode에 정보 넣고

  if (predLoc == NULL)   //pred(이전) 노드가 없으면
  {
    newNode->next = listData; // newNode가 첫노드
    listData = newNode;
  }
  else//이전노드 있으면 - pred와 location 사이에 newNode 끼워넣어야 한다
  {
    newNode->next = location;//newNode 의 다음은 location 
    predLoc->next = newNode; //pred노드의 다음은 newNode
  }
  length++;
}
```

#### Delete Item

```cpp
template <class ItemType>
void SortedType<ItemType>::DeleteItem(ItemType item){
    NodeType<ItemType>* location = listData;
    NodeType<ItemType>* tempLocation;

    if (item == listData->info)
    {
        tempLocation = location;
        listData = listData->next;		
    }
    else
    {
        while (!(item==(location->next)->info))
          location = location->next;

        tempLocation = location->next;
        location->next = (location->next)->next;
    }
    delete tempLocation;
    length--;
}
```

## Doubly Linked List

* Linked List sorted List에서 가장 마지막 노드를 찾는 시간이 너무 오래 걸린다. `O(N^2)`
* Circular하고, listData가 가장 뒤의 노드 Pointing 하는 Doubly Linked List 자료구조로 문제를 해소하고자 했다.
* 앞을 볼 필요가 많을 때 자신의 앞과 뒤 모두를 포인팅하는 리스트를 고려할 수 있다.
* 단점
  * Data 양이 늘어나고 (+4byte), 처리하는 연산자가 추가로 필요하다.

#### Add Item

```cpp
newNode -> back = location -> back;
newNode -> next = location;
location -> back -> next = newNode;
location -> back = newNode;
```

* 허상 포인터(Dangling pointer)가 발생할 수 있기 때문에 Doubly Linked List에서는 포인팅 순서가 중요하다.
* 위 방식을 완전히 따라야 하는 것은 아니다.


#### Delete Item

```cpp
location -> back -> next = location -> next;
location -> next -> back = location -> back;
```

### Header & Trailer

* 양 끝단 임의로 항상 존재하게 만드는 방법 `aaaaaaaaaaaaa`, `ZZZZZZZZZZZ`
  * 장점: end case delete시의 불편함이 해소되고 코드가 간단해진다.
  * 단점: 쓸데 없는 메모리 소비가 일어난다.


## 복잡도 (Big-O)
* **시간복잡도** :  단위연산 (가장 기초가 되는 연산) 몇 번 쓰는가? 
  * 비교 연산 횟수 얼마나 줄일 수 있는지 파악하는 것이 중요하다.
* 공간복잡도 : 입력 되는 record의 크기 n에 비례해서 공간 얼마나 필요한가?
* O(logn)과 O(n)의 교차지점 이후로는 n^2, n^3 등의 그래프가 항상 logn의 위에 있다.
* `O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n)`
* BigO는 데이터 수의 증가에 따른 연산 횟수 증가 형태 표현한 것이다.



### Unsorted list

| Operation    | Array | Linked-list |
| ------------ | ----- | ----------- |
| Constructor  | O(1)  | O(1)        |
| MakeEmpty    | O(1)  | O(N)        |
| InsertItem   | O(1)  | O(1)        |
| DeleteItem   | O(N)  | O(N)        |
| IsFull       | O(1)  | O(1)        |
| LengthIs     | O(1)  | O(1)        |
| RetrieveItem | O(N)  | O(N)        |
| ResetList    | O(1)  | O(1)        |
| GetNextItem  | O(1)  | O(1)        |
| Destructor   | O(1)  | O(N)        |

### Sorted list

| Operation    | Array               | Linked-list |
| ------------ | ------------------- | ----------- |
| Constructor  | O(1)                | O(1)        |
| MakeEmpty    | O(1)                | O(N)        |
| InsertItem   | O(N)                | O(1)        |
| DeleteItem   | O(N)                | O(N)        |
| IsFull       | O(1)                | O(1)        |
| LengthIs     | O(1)                | O(1)        |
| RetrieveItem | O(N) or O(log_2(N)) | O(N)        |
| ResetList    | O(1)                | O(1)        |
| GetNextItem  | O(1)                | O(1)        |
| Destructor   | O(1)                | O(N)        |

### Stack

| Operation   | Array | Linked-list |
| ----------- | ----- | ----------- |
| Constructor | O(1)  | O(1)        |
| MakeEmpty   | O(1)  | O(N)        |
| Push        | O(1)  | O(1)        |
| Pop         | O(1)  | O(1)        |
| IsFull      | O(1)  | O(1)        |
| IsEmpty     | O(1)  | O(1)        |
| Top         | O(1)  | O(1)        |
| Destructor  | O(1)  | O(N)        |

#### Queue

| Operation   | Array | Linked-list |
| ----------- | ----- | ----------- |
| Constructor | O(1)  | O(1)        |
| MakeEmpty   | O(1)  | O(N)        |
| Enqueue     | O(1)  | O(1)        |
| Dequeue     | O(1)  | O(1)        |
| IsFull      | O(1)  | O(1)        |
| IsEmpty     | O(1)  | O(1)        |
| Destructor  | O(1)  | O(N)        |