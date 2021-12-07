# Listview
## ListView.builder
* itemCount와 itemBuilder를 이용해서 구현한다.
* 반복 되는 위젯을 for문보다 훨씬 간단하게 설계할 수 있다.
* setState를 통해 클릭 시 색깔이 사라지는 위젯을 구현했다.


```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Listview',
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
  final List<String> alphabet = <String>['A', 'B', 'C', 'D', 'E', 'F'];
  final List<int> color = <int>[100, 200, 300, 400, 500, 600, 700];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Listview", textAlign: TextAlign.center),
          backgroundColor: Colors.white,
          elevation: 10.0,
          centerTitle: true,
          foregroundColor: Colors.black,
        ),
        body: ListView.builder(
            itemCount: alphabet.length,
            itemBuilder: (BuildContext context, int index) {
              return GestureDetector(
                onTap: () {
                  setState(() {
                    color[index] = 0;
                  });
                },
                child: Container(
                  height: 150,
                  color: Colors.purple[color[index]],
                  child: Center(child: Text('Block ${alphabet[index]}')),
                ),
              );
            }));
  }
}
```

<img width="300" src="https://user-images.githubusercontent.com/64299475/144984124-6b13b408-202c-4c55-a789-9d9d7659c2a8.png"> <img width="300" src="https://user-images.githubusercontent.com/64299475/144984098-e63bc778-8114-4feb-a2ba-45b994f76ac6.png">


## ListView.seperated
* seperatorBuilder 속성을 추가해서 구현한다.
* 반복되는 위젯 사이에 구분선이 추가되는 위젯이다.

```dart
class _MyHomePageState extends State<MyHomePage> {
  final List<String> alphabet = <String>['A', 'B', 'C', 'D', 'E', 'F'];
  final List<int> color = <int>[100, 200, 300, 400, 500, 600, 700];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Listview", textAlign: TextAlign.center),
          backgroundColor: Colors.white,
          elevation: 10.0,
          centerTitle: true,
          foregroundColor: Colors.black,
        ),
        body: ListView.separated(
            itemCount: alphabet.length,
            separatorBuilder: (BuildContext context, int index) =>
                const Divider(thickness: 3),
            itemBuilder: (BuildContext context, int index) {
              return GestureDetector(
                onTap: () {
                  setState(() {
                    color[index] = 0;
                  });
                },
                child: Container(
                  height: 150,
                  color: Colors.purple[color[index]],
                  child: Center(child: Text('Block ${alphabet[index]}')),
                ),
              );
            }));
  }
}
```


<img width="300" src="https://user-images.githubusercontent.com/64299475/144984073-0663ee4f-dd59-4318-8ff9-825a515d0e0f.png"> <img width="300" src="https://user-images.githubusercontent.com/64299475/144984038-99794c97-5144-4931-89ea-06c502f2b35f.png">
