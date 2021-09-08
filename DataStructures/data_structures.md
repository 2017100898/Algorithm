# Data Structures
* Data가 많을 때 어떻게 저장하고 가공할 것인가?
* High-level data structures : stack, queue, tree
* Data aggregates : array, structure
* Primitive data types : 21, 4.21, 'M'
* Machine level data storage : 1011010001101

### Why Data Structures?
* Data 양이 많아지면 Search, Sort에서 array 등을 사용하면 비효율이 발생한다.
* 자료구조는 더욱 경제적으로 프로그래밍을 할 수 있도록 도와준다.

### 소프트웨어 공학
* 시간, 비용 -> 체계적으로 하는 것

### 개발 방법
* Top-down : 큰 기능 -> 작은 기능
* Bottom-up : 작은 기능 결합 -> 위로
* Functional decomposition 
* Round-trip gestalt design

### 접근 방법
* Verb : 절차 지향 관점 - 어떤 순서로 시작? 끝?
* Noun : 객체 지향 관점 - 필요한 객체? 객체 디자인 중요

### Test
* 프로그래밍을 할 때는 예외 케이스가 충분히 처리될 수 있도록 해야 한다.
* Verification & Validation

- - - -

## Data
* 정보를 기계가 분석할 수 있게 표현해 놓은 것
* ADT (Abstract Data Type): Data Type 을 추상화 한 것.  `int a;` sys 밑에서 어떻게 돌아가는지는 몰라도 잘 사용해왔다.

## Composite Data Type
* Unstructured : class, struct
* Structured : arrays

```cpp
struct CarType{
	int year;
	char maker[10];
	float price;
} //선언

CarType thisCar; //실제 변수 memory에 만들어짐
CarType myCar;
```

## Class data type
* struct : public이 default, 관용적으로는 멤버 변수들만 포함
* class : 사용자 정의형 데이터 타입, 멤버 함수들까지 포함 가능, private 접근자
* Scope Resolution Operator (::) 
* Class에서는 객체 물려 받아서 새로운 객체 만든다. `is-a 관계` (상속)

 
