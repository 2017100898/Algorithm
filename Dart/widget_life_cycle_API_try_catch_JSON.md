# Widget Life-cycle, API, Try-catch, JSON
## Widget Life-cycle
### Stateless widget
* 한번 생성되면 절대 바뀌지 않는 위젯 
* 재생성 하려면 완전히 파괴하고 rebuild하는 방법 밖에 없음
	* build method 만 신경쓰면 됨

### Stateful widget
* widget의 구성요소, 속성을 지속적으로 추적하는 State object 요소와 결합
* 생명주기에 따라 각 시점에서 원하는 다양한 일들을 Stateful widget에 시킬 수 있다.
* stateless 위젯보다 좀 더 긴 생명주기를 갖는다.

### Stateful widget’s life-cycle method
1. initState method
2. build method
3. dispose method

## API (Application Programming Interface)
### 기능
1. 일련의 표준화된 명령이나 기능
	* appBar, backgroundColor, textStyle… 코딩 없이 쉽게 해결 가능.
2. 매개 역할자로써의 API
	* 비유하자면 내 통장 잔고에서 돈(data)을 꺼내기 위해서는 은행 직원(API) 에게 내 통장 잔고와 비밀번호(Key) 가 필요함.
	* API는 Key값을 확인하고 원하는 양 만큼의 데이터를 제공해 줌.

### 실행 방식
<img width="560" alt="스크린샷 2021-10-03 오전 2 10 05" src="https://user-images.githubusercontent.com/64299475/135726055-3eb3907b-9da6-4974-b01a-e415295cb202.png">
* 내가 제공한 파라미터가 유효한 경우에만 API는 데이터를 제공해 준다.


## Try-catch
* 예외 상황 처리 및 에러메시지 설정

```dart
    try {
      Position position = await Geolocator.getCurrentPosition(
          desiredAccuracy: LocationAccuracy.high);
      print(position);
    } catch (e) {
      print('There was a problem.');
    }
````


## JSON
* JSON vs XML
* XML : html 코드와 상당히 유사하지만, html은 약속된 기호만 사용 가능하고 xml 은 사용자 임의의 기호까지도 사용 가능. 
* JSON : Key-value 1:1 맵핑시키는 구조. 하지만 일일이 보고 이해하기가 쉽지 않음. 다양한 [JSON Viewer ](https://chrome.google.com/webstore/detail/json-viewer/efknglbfhoddmmfabeihlemgekhhnabb/related?hl=ko) 존재.


[YouTube 코딩셰프](https://www.youtube.com/watch?v=YqKMBQYZSmw&list=PLQt_pzi-LLfoOpp3b-pnnLXgYpiFEftLB&index=13)를 통해 공부하고 정리했습니다.