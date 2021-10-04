import 'package:flutter/material.dart';

class Model {
  Widget getWeatherIcon(int? condition) {
    if (condition == null)
      return Text(
        '🌈',
        style: TextStyle(fontSize: 65.0, fontWeight: FontWeight.w300),
      );
    else if (condition < 300) {
      return Text(
        '☁️',
        style: TextStyle(fontSize: 65.0, fontWeight: FontWeight.w300),
      );
    } else if (condition < 600) {
      return Text(
        '❄️',
        style: TextStyle(fontSize: 65.0, fontWeight: FontWeight.w300),
      );
    } else if (condition == 800) {
      return Text(
        '☀️',
        style: TextStyle(fontSize: 65.0, fontWeight: FontWeight.w300),
      );
    } else {
      return Text(
        '⛅️',
        style: TextStyle(fontSize: 65.0, fontWeight: FontWeight.w300),
      );
    }
  }

  Widget getAirIcon(int? index) {
    if (index == null)
      return Text(
        '🥰',
        style: TextStyle(fontSize: 65.0, fontWeight: FontWeight.w300),
      );
    else if (index == 1) {
      return Text(
        '☺️',
        style: TextStyle(fontSize: 50.0, fontWeight: FontWeight.bold),
      );
    } else if (index == 2) {
      return Text(
        '😯',
        style: TextStyle(fontSize: 50.0, fontWeight: FontWeight.bold),
      );
    } else if (index == 3) {
      return Text(
        '😷',
        style: TextStyle(fontSize: 50.0, fontWeight: FontWeight.bold),
      );
    } else if (index == 4) {
      return Text(
        '🤢',
        style: TextStyle(fontSize: 50.0, fontWeight: FontWeight.bold),
      );
    } else {
      return Text(
        '🤮',
        style: TextStyle(fontSize: 50.0, fontWeight: FontWeight.bold),
      );
    }
  }

  Widget getAirCondition(int? index) {
    if (index == null) {
      return Text(
        'Null',
        style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
      );
    } else if (index == 1) {
      return Text(
        '매우 좋음',
        style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
      );
    } else if (index == 2) {
      return Text(
        '좋음',
        style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
      );
    } else if (index == 3) {
      return Text(
        '보통',
        style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
      );
    } else if (index == 4) {
      return Text(
        '나쁨',
        style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
      );
    } else {
      return Text(
        '매우 나쁨',
        style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
      );
    }
  }
}
