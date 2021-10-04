import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:timer_builder/timer_builder.dart';
import 'package:intl/intl.dart';
import 'package:weather/model/model.dart';

class WeatherScreen extends StatefulWidget {
  WeatherScreen({this.parseWeatherData, this.parseAirPollution});
  final dynamic parseWeatherData;
  final dynamic parseAirPollution;

  @override
  _WeatherScreenState createState() => _WeatherScreenState();
}

class _WeatherScreenState extends State<WeatherScreen> {
  late Model model = Model();
  String? cityName;
  double? temp;
  var date = DateTime.now();
  late Widget icon;
  String? des;
  late Widget airIcon;
  late Widget airState;
  double? dust1;
  double? dust2;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    updateData(widget.parseWeatherData, widget.parseAirPollution);
  }

  void updateData(dynamic weatherData, dynamic airData) {
    double temp2 = weatherData['main']['temp'];
    temp = temp2;
    int condition = weatherData['weather'][0]['id'];
    des = weatherData['weather'][0]['description'];
    int index = airData['list'][0]['main']['aqi'];
    dust1 = airData['list'][0]['components']['pm10'];
    dust2 = airData['list'][0]['components']['pm2_5'];
    cityName = weatherData['name'];
    icon = model.getWeatherIcon(condition);
    airIcon = model.getAirIcon(index);
    airState = model.getAirCondition(index);
  }

  String getSystemTime() {
    var now = DateTime.now();
    return DateFormat("h:mm a").format(now);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
            backgroundColor: Colors.white,
            elevation: 0.0,
            leading: IconButton(
              icon: Icon(
                Icons.near_me,
                color: Colors.indigoAccent[200],
              ),
              onPressed: () {},
              iconSize: 30.0,
            ),
            actions: [
              IconButton(
                icon: Icon(
                  Icons.location_searching,
                  color: Colors.indigoAccent[200],
                ),
                onPressed: () {},
                iconSize: 30.0,
              ),
            ]),
        body: Container(
          child: Stack(
            children: [
              Container(
                  padding: EdgeInsets.all(20.0),
                  child: Column(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Expanded(
                          child: Column(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    SizedBox(
                                      height: 130.0,
                                    ),
                                    Text(
                                      '$cityName',
                                      style: TextStyle(
                                          fontSize: 35.0,
                                          fontWeight: FontWeight.bold,
                                          color: Colors.indigo),
                                    ),
                                    Row(
                                      children: [
                                        TimerBuilder.periodic(
                                          Duration(minutes: 1),
                                          builder: (context) {
                                            print('${getSystemTime()}');
                                            return Text('${getSystemTime()}',
                                                style:
                                                    TextStyle(fontSize: 16.0));
                                          },
                                        ),
                                        Text(DateFormat(' - EEEE').format(date),
                                            style: TextStyle(fontSize: 16.0)),
                                        Text(
                                            DateFormat(' - d MMM, yyyy')
                                                .format(date),
                                            style: TextStyle(fontSize: 16.0))
                                      ],
                                    )
                                  ],
                                ),
                                Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      '$temp\u2103',
                                      style: TextStyle(
                                          fontSize: 65.0,
                                          fontWeight: FontWeight.w300,
                                          fontStyle: FontStyle.italic),
                                    ),
                                    Row(
                                      children: [
                                        icon,
                                        SizedBox(width: 10.0),
                                        Text(
                                          '$des',
                                          style: TextStyle(
                                              fontSize: 16.0,
                                              fontWeight: FontWeight.w400),
                                        ),
                                      ],
                                    )
                                  ],
                                )
                              ]),
                        ),
                        Column(
                          children: [
                            Divider(
                              height: 15.0,
                              thickness: 2.0,
                            ),
                            Row(
                                mainAxisAlignment:
                                    MainAxisAlignment.spaceBetween,
                                children: [
                                  Column(
                                    children: [
                                      Text(
                                        'AQI(대기질지수)',
                                        style: TextStyle(
                                            fontSize: 16.0,
                                            fontWeight: FontWeight.bold),
                                      ),
                                      SizedBox(
                                        height: 10.0,
                                      ),
                                      airIcon,
                                      SizedBox(
                                        height: 10.0,
                                      ),
                                      airState,
                                    ],
                                  ),
                                  Column(
                                    children: [
                                      Text(
                                        '미세먼지',
                                        style: TextStyle(
                                            fontSize: 16.0,
                                            fontWeight: FontWeight.bold),
                                      ),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      Text(
                                        '$dust1',
                                        style: TextStyle(
                                            fontSize: 35.0,
                                            fontWeight: FontWeight.bold),
                                      ),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      Text(
                                        '㎍/㎥',
                                        style: TextStyle(
                                            fontSize: 16.0,
                                            fontWeight: FontWeight.bold),
                                      ),
                                    ],
                                  ),
                                  Column(
                                    children: [
                                      Text(
                                        '초미세먼지',
                                        style: TextStyle(
                                            fontSize: 16.0,
                                            fontWeight: FontWeight.bold),
                                      ),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      Text(
                                        '$dust2',
                                        style: TextStyle(
                                            fontSize: 35.0,
                                            fontWeight: FontWeight.bold),
                                      ),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      Text(
                                        '㎍/㎥',
                                        style: TextStyle(
                                            fontSize: 16.0,
                                            fontWeight: FontWeight.bold),
                                      ),
                                    ],
                                  ),
                                ])
                          ],
                        )
                      ])),
            ],
          ),
        ));
  }
}
