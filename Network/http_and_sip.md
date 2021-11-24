# HTTP and SIP
* **HTTP**는 Transport Layer 영역에 속한다. HTML 웹서비스를 실어나르는 것을 시작으로 했고, 현재 웹브라우저와 웹서버 사이의 통신을 지배하고 있다.  HTTP는 매우 중요한 프로토콜이다.
* **SIP**는 카카오톡과 같은 인스턴트 메신저, 줌과 같은 화상 통화 어플리케이션의 핵심 기술에 해당하는 프로토콜이다.

## HTTP 1.x
### Web Client and Servers
<img width="400" src="https://user-images.githubusercontent.com/64299475/142028253-9b656713-ca2c-4668-addd-9c350a49e0b8.png">

* Web은 점과 줄로 연결 되어 있다. 점은 정보이고, 줄은 하나의 정보에서 추가적으로 알고싶은 것이 있을 때 다른 정보로 이동하기 위한 것이다.
* Web은 정보를 주고 받기 위해 HTTP를 사용한다. 웹 브라우저는 Web Client이다. 
* **Web Client** : 정보를 요청하는 자
* **Web Server** : 정보를 제공하는 자
* **HTTP request** : Client ⇒ Server 정보 요청할 때 보내는 메시지
	* 파일을 달라고 요청할 때는 `GET` 명령어를 사용한다.
* **HTTP response** :  Server ⇒ Client 정보 제공할 때 보내는 메시지
	* GET에 대한 응답 제공 (ex. OK), Content-type, Content-length 제공

### Resources
* Resource는 HTTP 에서 request, response에서 주고 받는 File이다.
* 웹 페이지 하나를 채우는 것은 수많은 리소스가 서로 다른 컴퓨터에서 오는 것이다.
* **Static Content** : HTTP request가 서버에 도착하는 시간이 T0일 때, T0전에 존재하는 콘텐츠를 뜻한다. `MS word File, Image File, Video Clip, etc…`
* **Dynamic Content** : HTTP request가 서버에 도착하는 시간이 T0일 때, T0이후에 만들어질 콘텐츠를 뜻한다.  `Live Image (사용자 접속 기준에 의해 동적으로 만들어지는 이미지), Trade Stocks, etc…`
* 넷플릭스에 들어가서 영화를 본다고 하자. 넷플릭스는 내가 들어가기 전에도 콘텐츠가 이미 존재하고 바뀌지 않기 때문에 Static Content이다. 
* **Media Types : MIME** (Multipurpose Internet Mail Extensions)
	* 실어나르는 Contents의 Type과 길이가 무엇인지 명시하는 프로토콜
	* MIME Type :  `image/jpeg`
* **URI (Uniform Resource Identifier)**
	* 인터넷에서 리소스를 찾아기 위한 Address
	* 전세계에서 유일하게 식별할 수 있어야 한다.
	* 위치에 대한 정보도 들어가야 한다.
	* URL (locator) and URN (Name)

### HTTP Method
* **GET** : Client 가 Server에게 받기 원하는 리소스를 요청, 파일 다운로드
* **PUT** : Client가 전달한 리소스를 Server가 저장, 파일 업로드
* **DELETE** : Server로부터 해당 리소스를 삭제
* **POST** : Client가 Server에게 File이 아닌 '(글자)값’을 보내고 싶을 때 사용
* **HEAD** : GET과 비슷하지만, Response 시 File 본체를 제외하고 전송 (Type과 Length로 파일 변했는지 파악할 때  등 사용)
* **TRACE** : Proxy가 있는지 확인 (디버그 목적 등으로도 사용 가능)
* **OPTIONS** : Server가 지원하는 Method 모두 알려달라고 요청 (보통은 OPTIONS 안 됨)

#### 기타
* **200** : OK. 요청한 작업 성공적으로 수행
* **302** : 정보가 있는 다른 곳으로 이동
* **404** : 파일 지워졌을 때

### Connection
* HTTP는 기본적으로 밑에 TCP를 쓰도록 권장되고 있다.
* HTTP는 자체적으로 신뢰성을 보장할 수 없으나 **TCP는 Reliable 하다.** 
* UDP를 쓰면 유실될 수 있다.
* **Connections Process**
	1. Web Browser에 URL을 치면, DNS를 통해 URL에 대한 IP 주소를 가져온다.
	2. Client는 Server에게 TCP 연결을 하고, HTTP GET이 나간다.
	3. Response 를 가져오면 TCP를 끊고 연결을 해제한다.

