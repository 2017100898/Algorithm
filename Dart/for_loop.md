# For loop
## For loop 구조
```dart
void main() {
  for (int i = 0; i < 5; i++) {
    print('${i + 1}');
  }
}

//1
//2
//3
//4
//5
```


```dart
void main() {
  for (int i = 0; i < 10; i+=3) {
    print('${i + 1}');
  }
}

//1
//4
//7
//10
```

```dart
void forward(int move){
  for(int i = 1; i <= move; i++){
    print('$i칸 이동했습니다.');
  }
}

void main(){
  forward(5);
}
```


## For in loop 
```dart
void main(){
  List<String> rainbow = ['빨', '주', '노', '초', '파', '남', '보'];
  
  for(int i = 0; i<rainbow.length; i++){
    print(rainbow[i]);
  }
}
```

```dart
void main(){
  List<String> rainbow = ['빨', '주', '노', '초', '파', '남', '보'];
  
  for(String x in rainbow){
    print(x);
  }
}
```

## forEach loop
```dart
void main(){
  List<String> rainbow = ['빨', '주', '노', '초', '파', '남', '보'];
  
  rainbow.forEach((name){
    print(name);
  });
  
}
```

## for loop, for in loop 활용
```dart
import 'dart:math';
  
List<int> lottoNumber(){
  var random = Random();
  List<int> lottoList = [];
  var num;
  
  for(int i = 0; i<6; i++){
    num = random.nextInt(45)+1;
    lottoList.add(num);
  }
  
  print('당첨번호');
  print(lottoList);
  
  return lottoList;
}
  
List<int> myNumber(){
  var random = Random();
  List<int> myList = [];
  var num;
  
  for(int i = 0; i<6; i++){
    num = random.nextInt(45)+1;
    myList.add(num);
  }
  
  print('내 추첨번호');
  print(myList);
  
  return myList;
}

void checkNumber(lottoList, myList){
  
  int match = 0;
  
  for(int lotto in lottoList){
    for(int myNum in myList){
      
      if(lotto == myNum){
        match++;
        print('내 추첨번호 = $myNum');
      }
      //print('로또번호 = $lotto');
      
    }
  }
  
  print('$match개의 당첨번호가 있습니다!');
}

void main(){
  
  List<int> lottoFinal = lottoNumber();
  List<int> myFinal = myNumber();
  checkNumber(lottoFinal, myFinal);
  
}

/*
당첨번호
[18, 38, 35, 21, 30, 14]
내 추첨번호
[14, 28, 44, 18, 42, 23]
내 추첨번호 = 18
내 추첨번호 = 14
2개의 당첨번호가 있습니다!
*/
  
```

* 하지만 이 프로그램은 중복을 허용하는 단점을 지닌다.

## Set while
* Set은 중복을 허용하지 않는다.
* Set<int> rainbow = {1,2,3,4,5,6}
* 숫자 개수 일정하게 맞춰주기 위해서는 while loop 사용 가능

```dart
import 'dart:math';
  
Set<int> lottoNumber(){
  var random = Random();
  final Set<int> lottoSet = {};
  var num;
  
  while(lottoSet.length != 6){
    lottoSet.add(random.nextInt(45)+1);
  }
  
  print('당첨번호');
  print(lottoSet.toList());
  
  return lottoSet;
}
  
Set<int> myNumber(){
  var random = Random();
  Set<int> mySet = {};
  var num;
  
  while(mySet.length != 6){
    mySet.add(random.nextInt(45)+1);
  }
  
  print('내 추첨번호');
  print(mySet.toList());
  
  return mySet;
}

void checkNumber(lottoSet, mySet){
  
  int match = 0;
  
  for(int lotto in lottoSet){
    for(int myNum in mySet){
      
      if(lotto == myNum){
        match++;
        print('내 추첨번호 = $myNum');
      }
      //print('로또번호 = $lotto');
      
    }
  }
  
  print('$match개의 당첨번호가 있습니다!');
}

void main(){
  
  Set<int> lottoFinal = lottoNumber();
  Set<int> myFinal = myNumber();
  checkNumber(lottoFinal, myFinal);
  
}
```

## list.generate
* dummy data 생성 시 사용
* `List<int>.generate(10, (i) => i+1)` : 1~10 데이터 생성
* `shuffle()` 함수  

```dart
List<int> lottoNumber(){
  
  var number = (List<int>.generate(45, (i) => i+1)..shuffle()).sublist(0, 6);
  
  print('당첨번호');
  print(number);
  
  return number;
}
  
List<int> myNumber(){
  var number2 = (List<int>.generate(45, (i) => i+1)..shuffle()).sublist(0, 6);
  
  print('내 추첨번호');
  print(number2);
  
  return number2;
}

void checkNumber(number, number2){
  
  int match = 0;
  
  for(int lotto in number){
    for(int myNum in number2){
      
      if(lotto == myNum){
        match++;
        print('내 추첨번호 = $myNum');
      }
      
    }
  }
  
  print('$match개의 당첨번호가 있습니다!');
}

void main(){
  
  List<int> lottoFinal = lottoNumber();
  List<int> myFinal = myNumber();
  checkNumber(lottoFinal, myFinal);
  
}
```