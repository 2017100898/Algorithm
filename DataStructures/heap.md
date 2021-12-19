# 힙 (Heap)
* 우선순위 큐를 위해 만들어진 자료구조다.
* Max Heap : 가장 큰 노드가 가장 위에 위치한다.
* Min Heap : 가장 작은 노드가 가장 위에 위치한다.
* 하나의 노드를 가질 때는 반드시 Left여야 한다.
* 힙은 반정렬 상태를 유지하며, 중복 값을 허용한다.
	* 반대로 Binary Search Tree는 중복값을 허용하지 않는다.
* 배열을 사용해서 구현하는 것이 낭비되는 공간이 없어서 편하고 Random Access가 가능하다.
* Root가 없어졌을 때 새롭게 heap 구성하는데 두는 비용 : `O(logn)`

## Heap의 조건
1. **Complete Binary Tree**
	* 마지막 레벨을 제외한 모든 높이에서 노드가 꽉 차 있는 Binary Tree (노드는 왼쪽에서 오른쪽 순으로 채워진다.)
2. **자식들보다 부모가 더 크거나 같아야 한다.**

```cpp
template< class ItemType >
struct HeapType 
{
	void ReheapDown ( int root , int bottom ) ; 
	void ReheapUp ( int root, int bottom ) ;
	ItemType* elements;
	int numElements ;
};
```

## ReHeapDown
<img width="400" src="https://user-images.githubusercontent.com/64299475/146689187-a76ec187-2989-457e-8219-88f61e41dfd9.png">


* used by DeleteItem
* 재귀로 끝없이 호출하다가,
  * 아래로 내려오던 것이 leaf node에 도달했을 때
  * 두 자식 노드 모두 본인보다 작을 때 탈출한다.

```cpp
template< class ItemType >
void HeapType<ItemType>::ReheapDown ( int root, int bottom )
{
  int maxChild ;
  int rightChild ;
  int leftChild ;
  leftChild = root * 2 + 1 ;
  rightChild = root * 2 + 2 ;
  
  if ( leftChild <= bottom )
  {
    if ( leftChild == bottom ) 
      maxChild = leftChld ;
    else 
    {
      if (elements [ leftChild ] <= elements [ rightChild ] )
        maxChild = rightChild ;
      else
        maxChild = leftChild ;
    }
    if ( elements [ root ] < elements [ maxChild ] )
    {
      Swap ( elements [ root ] , elements [ maxChild ] ) ;
      ReheapDown ( maxChild, bottom ) ;
    }
  }
}

```

## ReHeapUp
<img width="400" src="https://user-images.githubusercontent.com/64299475/146689185-2eb6a6f9-5d1f-4178-8d97-5d2652d81cbc.png">

* used by InsertItem
* 재귀로 끝없이 호출하다가,
  * root가 될 때
  * `부모 > 자식`을 만족했을 때 탈출한다.

```cpp
template< class ItemType >
void HeapType<ItemType>::ReheapUp ( int root, int bottom )
{
int parent ;
  if ( bottom > root )
  {
    parent = ( bottom - 1 ) / 2;
    if ( elements [ parent ] < elements [ bottom ] )
    {
      Swap ( elements [ parent ], elements [ bottom ] ) ;
      ReheapUp ( root, parent ) ;
    }
  }
}
```

## Priority Queue
* Highest-Priority Element가 언제나 access 할 수 있는 ADT
* `data`와 `우선순위 값` 2개를 내부적으로 저장해야 한다.
  * 항상 pair 하다.
  * 만약 pair가 아니면 data 자체가 우선순위 값인 경우다.
* Dequeue
	1. 일단 가장 큰 값을 찾고 `O(N)`
	2. 찾으면 뒤에 있는 값들을 앞으로 민다. `O(N)`
* 다양한 방법으로 구현할 수 있다.
	* Unsorted List
	* Array based Sorted List : insert가 어렵다.
	* Reference Based Sorted : O(N)
	* BST : O(logN)
	* Heap : O(logN)


### 시간 복잡도

|             | Enqueue | Dequeue |
| ----------- | ------- | ------- |
| Heap        | O(logN) | O(logN) |
| Linked List | O(N)    | O(N)    |
| BST         |         |         |
| ㄴ Balanced | O(logN) | O(logN) |
| ㄴ Skewed   | O(N)    | O(N)    |

