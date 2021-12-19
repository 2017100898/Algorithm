# Sorting and Searching
* Sort
  * ascending : 1 2 3 4
  * descending : 4 3 2 1

## Sort
* 가정
  * element끼리 비교가 가능해야 하고 같은 값이 있어도 괜
* Simple Sort  O(N^2)
  * Straight Selection Sort
  * Bubble Sort
  * Insertion Sort
* Complex Sort O(NlogN)
  * Heap Sort
  * Quick Sort
  * Merge Sort



## Straight Selection Sort
* Selection Sort는 안정성을 보장하지 않는다.
  * 서로 같은 값끼리 인덱스가 역전하지 않는 것이 안정성을 보장하는 것이다.

  

## Bubble Sort
* 두 개의 인접 노드를 묶어서 비교 후 역순이면 Swap 하는 것
* 이는 Swap 연산이 너무 많이 일어나고, Straight Selection Sort보다 시간이 더 오래 걸릴 수 있다.
* 효율이 좋지 않다.



## Insertion Sort
* 삽입할 위치를 찾아서 insert 하는 Sorting 방법
* 밀어내는 연산까지 고려하면 효율이 좋지 않다.



## Heap Sort
* Root를 뽑고 ReHeapDown하는 과정을 반복한다.



## Quick Sort
* 기준 키 기준으로 작거나 같은 값을 지닌 Data는 앞으로, 큰 값을 지닌 Data는 뒤로 가게 하여 정렬하는 방법
* 다른 것은 몰라도, 기준점의 위치는 확정할 수 있다.
* 한쪽으로 치우치게 나눠질 수록 효율이 좋지 않으며, 절반으로 나눠지면 효율이 좋다.



## Merge Sort
* 하나의 Data를 여러 개의 Sub Data로 분할한 후 정렬하고 합병하는 정렬 방법
* 이 정렬 방법은 새로운 메모리가 필요하므로 메모리를 많이 쓴다.



## Search
* Linear Searching - O(N)
* High-Probability Ordering - O(N)
* Key Ordering : Binary Search - O(logN)



## Hashing
* 해싱이란, 어떤 value가 주어졌을 때, value에 해당하는 unique한 Index를 알려주는 함수다.
* Buckets
* Chain
* 충돌 (Collision) : 이미 array에 숫자 있을 때 충돌이 일어난다.
  * Rehashing : 충돌이 생기면 다른 hash function 사용하는 것이다.
    * f1 = key %100
    * f2 = (f1+1)%100
    * f3 = (f2+1)%100 `Linear Probing`
  * Collision을 줄이기 위해서는 Table을 크게 만들거나, Uniform 하게 분배해야 한다.