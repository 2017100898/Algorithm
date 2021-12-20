# Sorting and Searching
* Sort
  * ascending : 1 2 3 4
  * descending : 4 3 2 1

## Sort
* 가정
  * 정렬을 하기 위해서는 대소 관계를 파악할 수 있는 Key 값이 있어야 한다.
  * 같은 값이 있어도 괜찮다.
* **Simple Sort : O(N^2)**
  * Straight Selection Sort
  * Bubble Sort
  * Insertion Sort
* **Complex Sort : O(NlogN)**
  * Heap Sort
  * Quick Sort
  * Merge Sort
* n 이 크지 않으면, nlogn 보다 n^2이 더 좋을 수도 있다. (개발 비용을 낮출 수 있기 때문)

## Straight Selection Sort
* Selection Sort는 안정성을 보장하지 않는다.
  * 서로 같은 값끼리 인덱스가 역전하지 않는 것이 안정성을 보장하는 것이다.
* 정렬이 안 된 부분 중에 가장 작은 값을 찾고 n번 Index로 이동하는 과정을 반복한다. (n : 0, 1, 2, 3...)
 
## Bubble Sort
* 두 개의 인접 노드를 묶어서 비교 후 역순이면 Swap 하는 것
* 이는 Swap 연산이 너무 많이 일어나고, Straight Selection Sort보다 시간이 더 오래 걸릴 수 있다는 단점이 있다.
* 효율이 좋지 않다.

## Insertion Sort
* 삽입할 위치를 찾아서 insert 하는 Sorting 방법
* 밀어내는 연산까지 고려하면 효율이 좋지 않다.

## Heap Sort
* Root를 뽑고 ReHeapDown하는 과정을 반복하는 방법
* (N/2) * O(logN) for making heap
* (N-1) * O(logN) for sorting heap

## Quick Sort
* 기준 키 기준으로 작거나 같은 값을 지닌 Data는 앞으로, 큰 값을 지닌 Data는 뒤로 가게 하여 정렬하는 방법
* 다른 것은 몰라도, 기준점의 위치는 확정할 수 있다.
* 한쪽으로 치우치게 나눠질 수록 효율이 좋지 않으며, 절반으로 나눠지면 효율이 좋다.
* Quick Sort는 **평균적으로** 빠르다.

## Merge Sort
* 하나의 Data를 여러 개의 Sub Data로 분할한 후 정렬하고 합병하는 과정을 재귀적으로 반복하는 정렬 방법
* 이 정렬 방법은 새로운 메모리가 필요하므로 메모리를 많이 쓴다.
* 개선된 형태로 메모리 절반 정도를 줄일 수 있다.

## Sorting 시간 복잡도
<img width = "400" src= "https://user-images.githubusercontent.com/64299475/146688195-d848d475-5e79-4035-948f-5259617fe742.png">
<img width = "400" src= "https://user-images.githubusercontent.com/64299475/146688197-9d67ce70-c6c1-424b-a9b7-e562713384ae.png">

## Sorting pros and cons 정리
<img width = "470" src= "https://user-images.githubusercontent.com/64299475/146688196-8beb4cfe-5457-45ef-855f-035ea6dcf21a.png">

## Tag Sort
* 키 필드를 정렬하여 올바른 순서를 만든 다음 실제 데이터 레코드를 해당 순서로 배치하는 정렬 방법
* 실제 레코드 대신 포인터를 재배치하여 이동 시간을 단축할 수 있다.

## Search
* Linear Searching - O(N)
* High-Probability Ordering - O(N)
* Key Ordering : Binary Search - O(logN)

## Hashing
* 해싱이란, 어떤 value가 주어졌을 때, value에 해당하는 unique한 Index를 알려주는 함수다.
* 해싱은 무조건 random access 가 가능하며, sorting이 필수다. - `O(1)을 구현하기 위함`
* 해싱은 1:1 대응이지만, 데이터보다 저장소가 더 작아서 중복 데이터가 등장할 수도 있다.
* Closed Hashing
* Opened Hashing

## Linear Probing
* array를 저장할 때, 임의의 함수를 만들어서 규칙적으로 저장한다.
* Hash(Key) = partNum % 100
	* ex) 4401 : [01] 번에 저장
	* **하지만 이때, 4201가 들어온다면 (HashVal + 01)%100 으로 이동한다.** 
	* 만약 4401가 이미 삭제 된 상태에서 4201을 찾는다면, 바로 아래에 있을 수 있으므로, **아래 것까지 확인하는 절차를 거쳐야 한다.**
	* 만약 4401가 이미 삭제 된 상태에서 이 상태에서 4101을 넣는다면 [01]에 넣으면 된다.

### Linear Probing의 문제점
<img width="440" alt="스크린샷 2021-12-20 오전 4 06 15" src="https://user-images.githubusercontent.com/64299475/146688186-45e25f27-d1d2-4a06-b5b4-9c8752c522d6.png"> 

* 사진에서 보는 바와 같이 77003을 삭제했을 때, 42504를 찾으려면 곤란하다.

### 충돌(Collision)
* 이미 array에 숫자 있을 때 충돌이 일어난다. 해싱 구성 시 이를 어떻게 처리할 건지에 대한 정보를 반드시 포함해야 한다.
* **Rehashing** : 충돌이 생기면 다른 hash function 사용하는 방법이다. (closed hashing)
  * f1 = key %100
  * f2 = (f1+1)%100
  * f3 = (f2+1)%100 `Linear Probing`
  * (HashVal ± 1^2) % array size `Quadratic Probing (1-2-4-...)`
  * (HashVal + random) % array size `Random Probing (1-3-7-...)`
* Collision을 줄이기 위해서는 Table을 크게 만들거나, Uniform 하게 분배해야 한다.

## Opened Hashing
### Buckets
<img width="440" src="https://user-images.githubusercontent.com/64299475/146688190-ab076188-9e9a-42d7-afab-461afe0807ee.png">

* 충돌 처리 방법
* 메모리를 얼마나 쓸지 예상하지 못 한다는 단점이 존재한다.
* 어차피 3개가 넘어가면 또 다시 충돌이 일어나므로 좋은 방법은 아니다.
* 너무 크게 만들면 Memory 낭비가 심하다.

### Chain
<img width="440" src="https://user-images.githubusercontent.com/64299475/146688188-bb82249c-2d20-4083-955d-4567235cb589.png">

* Linked List를 이용한 충돌 처리 방법
* 메모리를 얼마나 쓸지 예상하지 못 한다는 단점이 존재한다.
