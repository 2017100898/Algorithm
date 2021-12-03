# 위젯 생명주기 (Widget Life-cycle)
<img width = "400" src ="https://user-images.githubusercontent.com/64299475/144557270-ad633594-8460-4c2e-9ac7-ef151c8927eb.png">

## Stateful Lifecycle
### createState()
* 위젯을 만들자마자 바로 실행되는 함수다.

### initState
* State 값을 초기 설정하고, 최초 한 번만 실행이 된다.
* 이 단계에서는 context 가 없기에 context에 접근이 불가능하다.

```dart
@override
void initState() {
  super.initState();
}
```

### didChangeDependencies
* initState와 마찬가지로 최초 생성 때 한 번 호출이 된다.
* initState와 다르게 context에 접근을 할 수 있다.
* provider, mediaQuery 사용시에 context controll 이 필요하다.

```dart
@override
void didChangeDependencies() {
  super.didChangeDependencies();
	print(MediaQuery.of(context).size);
}
```

### build
* UI 구성하고 가장 빈번하게 호출되는 부분이다.
* 많은 양의 프로세스가 build 부분에 분포하면 앱 performance 자체가 떨어질 수 있다.
* 계산 많이 하는 부분은 build 보다는 최초 한번만 처리하도록 만드는 것이 좋다.

### setState
* 상태가 바뀔 때마다 setState를 호출할 수 있다.

```dart
@override
void setState(VoidCallback fn) {
   super.setState(fn);
}
```

### didUpdateWidget
* 부모 위젯이 변경되어 해당 위젯을 재빌드해야하는 경우 initState() 대신 사용된다.

```dart
@override
void didUpdateWidget(covariant mainPage oldWidget) {
  super.didUpdateWidget(oldWidget);
}
```

### dispose
* 제거될 때 호출되는 함수다.
```dart
@override
void dispose() {
  super.dispose();
}
```