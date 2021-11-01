# Data Structures
* Data가 많을 때 어떻게 저장하고 가공할 것인가?
* High-level data structures : stack, queue, tree
* Data aggregates : array, structure
* Primitive data types : 21, 4.21, 'M'
* Machine level data storage : 1011010001101

### Why Data Structures?
* Data 양이 많아지면 Search, Sort에서 array 등을 사용하면 비효율이 발생한다.
* 자료구조는 더욱 경제적으로 프로그래밍을 할 수 있도록 도와준다.



## 소프트웨어 공학

* 소프트웨어 공학은 시간 내, 비용 내에서 체계적으로 동작하는 것을 뜻한다.
* Tool
  * Hardware : 컴퓨터, 장치
  * Software : 운영체제, 컴파일러, 디버깅 System 등
  * Ideaware : Knowledge (개발을 하기 위해 알고 있어야할 지식, ex. 자료구조 )
* Alogrithm (알고리즘) : 주어진 문제를 풀기 위해 거쳐야 할 과정
* Software Quality 측정
  1. 동작 하는가?
  2. 수정하는데 시간, 돈이 얼마나 적게 드는가? (즉, 남이 읽을 수 있는 코드인가?)
  3. 재사용 가능한가?
  4. 예산(돈)을 지킬 수 있는가?



###  소프트웨어 개발 방법
* Specification(구체화)는 `어떻게`가 아닌, `무엇을 해야 하는가?` 에 관한 것
* 추상화 : 우리가 만들어야 하는 것 굉장히 복잡하므로 간단한 형태로 만들어야 한다. 따라서 System viewer의 관점에서 필요한 것만 남겨야 한다. (Information Hiding)

  

### 개발 방법
* Top-down : 큰 기능 ⇒ 더 작은 기능
* Bottom-up : 결합 ⇒ 위로
* Functional decomposition (Top-down) : 함수의 합성, 큰 함수 구현하기 위해서는 어떻게 해야 하는가?
* Round-trip gestalt design : 객체로 바라보는 것

  

### 접근 방법
* Verb : 절차 지향(Procedural) 관점 - 어떤 순서로 시작하고 끝을 맺을 것인가?
* Nouns : 객체 지향 관점 - 필요한 객체가 무엇인가? 객체 디자인이 중요하다.



### Test
* 프로그래밍을 할 때는 예외 케이스가 충분히 처리될 수 있도록 해야 한다.
* V&V (Verification & Validation)
  * Verification : 프로세스 관점에서 잘 동작하는가?
  * Validation : 스펙대로 만들고 있는가? `검증이 필요하며 Test case를 통과하더라도 우연일 수 있기 때문에 수학적 증명이 필요하다.`
  * 결국 둘 다 잘해야 한다.
* Error : Specification, Design, Coding, Input - 갈 수록 비용이 든다.
* Error 컨트롤
  1. Robustness
  2. Preconditions
  3. Postconditions

     

## Data
* 정보를 기계가 분석할 수 있게 표현해 놓은 것
* Data Encapsulation : 외부로부터 자세한 데이터 객체의 자세한 구현 정보를 숨기는 것
  * Application level
  * Logical level
* ADT (Abstract Data Type)
  * Data Type 을 추상화 한 것. 즉, 명세(Property)와 구현(Implementation) 분해한 것
  * 우리는`int a;` 가 system 밑에서 어떻게 돌아가는지는 몰라도 잘 사용해왔다.
* Data의 3가지 레벨
  * Application Level (user level)  : 특정 상황에서 실제 Data 모델링 
  * Logical Level (ADT level) : Data의 범위, Data가 가능한 연산 (What)
  * Implementation Level :  Data type이 프로그램에서 실제로 작동하는 모습 (How)
* ADT operation의 특성
  1. Constructor : 새로운 instance 만드는 것
  2. Transformer : Data Element 변경하는 것
  3. Observer : 값을 변경하지 않고 구경만 하는 것
  4. Iterator : Data 많이 있을 때 다음 것 가져오는 것 (ex. foreach)


## ADT
* ADT는 기능의 구현 부분을 나타내지 않고 순수한 기능이 무엇인지 나열한다.
* 구현자는 사용자가 사용할 때 꼭 필요한 정보만 제공한다.
* ADT는 수치화 되어 있는 명세서다.
  * 어떤 기능, 어떤 데이터를 필요로 하며, 어떤 동작을 하는지 작성한다.
  * 구현자와 사용자를 구분한다.
