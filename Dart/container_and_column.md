# Container
* Container widget은 페이지 내에서 최대한의 공간을 차지한다.
* 하지만, child를 갖게 되면 그 child의 크기로 줄어든다.
* **Container는 오직 하나의 child 만 갖는다.**

## SafeArea & margin
```dart
class MyPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: Container(
          color: Colors.pink,
          child: Text('Hello'),
          width: 100,
          height: 100,
          margin: EdgeInsets.all(20),
        ),
      ),
    );
  }
}
```

* margin을 아래처럼 구체적으로 지정해줄 수도 있다.

```dart
            margin: EdgeInsets.symmetric(
              vertical: 80,
              horizontal: 20,
            )
```

<img height=300 src = "https://user-images.githubusercontent.com/64299475/133656042-0fc88d10-bf26-401f-a034-b7143a25a6e7.png">

* Box 내의 Text를 Box 경계선으로 부터 띄우기 위해서는 padding을 사용한다.

```dart
padding: EdgeInsets.all(20)
```



# Column Widget
* Column 위젯은 여러 children을 가진다.

## Container 정중앙(center) 배치
```dart
class MyPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        body: SafeArea(
            child: Center(
                child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
              width: 100,
              height: 100,
              color: Colors.pinkAccent,
              child: Text('Container 1'),
            ),
            Container(
              width: 100,
              height: 100,
              color: Colors.yellowAccent,
              child: Text('Container 2'),
            ),
            Container(
              width: 100,
              height: 100,
              color: Colors.indigo,
              child: Text('Container 3'),
            ),
          ],
        ))));
  }
}

```



* Center() 와 mainAxisAlignment를 동시에 실행해야 Container를 정중앙에 배치할 수 있다.

<img height=300 src = "https://user-images.githubusercontent.com/64299475/133655861-95389bb4-6ef8-4dd5-bc1f-98ef8d136749.png">

* mainAxisAlignment 대신 `mainAxisSize: MainAxisSize.min`을 사용하면 Container들이 상하의 통제권을 확보할 수 있다.
* `verticalDirection: VerticalDirection.up` 은 Container들의 정렬 순서를 위에서 아래로 만든다.
* `mainAxisAlignment: MainAxisAlignment.spaceEvenly` 을 사용하면 세 Container가 정확히 같은 간격으로 떨어지게 된다.



## Container 오른쪽 정렬
```dart
class MyPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        body: SafeArea(
            child: Center(
                child: Column(
          verticalDirection: VerticalDirection.up,
          crossAxisAlignment: CrossAxisAlignment.end,
          children: <Widget>[
            Container(
              width: 100,
              height: 100,
              color: Colors.pinkAccent,
              child: Text('Container 1'),
            ),
            Container(
              width: 100,
              height: 100,
              color: Colors.yellowAccent,
              child: Text('Container 2'),
            ),
            Container(
              width: 400,
              height: 100,
              color: Colors.indigo,
              child: Text('Container 3'),
            ),
            Container(
              width: double.infinity,
            )
          ],
        ))));
  }
}
```

* `crossAxisAlignment: CrossAxisAlignment.end`와 **Invisible Container**를 통해 Container를 오른쪽 정렬할 수 있다.

<img height=300 src = "https://user-images.githubusercontent.com/64299475/133655822-48246586-2026-4a8a-8b4d-a076c0cd208d.png">

## 가로방향으로 화면 채우기
```dart
class MyPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        body: SafeArea(
            child: Center(
                child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            Container(
              height: 100,
              color: Colors.pinkAccent,
              child: Text('Container 1'),
            ),
            Container(
              height: 100,
              color: Colors.yellowAccent,
              child: Text('Container 2'),
            ),
            Container(
              height: 100,
              color: Colors.indigo,
              child: Text('Container 3'),
            ),
          ],
        ))));
  }
}
```

* `crossAxisAlignment: CrossAxisAlignment.stretch`을 통해 가로 방향으로 Container를 늘릴 수 있다. 이때 각 Container의 width는 삭제한다.

```dart
children: <Widget>[
            Container(
              height: 100,
              color: Colors.pinkAccent,
              child: Text('Container 1'),
            ),
            SizedBox(height: 30.0),
            Container(
              height: 100,
              color: Colors.yellowAccent,
              child: Text('Container 2'),
            ),
            Container(
              height: 100,
              color: Colors.indigo,
              child: Text('Container 3'),
            ),
          ],

```

* Container 사이의 간격을 띄우고 싶다면 **SizedBox**를 활용할 수 있다.

<img height=300 src = "https://user-images.githubusercontent.com/64299475/133655732-9f8d8bab-8c84-4df4-b10e-3d4c35e2e10c.png">