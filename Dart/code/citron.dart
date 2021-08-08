// darttutorial-32-03.dart : Flutter HelloWorld using baseline widgets
// Reference: https://flutter.dev/docs/development/ui/widgets-intro#using-material-components
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
