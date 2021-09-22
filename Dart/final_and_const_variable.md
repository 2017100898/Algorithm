# final and const variable
* 변수값이 한 번 초기화 되면 바꿀 수 없게 하는 제어자

## 변수
```dart
void main() {
  int age;
  age = 20;
}
```

* 컴파일러가 메모리에 20이라는 숫자 저장하게 됨.
* _0x00A3FC00 <==== age_ (20이라는 숫자 저장된 메모리 Point)

```dart
void main() {
  int age;
  age = 20;
  age = 50;
}
```

* 예전 주소 위에 새롭게 50 가리키기 위한 주소 덮어 씌움.


```dart
void main() {
  
  final int myFinal = 30;
  const int myConst = 70;
  // final과 const 같은 키워드를 제어자(modifier)라고 함.

  myFinal = 20; //error
  myConst = 60; //error

}
```


## Final 변수
* 오직 한 번만 설정할 수 있다.
* 초기화 방법
	1. 변수 선언 시 초기화 하는 것
	2. 객체 생성 시 외부 데이터 받아서 생성자 통해 초기화하는 것
	
```dart
 class Person{
   final int age;
   String name;
   Person(this.age, this.name);
 }

void main(){
  Person p1 = new Person(20, "Kim");
  print(p1.age);
}
```

## Const 변수
* 컴파일 시점에 상수가 된다. 값이 이미 초기화되어 있어야 한다.
* const 변수는 선언과 동시에 초기화.

```dart
void main() {
  const time = DateTime.now(); //error
}
```

```dart
void main() {
  final time = DateTime.now(); //ok
}
```


[YouTube 코딩셰프](https://www.youtube.com/watch?v=StvbitxUKSo&list=PLQt_pzi-LLfoOpp3b-pnnLXgYpiFEftLB&index=1)를 참고하여 공부하고 정리했습니다.