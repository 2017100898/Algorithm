# Material App with Flutter

### Flutter에서의 위젯이란?
1. UI를 만들고 구성하는 모든 기본 단위 요소 (text, icon, button…)
2. 눈에 보이지 않는 요소들까지 위젯 (center, column, padding 등의 레이아웃 정의 요소)
3. Everything is a widget

### Types of Widgets
1. **Stateless widget** : 상태가 없는 정적인 위젯, 움직임이나 변화 없음, 스크린 상에 존재만 할 뿐 아무것도 하지 않음, 어떠한 실시간 데이터도 저장하지 않음, 어떤 변화(모양, 상태)를 유발시키는 value값을 가지지 않음 (정적인 이미지, 텍스트 등)
2. **Stateful widget** : 계속 움직임이나 변화가 있는 동적인 위젯, 사용자의 interaction에 따라서 모양 바뀜, 데이터 받게 되었을 때 모양 바뀜 (text input field, 체크 리스트 등)

### Flutter widget tree
1. 위젯들은 트리 구조로 정리될 수 있음
2. 한 위젯내에 얼마든지 다른 위젯들이 포함될 수 있음
3. 위젯은 부모 위젯과 자식 위젯으로 구성
4. parent 위젯을 widget container라고 부르기도 함 

<img width="598" alt="20210717_232902" src="https://user-images.githubusercontent.com/64299475/126041090-e95d5ee6-f4e6-40c5-8732-dff5c6d81c88.png">


출처: [유튜브 코딩셰프](https://www.youtube.com/channel/UC_2ge45JCuJH1z6VYt4iCgQ)
   
   

## Text 띄우기
```dart
import 'package:flutter/material.dart';

void main() => runApp(myApp());

class myApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Project X app",
      theme: ThemeData(primarySwatch: Colors.brown),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Project X'),
        elevation: 0.0,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('안뇽?'),
            Text('안뇽?'),
            Text('안뇽?'),
          ],
        ),
      ),
    );
  }
}

```

<img src ="https://user-images.githubusercontent.com/64299475/126041109-a17fd328-7166-4348-ad4b-6434261d654b.png"  width="40%">




## Padding과 Drawer, Icon 위젯을 이용한 Material App 만들기
```dart
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

void main() => runApp(myApp());

class myApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "Citron",
      theme: ThemeData(
        primarySwatch: Colors.amber,
        fontFamily: 'Uchen',
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.amber[50],
      appBar: AppBar(
        title: Text('Citron'),
        backgroundColor: Colors.amber[600],
        centerTitle: true,
        elevation: 0.0,
        actions: [
          IconButton(
            onPressed: () {
              Navigator.push(
                  context, MaterialPageRoute(builder: (context) => cart()));
            },
            icon: Icon(Icons.shopping_cart),
          ),
          IconButton(
            onPressed: () {
              print('Search button is clicked');
            },
            icon: Icon(Icons.search),
          )
        ],
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            UserAccountsDrawerHeader(
              currentAccountPicture: CircleAvatar(
                backgroundImage: AssetImage('assets/profile.jpg'),
                backgroundColor: Colors.white,
              ),
              accountName: Text(
                'HYEWON',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15),
              ),
              accountEmail: Text('hyen@hyen.com'),
              onDetailsPressed: () {
                print('arrow is clicked');
              },
              decoration: BoxDecoration(
                color: Colors.amber,
                borderRadius: BorderRadius.only(
                  bottomLeft: Radius.circular(20.0),
                  bottomRight: Radius.circular(20.0),
                ),
              ),
            ),
            ListTile(
              leading: Icon(Icons.home),
              title: Text('Home'),
              trailing: Icon(Icons.add),
            ),
            ListTile(
              leading: Icon(Icons.question_answer),
              title: Text('Q&A'),
              trailing: Icon(Icons.add),
              onTap: () {
                Navigator.push(
                    context, MaterialPageRoute(builder: (context) => qna()));
              },
            ),
            ListTile(
              leading: Icon(Icons.settings),
              title: Text('Setting'),
              trailing: Icon(Icons.add),
            ),
          ],
        ),
      ),
      body: Padding(
          padding: EdgeInsets.fromLTRB(30.0, 40.0, 0.0, 0.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Center(
                child: CircleAvatar(
                  backgroundImage: AssetImage('assets/deden.png'),
                  radius: 100.0,
                ),
              ),
              Divider(
                height: 60.0,
                color: Colors.black,
                thickness: 1.0,
                endIndent: 30.0,
              ),
              Text(
                'NAME',
                style: TextStyle(
                  color: Colors.black,
                  letterSpacing: 2.0,
                ),
              ),
              SizedBox(
                height: 10.0,
              ),
              Text(
                'Citron',
                style: TextStyle(
                    color: Colors.black,
                    letterSpacing: 2.0,
                    fontSize: 28.0,
                    fontWeight: FontWeight.bold),
              ),
              SizedBox(
                height: 30.0,
              ),
              Text(
                'CITRON LEVEL',
                style: TextStyle(
                  color: Colors.black,
                  letterSpacing: 2.0,
                ),
              ),
              SizedBox(
                height: 10.0,
              ),
              Text(
                '14',
                style: TextStyle(
                    color: Colors.black,
                    letterSpacing: 2.0,
                    fontSize: 28.0,
                    fontWeight: FontWeight.bold),
              ),
              SizedBox(
                height: 30.0,
              ),
              Row(
                children: [
                  Icon(Icons.check_circle_outline),
                  SizedBox(
                    width: 10.0,
                  ),
                  Text(
                    'using lightsaber',
                    style: TextStyle(fontSize: 16.0, letterSpacing: 1.0),
                  ),
                ],
              ),
              Row(
                children: [
                  Icon(Icons.check_circle_outline),
                  SizedBox(
                    width: 10.0,
                  ),
                  Text(
                    'fire flames',
                    style: TextStyle(fontSize: 16.0, letterSpacing: 1.0),
                  ),
                ],
              ),
              Row(
                children: [
                  Icon(Icons.check_circle_outline),
                  SizedBox(
                    width: 10.0,
                  ),
                  Text(
                    'face hero tattoo',
                    style: TextStyle(fontSize: 16.0, letterSpacing: 1.0),
                  ),
                ],
              ),
              SizedBox(
                height: 10.0,
              ),
              Center(
                child: CircleAvatar(
                  backgroundImage: AssetImage('assets/mini.png'),
                  radius: 40.0,
                  backgroundColor: Colors.amber[50],
                ),
              ),
            ],
          )),
    );
  }
}

class cart extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Shopping Cart'),
      ),
    );
  }
}

class qna extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Q&A'),
      ),
    );
  }
}
```



<img src = "https://user-images.githubusercontent.com/64299475/126046233-5e5f0535-8ef5-4bbf-8f61-69b1edd7bd12.png" width="30%" height="30%">         <img src = "https://user-images.githubusercontent.com/64299475/126046257-1ec8d265-af66-491b-bfed-e12243fb6a43.png" width="30%" height="30%">      <img src = "https://user-images.githubusercontent.com/64299475/126046264-5a16f7cf-d3e3-488a-952e-4990d248d25c.png" width="30%" height="30%">

