# Callback

> 자식 위젯 Page에서 어떠한 입력 값을 넣었을 때, 부모 위젯 Page에서 그 값을 띄워주는 기능을 구현하고 싶다.  
> 하지만 어떻게? 단순히 부모 위젯의 값을 가져오는 것은 어렵지 않지만 setState 시키는 것은 callback 함수를 사용해야 한다.

* **VoidCallback**
	* 매개 변수를 사용하지 않고 값을 반환하지 않는 함수다. void callback은 자식 위젯에서 발생한 이벤트에 대해 부모위젯에게 **알릴 때** 유용하게 쓰인다.
* **FunctionalCallback**
	* 자식 위젯에서 발생한 이벤트를 부모 위젯에게 **알리고 부모 위젯에 값을 return** 하는 Callback이다.

<img width="300" src="https://user-images.githubusercontent.com/64299475/151955634-ca7727dc-82a1-4b7a-95c0-35d2bba2f7ad.png"> <img width="300" src="https://user-images.githubusercontent.com/64299475/151955642-7c8c5075-23bb-41f6-9e67-7ad9b1b41793.png"> <img width="300" src="https://user-images.githubusercontent.com/64299475/151955646-a0fd76e9-357d-4bdc-89c5-471590eda5af.png"> <img width="300" src="https://user-images.githubusercontent.com/64299475/151955652-43daf05f-563b-4b91-b315-a3dd455415e3.png">

* 전체 코드는 아래와 같으며, FunctionalCallback을 구현한 것이다.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Callback',
      theme: ThemeData(
        primarySwatch: Colors.teal,
      ),
      home: const Callback(),
    );
  }
}

// parent widget
class Callback extends StatefulWidget {
  const Callback({Key? key}) : super(key: key);

  @override
  _CallbackState createState() => _CallbackState();
}

class _CallbackState extends State<Callback> {
  String word = "none"; //✔️ 변수 초기화
 
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Callback"),
          elevation: 0.0,
        ),
        body: Center(
            child:
                Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          Text(
            word,
            style: TextStyle(color: Colors.black),
          ),
          const SizedBox(height: 30),
          GestureDetector(
              onTap: () {
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => CallbackChild(
                            callback: (value) => setState(() {
                                  word = value; //✔️ 자식 위젯에서 변화가 감지되면 부모 위젯에서 word setState (값 변경)
                                }))));
              },
              child: Container(
                  width: 100,
                  height: 30,
                  decoration: BoxDecoration(
                    color: Colors.teal,
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                  child: const Center(
                    child: Text(
                      "nextPage",
                      style: TextStyle(color: Colors.white),
                    ),
                  )))
        ])));
  }
}

//child widget
class CallbackChild extends StatefulWidget {
  const CallbackChild({Key? key, required this.callback}) : super(key: key); //✔️ 
  final Function(String) callback; //✔️ callback 함수를 입력 파라미터로 설정

  @override
  _CallbackChildState createState() => _CallbackChildState();
}

class _CallbackChildState extends State<CallbackChild> {
  late TextEditingController _controller;

  @override
  void initState() {
    _controller = TextEditingController();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Center(
      child: Container(
          width: 290,
          height: 30,
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(10.0),
            border: Border.all(width: 1),
          ),
          child: TextField(
            textAlign: TextAlign.left,
            controller: _controller,
            textInputAction: TextInputAction.search,
            decoration: InputDecoration(
              prefixIconConstraints:
                  const BoxConstraints(minWidth: 18, minHeight: 18.2),
              prefixIcon: Padding(
                padding: const EdgeInsets.only(left: 14),
                child: Container(
                  width: 26,
                  child: const Align(
                    alignment: Alignment.centerLeft,
                    child: Icon(Icons.search, size: 20),
                  ),
                ),
              ),
            ),
            onSubmitted: (value) {
              widget.callback(value); //✔️ callback 함수에 value 값 반환 (stl widget에서는 callback(value))
              Navigator.pop(context);
            },
          )),
    ));
  }
}

```



<img width="300" src="https://user-images.githubusercontent.com/64299475/151958814-eb423944-f4c4-488b-bf22-8d5498f17c96.png"><img width="300" src="https://user-images.githubusercontent.com/64299475/151958820-94d185bb-0204-4550-a718-431a9df13efc.png"><img width="300" src="https://user-images.githubusercontent.com/64299475/151958824-5142e1f4-92f5-4f4d-93b3-81bb3963da0d.png"><img width="300" src="https://user-images.githubusercontent.com/64299475/151958834-1ecad25e-b2de-450f-9852-202de82537b5.png"> 

* 네 번째 사진을 보자. 값이 변경된 이후에 자식 위젯에서 다시 부모 위젯의 word 변수에 접근하고 있다.
* 그러나 setState 해둔 "hello"가 아닌 초기값 "none"이 return 되는 것을 확인할 수 있다.
* 아래사진처럼 이전에 setState 해둔 변수를 제대로 불러오고 싶다면, 부모 위젯을 global로 만들어 구현하는 방법을 사용할 수 있다.


<img width="300" src="https://user-images.githubusercontent.com/64299475/151958826-98a0079c-94b1-47cc-873d-f113b2957555.png">

* 전체 코드는 아래와 같다.


```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Callback',
      theme: ThemeData(
        primarySwatch: Colors.teal,
      ),
      home: const Callback(),
    );
  }
}

_CallbackState ppState = new _CallbackState(); //✔️ 부모 state를 global 변수로 빼준다.

// parent widget
class Callback extends StatefulWidget {
  const Callback({Key? key}) : super(key: key);

  @override
  _CallbackState createState() => ppState;
}

class _CallbackState extends State<Callback> {
  String word = "none";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Callback"),
          elevation: 0.0,
        ),
        body: Center(
            child:
                Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          Text(
            word,
            style: TextStyle(color: Colors.black),
          ),
          const SizedBox(height: 30),
          GestureDetector(
              onTap: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => CallbackChild()));
              },
              child: Container(
                  width: 100,
                  height: 30,
                  decoration: BoxDecoration(
                    color: Colors.teal,
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                  child: const Center(
                    child: Text(
                      "nextPage",
                      style: TextStyle(color: Colors.white),
                    ),
                  )))
        ])));
  }
}

//child widget
class CallbackChild extends StatefulWidget {
  const CallbackChild({Key? key}) : super(key: key);

  @override
  _CallbackChildState createState() => _CallbackChildState();
}

class _CallbackChildState extends State<CallbackChild> {
  late TextEditingController _controller;

  @override
  void initState() {
    _controller = TextEditingController();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Center(
      child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
        Text(ppState.word),
        Container(
            width: 290,
            height: 30,
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10.0),
              border: Border.all(width: 1),
            ),
            child: TextField(
              textAlign: TextAlign.left,
              controller: _controller,
              textInputAction: TextInputAction.search,
              decoration: InputDecoration(
                prefixIconConstraints:
                    const BoxConstraints(minWidth: 18, minHeight: 18.2),
                prefixIcon: Padding(
                  padding: const EdgeInsets.only(left: 14),
                  child: Container(
                    width: 26,
                    child: const Align(
                      alignment: Alignment.centerLeft,
                      child: Icon(Icons.search, size: 20),
                    ),
                  ),
                ),
              ),
              onSubmitted: (value) {
                ppState.setState(() {
                  ppState.word = value; //✔️ 자식 위젯에서 바로 부모 위젯의 변수를 setState 시킬 수 있다.
                });
                Navigator.pop(context);
              },
            )),
      ]),
    ));
  }
}

```