* ADT 설계의 장점
  * Operation과 domain만 정의하여 독립적인 작업이 가능하며 및 공동 작업에 유리하다.
  * 구현 방법이 바뀌어도 응용 프로그램은 영향을 받지 않고 재사용이 가능하다.
  * 추상 자료형에 대한 구현은 외부로부터 숨겨져 정보 은닉이 이루어진다.
  * 데이터 타입의 표현에 대한 수정이 편리하다.

  

## Composite Data Type
* Unstructed : class
  * 꼭 같은 Data Type일 필요는 없다. (heterogeneous)
* Structured : 배열 (arrays)
  * 크기가 모두 같은 homogeneous 구조다.

```cpp
struct CarType{
	int year;
	char maker[10];
	float price;
} //선언

CarType thisCar; //실제 변수 memory에 만들어짐
CarType myCar;
```

* Data
  * Static : 전역변수,  한번 정해지면 바뀌지 않는다
    * binding time : compile
  * Automatic : 지역변수
  * Dynamic : 동적할당, 바뀐다
    * binding time :  runtime

```cpp
void f() { 
	int x; //automatic data, lifetime : 함수 시작 ~ 함수 끝
	static int y; //static data, lifetime: 프로그램 시작 ~ 프로그램 끝
}
```

## Class data type
* struct : public이 default, 관용적으로는 멤버 변수들만 포함
* class : 사용자 정의형 데이터 타입, 멤버 함수들까지 포함 가능, private 접근자
* Scope Resolution Operator (::) 
* Class에서는 객체 물려 받아서 새로운 객체 만든다. `is-a 관계` (상속)
  * Existing class: 원래 존재하던 것
  * Derived class: 새로 만든 것
  * Inheritance를 하다보면 어떤 객체를 말하는지 모호해지는 현상이 발생한다. `polymorphism`


```cpp
class DataType{
public:
  ...
	int YearIs() const; // const는 private의 variable 들을 바꾸지 않는 observe operation

private:
} // class (묘사)

DataType a; // object (실제)
```



### 구조체
* 구조체 Operation
  1. Assignment : `a = b;`
  2. Parameter
* Memory & Offset
  * 예를 들어 `CarType a;`의 `year`의 byte는 4, `maker`는 10, `price`는 모른다고 생각해보자.

  

#### Offset

| year  |  0   |
| :---: | :--: |
| maker |  4   |
| price |  14  |

#### Memory (base address : 8000)

| year  | 8000 |
| :---: | :--: |
| maker | 8004 |
| price | 8014 |

* Base Address : `a` 가 시작되는 주소
* 컴파일할 때 사용 가능하다.

  

## Parameter
* Pass by value : `void f(CarType b){...}` - 시간이 오래 걸린다.
  * Pass bye value로 동적할당 된 포인터를 넘기면 **Shallow Copy** 가 발생한다. 
  * 이는 선언이 되었어도 주소값을 같이 쓰기 때문에 원본 손상되는 결과 초래할 수 있다.
  * 공간 생성 및 해제가 가능하다.
  * 장점 : 메모리 할당량 적다.
* Pass by reference : `void f(CarType& b){...}`- 주소값만 넘기는 것
  * 참조 변수 (`DataType& variable = a;`)와 동일한 형식이라고 생각하면 된다.
  * 참조 변수는 선언과 동시에 초기화 된다.
  * 참조 변수는 주소값 `int* ptr = &x;` 과 다른 개념이다.
  * 공간 생성 따로 하지 않고 별명으로 가져다 쓰는 것이다.
* actual parameter : add (1, **2**) - 함수 호출 시 넘겨주는 것
* formal parameter : int add(int x, **int y**) - 함수 선언 시
* StackType <**float**> numStack; ⇒ actual
* template <**class ItemType**> ⇒ formal



## Generic Data Type

```cpp
class ItemType{
	compareTo();
	...
}

class List{
	ItemType A;
	...
}
```

* Generic Data Type은 어떤 데이터 타입으로도 작동하게 하는 것이다. C++에서는 template으로 구현 가능하다.
* 또한, 위 코드처럼 리스트와 데이터의 구조를 분리함으로써 구현할 수 있다.
* 이 경우  Data Type 수정 시 ItemType class만 수정해주면 된다. 함수 compareTo는 ItemType class 안에 구현한다.