### Architectural Components of the Web
* **Proxy**
	* HTTP Client와 Server 사이에 존재하는 장치이다.
	* Proxy는 Client와 Server사이에서 주고 받는 트래픽을 쳐다보고, 막아야할지 말아야할지 결정을 한다. 예를 들어 대한민국에서는 들어가지 못 하는 사이트, 바이러스가 있는 사이트, 회사 내에서 업무와 관련 없는 사이트 등을 차단한다.
	* Client나 Server를 보호하기 위해 사용할 수 있다.
	* Proxy는 압축 등 다양한 기능이 있다.
	
## Web Browser as Development Tool
* Firefox, Chrome, Safari 등 Web Browser에서 개발자 도구 (웹 개발 도구)를 이용함으로써 메모리, 디버거, 저장소 등을 직접 경험할 수 있다.

## Web Server Development
* (설치형) 소프트웨어 사용 `-  대부분이 Static 한 Conents를 제공할 때 유용`
	* Apache
	* Nginx
	* Wordpress
* Programming language 사용 `- 최근 언어들은 HTTP 라이브러리를 갖고 있다. 해야 할 logic이 있을 때 유용`
	* Javascript
	* Node.js
	* C++ & Proxygen

### example

```javascript
var http = require('http');

http.createServer(function (req, res){
	res.writeHead(200, {'Content-Type': 'text/plain'}); //Header
	res.end('Hello World!'); //Contents
}).listen(8080);
```

## Web based Mobile Application Development
* HTTP가 실어나르던 트래픽이 진화를 거듭했고, 정적인 것만 표현할 수 있던 HTML을 Javascript가 보완하게 되었다.
* 웹 브라우저 위에서만 돌아가던 Javascript는 이후 개선을 시도했고, Application을 만드는 언어로 자리 잡는다.   `PhoneGap(브랜드) - CORDOVA(오픈소스)`
* Javascript, HTML, CSS 은 웹브라우저를 벗어나서 platform에 Independent하게 개발할 수 있는 도구로서 자리를 잡게 된다.

## HTTP 2.0
* SPEEDY

### HTTP 문제점에 대한 해결책
<img width="400" src="https://user-images.githubusercontent.com/64299475/142595982-f068fe47-101d-40c4-b4b5-f034d7641127.png">

* **바이너리 프로토콜** : 텍스트 단위는 프로세싱 시간이 오래 걸리므로, 0과 1의 조합으로 변환한다.
* **Multiplexing** : 순서대로 request를 받고 response를 보내지 않고, 준비가 되면 바로바로 보내도록 한다. 우선순위가 높으면 더 빨리 보내도록 한다.
* **헤더 압축** : 반복적으로 사용 되는 헤더는 인덱스로 표기한다.
* **우선순위 설정**
* **Server Push** : request를 하지 않아도, 클라이언트가 요구할 만한 것들은 보낸다. (ex. refresh, alarm, ad …)

## HTTP 3.0
### QUIC Protocol
<img width="400" src="https://user-images.githubusercontent.com/64299475/142599128-98f1cb0d-bdea-4385-ab25-2afb98f2d01d.png">

<img width="400" src="https://user-images.githubusercontent.com/64299475/142599248-79f06421-0fd4-4b98-a67e-684d1642d231.png">

<img width="400" src="https://user-images.githubusercontent.com/64299475/142600116-f215f8a0-c714-4d20-9114-bd9370aa4b74.png">

<img width="400" src="https://user-images.githubusercontent.com/64299475/142600226-f5bd0660-2365-4436-916b-fd465036fe03.png">

* **QUIC Protocol**은 UDP 를 사용하므로, 기존 에러 검출 및 복구를 사용하지 않는다. TCP를 쓰지는 않지만, TCP에서 제공했던 에러 검출 및 복구 기법들을 UDP 위에서 직접 구현하게 된다.
* **TCP는 중간에 문제가 발생하면, 재전송에 의해 뒤가 멈추고, 속도 조절이 안 되는 문제가 있으나, QUIC은 UDP이기 때문에 속도가 빠르고, 여러 줄로 가기 때문에 에러 검출 및 복구가 각각에 대해 이뤄지기 때문에 전체가 느려지는 현상을 방지할 수 있다.**
* TCP 위에서 HTTP 돌리니 문제 다수 발생해서 UDP 위에 올렸고, HTTP 2.0을 베이스로 개선을 시도 했다.
	1. 연결 시 시간 오래 걸리는 문제
	2. 전송 시의 Flow Control
	3. Congestion Control
	4. 네트워크 속도 지원 못하는 문제
