# Dart 언어의 문법
* 🎯 Flutter로 어플을 만들기 위해 dart를 공부해 보자!
* [Dartpad](https://dartpad.dev/?null_safety=true)를 사용하여 웹사이트에서 바로 dart를 실행시킬 수 있다.   


## Hello Dart

```dart
void main(){
  print("Hello Dart!"); //Hello Dart!  
}
```

## 변수

```dart
void main(){
  int num1 = 1;
  print(num1); //1
  
  double num2 = 2.1;
  print(num2); //2.1
  
  var num3 = 3; //Dart가 data type 유추하도록 함
  print(num3); //3
  
  var a = true;
  print(a); //true
}
```
* 실수형 var 변수에 정수 값 저장하는 것은 괜찮으나 정수형 var 변수에 실수 값을 저장하려고 하면 에러가 발생한다. 
* 이때 dynamic 타입으로 해결 가능하다.

```dart
void main(){

  dynamic num = 1;
  num = 2.3;
  print(num); //2.3
  
}
```

## List, Set, Map

```dart
void main() {
  var list1 = [1,2,3];
  var set1 = {'A','B','C','E','Z','Z'};
  var map1 = {1:'Pasta', 2:'Pizza'};
  
  print(list1); //[1, 2, 3]
  print(set1); // {A, B, C, E, Z}
  print(map1); //{1: Pasta, 2: Pizza}
}
```

* **list**: 동일한 데이터 타입 데이터를 여러 개 저장한다.
* **set**: 중복된 데이터가 없도록 하며 중괄호 {}를 사용한다. 순서는 의미가 없다.
* **map**: key값과 그에 상응하는 value 값을 함께 저장하며, 괄호 형태는 상관 없다.


```dart
void main() {
  List<int> list = [3, 1, 5];
  print(list); //[3,1,5]
  
  List<dynamic> list1 = ['a',2,"Bear", 42.1];
  print(list1); //[a, 2, Bear, 42.1]
  
  var list2 = ['a', 2, "Bear", 42.1];
  print(list2); //[a, 2, Bear, 42.1]
  print(list2.toString()); //[a, 2, Bear, 42.1]
}
```

* data type을 지정해주는 List<int> 등을 통해 List를 선언할 수 있다.
* List<dynamic>을 이용하면 서로 다른 타입의 element를 대입할 수 있다.
* var을 이용하면 타입을 따로 지정하지 않아도 추측해서 사용할 수 있다.

## Function

```dart
void main() {
  var student = Student();
  print(student.name);
}

class Student{
  String name = "Kim";
}
```

## if, else if, else
```dart
void main() {
  int grade = 84;
 
  if(grade>=90){
    print('A');
  }
  
  else if(grade>=80 && grade<90){
    print('B');
  }
  
  else if(grade>=70 && grade<80){
    print('C');
  }
  
  else{
    print('F');
  }
}
```


## Class

```dart
class Point{
  var x;
  var y;
}

void main(){
  var point1 = Point();
  print("[01]\$ point1 is (${point1.x}, ${point1.y})");
  //[01]$ point1 is (null, null)
}
```

* 초기화 하지 않아서 null 값을 가지며, 저장을 안 하고 있는 상태라서 Null을 반환한다.

```dart
class Point{
  var x;
  var y;
}

void main(){
  Point point1;
  print("[01]\$ point1 is (${point1.x}, ${point1.y})");
  //Error
}
```

* Point Class 저장을 하고 있는 상태라서 Error가 발생한다.

### method1
```dart
class Point{
  var x;
  var y;
}

void main(){
  var point1 = Point();
  point1.x = 4;
  point1.y = 5;
  print("[01]\$ point1 is (${point1.x}, ${point1.y})");
  //[01]$ point1 is (4, 5)
}
```

### method2
``` dart
class Point{
  var x;
  var y;
  
  Point(var numX, var numY){
    this.x = numX;
    this.y = numY;
  }
}

void main(){
  var point1 = Point(4, 5);
  print("[01]\$ point1 is (${point1.x}, ${point1.y})");
  //[01]$ point1 is (4, 5)
}
```

## 초기화
```dart
class Point{
  var x;
  var y;
  
  Point([var numX = 0, var numY=0]){
    this.x = numX;
    this.y = numY;
  }
}

void main(){
  var point1 = Point();
  print("[01]\$ point1 is (${point1.x}, ${point1.y})");
  //[01]$ point1 is (0, 0)
}
```


* constructor (초기화)를 만들지 않을 때는 자동으로 입력 파라미터가 없는 constructor 생성한다.  
* 개발자가 constructor 만들면 dart는 기본 default constructor 생성 하지 않는다.   

## constructor
```dart
class Point{
  var x;
  var y;
  
  Point([var numX = 0, var numY=0]){
    this.x = numX;
    this.y = numY;
  }
  
  Point.fromPoint(Point origin){
    this.x = origin.x;
    this.y = origin.y;
  }
}

void main(){
  var point1 = Point(3, 4);
  print("[01]\$ point1 is (${point1.x}, ${point1.y})");
  //[01]$ point1 is (3, 4)
  
  var point2 = Point.fromPoint(point1);
  print("[02]\$ point2 is (${point2.x}, ${point2.y})");
  //[02]$ point2 is (3, 4)
}
```
* **클래스이름.식별자이름**의 방식으로 또 다른 constructor를 만들 수 있다.


## Get & Set
```dart
class Point{
  var x;
  var y;
  
  Point([var numX = 0, var numY=0]){
    this.x = numX;
    this.y = numY;
  }
  
  Point.fromPoint(Point origin){
    this.x = origin.x;
    this.y = origin.y;
  }
  
  String get stringify => "(${this.x}, ${this.y})";
  set setX(num numX) => this.x = numX;
  set setY(num numY) => this.y = numY;
}

void main(){
  var point1 = Point();
  point1.setX = 3;
  point1.setY = 4;
  print("[01]\$ point1 is " + point1.stringify);
  //[01]$ point1 is (3, 4)

}

```
  
## 선택 및 필수 Input

```dart
void main() {
  var student = something();
  print(student);
  //hong
}

String something({String names = 'hong'}) {
  return names;
}

```
* method 입력 값이 옵션이면 변수 양 옆에 {} 표시   

```dart
void main() {
  var student = something('kim');
  print(student);
  //kim
}

String something(@required String names) {
  return names;
}
```
입력값 꼭 필요할 때는 변수명 앞에 @require 표시
  
 ## List 연결
```dart
void main() {
  var items = [1, 2, 3];
  var items2 = [...items, 4, 5];
  print(items2);
  //[1, 2, 3, 4, 5]
}
```

* ...으로 list 연결할 수 있다. 
* 앞 뒤 중간 어디든 상관 없이 가능.




## 타입확인과 타입캐스트
```dart
void main() {
  var a = 10;

  /*타입확인*/
  if (a is int) {
    print('정수');
  } else {
    print('정수가 아닙니다');
  }
  //정수

  /*타입캐스트*/
  var b;
  print(b ?? 'X'); 
  //X
  print(b?.toLowerCase()); 
  //null
}
```

* null일 때 기본값 설정시 ?? 활용   
* null이 아닐 때만 함수 실행하고 싶으면 ? 활용
