# Making cute cheery container ui
```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Cherry',
      theme: ThemeData(
        primaryColor: Colors.white,
      ),
      home: MyCherry(),
    );
  }
}

class MyCherry extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: Container(
            height: 150,
            width: 150,
            decoration: BoxDecoration(
              color: Colors.grey.shade100,
              borderRadius: BorderRadius.circular(100.0),
              boxShadow: [
                BoxShadow(
                  color: Colors.grey.shade400,
                  spreadRadius: 3,
                  blurRadius: 13,
                  offset: Offset(4, 4),
                ),
              ],
            ),
            child: Center(
                child: Text(
              '🍒',
              style: TextStyle(fontSize: 55),
            ))),
      ),
    );
  }
}


```

<img src ="https://user-images.githubusercontent.com/64299475/133930254-f25e03b8-73ce-4b7f-84fe-2fe810820e41.png"  width="40%">