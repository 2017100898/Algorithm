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
