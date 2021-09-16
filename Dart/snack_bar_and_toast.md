# BuildContext
* Widget tree에서 현재 widget의 위치 알 수 있는 정보
	* context를 넣어서 Scaffold를 return 한다.
* 모든 Widget은 자신만의 BuildContext를 갖고 있다.
* 모든 Widget은 함수를 갖고 있고 계층 구조를 만들어 나간다.

```dart
Widget build(BuildContext context){
	return Scaffold(
	~
)
}
```

* 위 코드에서, Widget이 Build 함수의 type 이고, context 라는 BuildContext type의 인자값을 대입하면 Scaffold를 return 한다.

# Snack bar 와 BuildContext
* Snackbar : 스크린 하단에 간단한 메세지 띄우는 기능

### Scaffold.of(context) method
* 현재 주어진 context에서 위로 올라가면서 가장 가까운 Scaffold 찾아서 반환하라.
* somthing.of(context) 의 형식
* Context는 BuildContext class의 instance

### Snackbar 구현
```dart
class cart extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Shopping Cart'),
      ),
      body: Center(
        child: TextButton(
          child: Text(
            'Click',
            style: TextStyle(color: Colors.black),
          ),
          onPressed: () {
            ScaffoldMessenger.of(context)
                .showSnackBar(SnackBar(content: Text("Cart가 비어있습니다!")));
          },
        ),
      ),
    );
  }
}
```

<img width="398" src = "https://user-images.githubusercontent.com/64299475/133646293-cc6de939-b2a4-4fb4-b29b-c52363878339.png">

# Toast
```dart
class cart extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Shopping Cart'),
      ),
      body: Center(
        child: TextButton(
          child: Text(
            'Click',
            style: TextStyle(color: Colors.black),
          ),
          onPressed: () {
            flutterToast();
          },
        ),
      ),
    );
  }
}

void flutterToast() {
  Fluttertoast.showToast(
      msg: 'Cart가 비어있습니다!',
      gravity: ToastGravity.BOTTOM,
      backgroundColor: Colors.grey,
      fontSize: 16.0,
      textColor: Colors.white,
      toastLength: Toast.LENGTH_SHORT);
}
```



<img width="398" src = "https://user-images.githubusercontent.com/64299475/133646276-901208cc-c188-485d-8192-cce94a16b5b6.png">

