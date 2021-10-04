# Key
1. 위젯이 위젯 tree 내에서 이동할 때 State 보존하는 역할
	* 1번 위젯이 2번 위젯 아래 위치로 내려가더라도, 1번 위젯을 식별해낼 수 있어야한다.
3. 위젯이나 요소 유니크하게 식별하는 역할

## State
* State란, UI가 변경되도록 영향을 미치는 데이터이다.
* ex. check box, text 입력…

### Stateless widget
* 자리를 바꾸는 두 위젯을 구현하고 싶을 때, 컨테이너를 삭제 및 추가하는 방식으로 위젯 위치 Swap 가능

> Index : 0 ,   1  
> tile :  [tile1, tile2]  
> ↓  
> Index : 0  
> tile :  [tile2]  
> ↓  
> Index : 0 ,   1  
> tile :  [tile2, tile1]  

### Stateful widget
* 더 이상 Stateless의 방식이 통하지 않는다.
* 이는 위젯의 정보가 위젯 자체가 아닌 State 객체에 따로 저장되어있기 때문이고, value값 자체도 이 State에 들어가있다.
* Key 속성을 추가하여 Widget tree와 Element tree를  Stateless처럼 연결 해줄 수 있다.

### Value Key
1. Flutter는 기본적으로 위젯의 타입으로 식별
2. Stateful 위젯의 식별을 위해서는 Key 필요
3. Value key는 value 값을 가지는 Stateful 위젯에 사용

### Global Key
* 한 위젯 내부에 있는 변수나 메소드 외부에서 접근할 수 있도록 하는 Key