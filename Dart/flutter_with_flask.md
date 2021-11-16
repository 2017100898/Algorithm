# Flutter with Flask
* Python에서 만든 Json 데이터를 Flutter 앱에서 띄우기 위해 Flask로 백엔드를 만들고 Flutter와 연결 시켰다.
* Flask는 django에 비해 가벼우며, 최소한의 기능만 제공하기 때문에 가벼운 API를 만들기에 적절하다.

## Flask
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    json_file1 = {}
    json_file1['name'] = 'hyewon'
    json_file1['age'] = '24'
    json_file1['like'] = 'coffee'

    return jsonify(json_file1)


if __name__ == '__main__':
    app.run()
```

* 127.0.0.1:5000 에 접속하면 아래와 같은 정보가 담긴 창이 뜬다.  
* `{"age":"24","like":"coffee","name":"hyewon"}`

</br>


## Flutter
```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:flutter/material.dart';

void main() async {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'New App',
      theme: ThemeData(
        primaryColor: Colors.white,
      ),
      home: MyPage(),
    );
  }
}

class MyPage extends StatefulWidget {
  const MyPage({Key? key}) : super(key: key);

  @override
  _MyPageState createState() => _MyPageState();
}

class _MyPageState extends State<MyPage> {
  var name = "None";
  var age = "None";
  var like = "None";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text('newApp')),
        body: Center(
          child: SafeArea(
              child: Container(
                  child: Column(children: [
            TextButton(
              child: Text("About me"),
              onPressed: () async {
                var url = Uri.parse('http://127.0.0.1:5000');
                var data = await getData(url);
                setState(() {
                  name = data['name'];
                  age = data['age'];
                  like = data['like'];
                });
              },
            ),
            Text("이름 : $name"),
            Text("나이 : $age"),
            Text("좋아하는 것 : $like"),
          ]))),
        ));
  }
}

Future getData(var url) async {
  http.Response response = await http.get(url);
  return jsonDecode(response.body);
}

```

* http의 get 함수를 통해 원하는 url로의 요청을 하고, Json 데이터를 파싱함으로써 앱에 정보를 띄울 수 있게 된다.
* ~~Android 앱은 주소가 10.0.2.2:40732 여야 한다는 말이 있더라~~

## Before Click
<img width="300" src="https://user-images.githubusercontent.com/64299475/142008354-ed703aeb-9869-4ddd-acb9-493ea25b3fff.png">

## After Click
<img width="300" src="https://user-images.githubusercontent.com/64299475/142008341-4ccb928e-d9d3-4716-a401-7960b181ea66.png">
