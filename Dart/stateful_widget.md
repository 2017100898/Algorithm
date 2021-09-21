# Stateful widget
## State
* State 는 데이터이다.
* UI가 변경되도록 영향을 미치는 데이터이다.
* App 수준과 Widget 수준의 데이터가 있다.
	
## Stateless widget
* State가 변하지 않는 위젯
* 한 번 build 되면 state가 변하지 않으며, rebuild 만을 통해서 새로운 state 적용 가능.

### Tree
* **Widget Tree** : 우리가 컨트롤 할 수 있음 - MyApp, Scaffold, AppBar, Text… 설계도
* **Element Tree** : 플러터가 내부적으로 컨트롤, Widget tree와 Render tree 연결 - MyApp Element, Scaffold Element, AppBar Element, Text Element… (Widget Tree 를 Point - 위젯의 정보 함께 가지고 있음.)
* **Render Tree** : 플러터가 내부적으로 컨트롤, 직접적으로 스크린에 그림 그려줌 - Render object  (element tree와 1:1 대응)

### Hot reload
* **reload** : 프레임은 그대로 둔 채, 부수적인 요소들만 바꾸는 것. element tree 활용해서 변경된 부분만 다시 그림.
* **rebuild** : 위젯 트리내에 모든 위젯 새롭게 만들어짐. 
* 과정 : Container Widget 변경 -> Hot Reload -> Build Method 호출 -> Widget tree rebuild -> Element tree link update -> Render tree에 element tree info 넘겨줌 -> Render object re-rendering

## Stateful widget
* Stateful, Stateless 모두 생성자를 통해 외부에서 데이터가 입력되면 그 결과를 반영하기 위해 Build Method가 호출이 되고, 필요한 부분의 UI 다시 렌더링하게 된다.
* Stateful은 내부에 **State라는 Class** 갖고 있다. 두 클래스의 결합으로 이루어져 있다.
* Stateful widget이 rebuild 되는 경우?
	1. Child 위젯의 생성자를 통해서 데이터가 전달될 때
	2. Internal state가 바뀔 때
* setState method 필요 

## 구현
```dart
class MyCherry extends StatefulWidget {
  @override
  State<MyCherry> createState() => _MyCherryState();
}

class _MyCherryState extends State<MyCherry> {
  int counter = 0;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: GestureDetector(
            onTap: () {
              setState(() {
                counter++;
                print('$counter');
              });
            },
            child:
                Column(mainAxisAlignment: MainAxisAlignment.center, children: [
              Container(
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
              SizedBox(
                height: 10,
              ),
              Text(
                'Click : $counter',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                textAlign: TextAlign.center,
              ),
            ])),
      ),
    );
  }
}
```


* 따로 reload를 하지 않아도 체리 클릭 시 숫자가 올라가는 모습을 확인할 수 있다.

<img  src="https://user-images.githubusercontent.com/64299475/134207594-caba5152-c7a7-4330-94e3-d635674be58c.png" width="30%" height="30%"> <img  src="https://user-images.githubusercontent.com/64299475/134207745-92b2e1a4-ed7d-4a77-8be5-80523b987a5e.png" width="30%" height="30%"> <img  src="https://user-images.githubusercontent.com/64299475/134207778-011856dd-0f17-4483-9b1c-ed1e48800dfb.png" width="30%" height="30%">

<br> 

[YouTube 코딩셰프](https://www.youtube.com/watch?v=StvbitxUKSo&list=PLQt_pzi-LLfoOpp3b-pnnLXgYpiFEftLB&index=1)를 참고하여 공부하고 정리했습니다.
