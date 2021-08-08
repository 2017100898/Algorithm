import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/widgets.dart';

class Search extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Center(
            child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
          Icon(Icons.search, size: 100.0, color: Colors.grey[500]),
          Text(
            '전체 게시판의 글을 검색해보세요',
            style: TextStyle(
                fontSize: 20.0,
                color: Colors.grey[500],
                fontWeight: FontWeight.bold),
          )
        ])));
  }
}
