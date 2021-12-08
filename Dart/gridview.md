# GridView
## GridView.builder
* 1열로 위젯을 나열하는 [리스트뷰 (ListView)](https://github.com/2017100898/TIL/blob/main/Dart/listview.md)와 다르게 GridView는 2열 이상으로 위젯을 나열할 때 사용하는 위젯이다.
* 클릭 시 아이콘의 색이 변하는 Stateful 한 예시를 만들어 보았다.

<img width="300" src="https://user-images.githubusercontent.com/64299475/145163086-e2915b36-0631-4ed1-8fec-d1765f4871e8.png"> <img width="300" src="https://user-images.githubusercontent.com/64299475/145163073-5535526e-0c13-4d7f-ad40-129c742fb952.png">


```dart
lass MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Gridview',
      theme: ThemeData(
          primarySwatch: Colors.purple,
          visualDensity: VisualDensity.adaptivePlatformDensity),
      home: MyHomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          title: Text("GridView"),
          foregroundColor: Colors.grey,
          backgroundColor: Colors.white,
        ),
        body: gridviewEx());
  }
}

class gridviewEx extends StatefulWidget {
  const gridviewEx({Key? key}) : super(key: key);

  @override
  _gridviewExState createState() => _gridviewExState();
}

class _gridviewExState extends State<gridviewEx> {
  final List<int> heart = <int>[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

  @override
  Widget build(BuildContext context) {
    return GridView.builder(
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2, // 1행에 보여줄 아이템의 개수
          //childAspectRatio: 4 / 5, // 아이템의 가로 세로 비율
          mainAxisSpacing: 1, // 수평 Padding 값
          crossAxisSpacing: 1, // 수직 Padding 값
        ),
        itemCount: heart.length, //아이템의 개수
        itemBuilder: (BuildContext context, int index) {
          return GestureDetector(
            onTap: () {
              setState(() {
                heart[index] == 0 ? heart[index] = 1 : heart[index] = 0;
              });
            },
            child: Center(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Stack(children: [
                    Container(width: 192, height: 192, color: Colors.grey),
                    Positioned(
                        left: 10.0,
                        top: 10.0,
                        child: Icon(
                            heart[index] == 0
                                ? CupertinoIcons.heart
                                : CupertinoIcons.heart_fill,
                            color: Colors.white)),
                  ]),
                ],
              ),
            ),
          );
        });
  }
}
```