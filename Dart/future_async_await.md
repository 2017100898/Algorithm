# Future, async, await
## Future 
* 우리는 주문 영수증으로 햄버거를 받을 수 있다.
* 그래서 햄버거를 받을 때까지 다른 일을 할 수 있다.
* 그러나 영수증은 궁극적으로 우리가 원하는 것은 아니며, 곧 햄버거를 받을 수 있다는 약속이다.
* **Future은 미래에 String, int, image 등 구체적이고 실제적인 객체로 반환될 것임을 의미함.** (= 주문 영수증)
* **Future<>** -> 우리가 어떤 결과물 받아야할지 미리 지정해줄 수 있음 -> **Future<String>**
* Future 클래스는 비동기 작업을 할 때 사용
* 일정 소요시간 후에 실제 데이터나 에러를 반환

## async
* Synchronous : 해야할 일 오직 하나만 하는 것.
* Asynchronous : 여러가지 일 동시에 하는 것. (ex. 짜장면, 짬뽕, 볶음밥 동시에 만듦)
* async 클래스는 await 메서드를 가지고 있음


### Synchronous
```dart
import 'dart:io';

void main() {
  showData();
}

void showData() {
  startTask();
  accessData();
  fetchData();
}

void startTask() {
  String info1 = '요청수행 시작';
  print(info1);
}

void accessData() {
  Duration time = Duration(seconds: 3);
  sleep(time); // 코드들이 Synchronous하게 실행 됨.
  String info2 = '데이터에 접속중';
  print(info2);
}

void fetchData() {
  String info3 = '잔액은 8,500만원입니다.';
  print(info3);
}
```

> 요청수행 시작  
> _((((duration))))_  
> 데이터에 접속중  
> 잔액은 8,500만원입니다.  

### Asynchronous
```dart
void main() {
  showData();
}

void showData() {
  startTask();
  accessData();
  fetchData();
}

void startTask() {
  String info1 = '요청수행 시작';
  print(info1);
}

void accessData() {
  Duration time = Duration(seconds: 4);

  if (time.inSeconds > 2) {
    Future.delayed(time, () { //Future.delayed 만나면 밑으로 내려 갔다가 옴
      String info2 = '데이터 처리 완료';
      print(info2);
    });
  } else {
    String info2 = '데이터를 가져왔습니다.';
    print(info2);
  }
}

void fetchData() {
  String info3 = '잔액은 8,500만원입니다.';
  print(info3);
}
```

> 요청수행 시작  
> 잔액은 8,500만원입니다.  
> _((((duration))))_  
> 데이터 처리 완료  

```dart
void main() {
  showData();
}

void showData() {
  startTask();
  String account = accessData();
  fetchData(account);
}

void startTask() {
  String info1 = '요청수행 시작';
  print(info1);
}

String accessData() {
  String account = '0';
  Duration time = Duration(seconds: 3);

  if (time.inSeconds > 2) {
    Future.delayed(time, () {
      account = '8,500만원';
      print(account);
    });
  } else {
    String info2 = '데이터를 가져왔습니다.';
    print(info2);
  }

  return account;
}

void fetchData(String account) {
  String info3 = '잔액은 $account입니다.';
  print(info3);
}

```

> 요청수행 시작  
> 잔액은 0입니다.  
> _((((duration))))_  
> 8,500만원  

```dart
void main() {
  showData();
}

void showData() async {
  startTask();
  String account = await accessData();
  fetchData(account);
}

void startTask() {
  String info1 = '요청수행 시작';
  print(info1);
}

Future<String> accessData() async {
  String account = '0';
  Duration time = Duration(seconds: 3);

  if (time.inSeconds > 2) {
    await Future.delayed(time, () {
      account = '8,500만원';
      print(account);
    });
  } else {
    String info2 = '데이터를 가져왔습니다.';
    print(info2);
  }

  return account;
}

void fetchData(String account) {
  String info3 = '잔액은 $account입니다.';
  print(info3);
}
```

> 요청수행 시작  
> _((((duration))))_  
> 8,500만원  
> 잔액은 8,500만원입니다.  

## await
* 작업이 처리될 때까지 좀 기다리라는 뜻
* await로 선언된 메서드는 응답이 처리될 때까지 대기