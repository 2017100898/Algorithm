# 힙 (Heap)
* Max Heap : 가장 큰 노드가 가장 위에 위치한다.
* 하나의 노드를 가질 때는 반드시 Left여야 한다.

## Heap의 조건
1. Complete Binary Tree
2. 자식들보다 부모가 더 크거나 같아야 한다.

## ReHeapDown

* used by DeleteItem
* 재귀로 끝없이 호출하다가,
  * 아래로 내려오던 것이 leaf node에 도달했을 때
  * 두 자식 노드 모두 본인보다 작을 때 탈출한다.

## ReHeapUp
* used by InsertItem
* 재귀로 끝없이 호출하다가,
  * root가 될 때
  * `부모 > 자식`을 만족했을 때 탈출한다.

## Priority Queue
* Highest-Priority Element가 언제나 access 할 수 있는 ADT
* `data`와 `우선순위 값` 2개를 내부적으로 저장해야 한다.
  * 항상 pair 하다.
  * 만약 pair가 아니면 data 자체가 우선순위 값인 경우다.