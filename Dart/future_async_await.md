# Future, async, await

## Thread
* 프로세스 내에서 실행되는 흐름의 단위
* 실질적인 앱의 동작을 담당하는 것
* 프로그램 : 생명이 없는 것 (ex. Photoshop - 깔려있을 뿐, 실행했을 때만 작동)
* 프로세스 : 생명이 있는 것 (ex. Photoshop 실행 후 -> 프로세스 실행)
* Dart는 **싱글 스레드**로 운영되는 언어
	* 한 번에 오직 하나의 작업만 실행하며, 이 작업이 실행되는 동안 코드 상에 존재하는 다른 작업들이 개입할 여지가 없다.
* Dart는 Event loop을 통해 무리 없이 앱 실행함.
	1. 명령 실행되면 FIFO 방식으로 Queue(대기열)에 **MicroTask**(짧은 시간동안 비동기적으로 먼저 실행되고 끝나는 작은 작업)와 **Event**(Button tap, Future, Stream, Reading files 등의 이벤트 순서대로 처리) 준비
	2. main 함수 실행
	3. Eventloop 실행 : 순서대로 대기열에 있는 MicroTask와 Event 처리

## Future 
* **비동기 방식으로 미래에 어느 시점에 완성되어 실제적인 데이터가 되거나 에러를 반환하는 객체**
* 우리는 주문 영수증으로 햄버거를 받을 수 있다.
* 그래서 햄버거를 받을 때까지 다른 일을 할 수 있다.
* 그러나 영수증은 궁극적으로 우리가 원하는 것은 아니며, 곧 햄버거를 받을 수 있다는 약속이다.
* **Future은 미래에 String, int, image 등 구체적이고 실제적인 객체로 반환될 것임을 의미함.** (= 주문 영수증)
* **Future<>** -> 우리가 어떤 결과물 받아야할지 미리 지정해줄 수 있음 -> **Future<String>**
* Future 클래스는 비동기 작업을 할 때 사용
* 일정 소요시간 후에 실제 데이터나 에러를 반환

> 1. 다트에 의해서 Future 객체가 내부적인 배열에 등록
> 2. Future 관련하여 실행되어야하는 코드들이 이벤트 큐에 등록
> 3. 불완전한 Future 객체 반환
> 4. **Synchronous 방식으로 실행되어야할 코드 먼저 실행**
> 5. 최종적으로 실제적인 data값이 future 객체로 전달

### 예시
```dart
void main(){
  
  print('Before the Future');
  Future((){
    print('Running the Future');//잠시 후에 처리하기 위해 건너뜀
  }).then((_){
    print('Future is complete');//Future 이후에 실행되므로 건너뜀
  });
  print('After the Future'); 
  
}
  
/* Result
Before the Future
After the Future
Running the Future
Future is complete
*/
```


## async (비동기)
* async 클래스는 await 메서드를 가지고 있음
* 이 메서드를 통해 나오는 결과물은 Future
* Await 키워드 만날 때까지 Synchronous 방식으로 코드 처리
* Await 키워드 만나면 Future 완료될 때까지 대기
* Future 완료되자마자 그 다음 코드들을 실행


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


[Youtube 코딩셰프](https://www.youtube.com/watch?v=HjhPhAUPHos&list=PLQt_pzi-LLfoOpp3b-pnnLXgYpiFEftLB&index=12)를 통해 공부하고 정리했습니다. 🐢