* TCP, UDP 성능 개선을 하기 위해서는 OS 커널을 건드려야 하는데, 이는 매우 부담스러운 일이다. 따라서 TCP가 아닌 UDP를 씀으로써 Transport layer가 아닌 그 위에서 무언가를 동작하도록 한다.
* QUIC 은 초기 연결 시간을 빠르게 하기 때문에 사용자는 체감 시간이 극명하게 낮아진다. QUIC은 급속도로 퍼지고 있고, 특히 UDP를 사용했을 때 효과를 극대화할 수 있는 비디오 트래픽에서 두각을 나타내고 있다.

### Application Space Execution
* QUIC은 Application Layer에서 에러 검출 및 복구를 한다.  Kernel 이 아닌 그 위에 개발이 되었기 때문에 성능 문제가 발생할 수 있다.
* Kernel 안에 있는 것들의 통신은 overhead가 적지만, QUIC은 시간이 조금 더 걸릴 수 있다. 그러나 부하가 큰 영향을 미칠 정도는 아니다.

### Client & Server Deployment
* Client  : chrome에서  `chrome://net-internals/#quic` 을 통해 QUIC을 켤 수 있다.
* Server : quic-go 등 QUIC으로 서버를 만드는 케이스들이 생겼다.

## SIP (Session Initiation Protocol)
* SIP는 카카오톡, 줌과 같은 소프트웨어의 실시간 통신, 파일 전송들을 지원하는 프로토콜이다.
* RTP (real-time protocol)

### SIP & SDP
<img width="400" src="https://user-images.githubusercontent.com/64299475/142602258-dbfffabd-7b99-4d7e-aaf8-ef16a5d96974.png">

*  INVITE, 200 OK, 즉, 위 사진에서 초록색 글자에 대한 내용은 **SIP**에서 정의하고, 실질적인 Media 에 대한 정보는 **SDP**에서 별도로 정의한다. SIP가 SDP를 실어나르는 형식이다.
* HTTP는 하나에 정의 되어 있고, SIP는 두 개로 나뉘어져 있다는 것 외에는 큰 차이는 없다.

### User Agent
* User Agent Client : 요구 보내는 쪽
* User Agent Server : 요구 받는 쪽

### Registrar
<img width="400" src="https://user-images.githubusercontent.com/64299475/142604125-7937bd01-da68-4dfd-a109-4fa079d24aef.png">

* 통신을 하기 위해서는 사용자가 현재 사용하고 있는 network 주소를 알아야 한다. 그러나 application의 ID는 고정 되어있지만 network 주소는 계속 바뀌는 문제가 있다. 
* 이런 상황에서, 휴대폰의 네트워크 주소를 주기적으로 확인하여 **SIP의 ID를 Ip address로 맵핑하는 것을 Registrar라고 한다.** 그렇기 때문에 소프트웨어에 서버가 필요하다.
* 이외에도 통신을 위해서는 Proxy Server, Redirect Server가 필요하다.

## Advanced Web Technologies
### WebRTC (Web Real-Time Communication)
* `Web Based Application` : 굳이 운영체제 내려가지 않고 Web을 기반으로 Application을 설계할 수 있다.
* 데이터 채널을 통해서 데이터를 주고 받을 수 있고, MediaStream Track이라는 API 사용해서 오디오, 비디오도 모두 지원 가능한 표준이다.
* Chrome, Firefox, android, IOS에서 이미 지원을 하고 있고, 이를 통해 웹 브라우저 내에서 웹 화상 시스템을 간단하게 만들 수 있다.

### asm.js
* web +  assembly : C++/RUST 등을 웹 브라우저 위에서 돌리는 기술 (제 4의 개발방법)

### WebVR / WebXR
* virtual reality contents를 실어나르는 것이 웹 브라우저의 기능 일부로 들어가는 것
* Mixedreality

### Solid
* Blockchain과 비슷한 방법으로, 나의 저장소를 내가 관리하는 방법이다.



