# Transport Layer - 2

## Socket Programming

### Network Socket

* 세계에서 유니크하게 식별할 수 있는 `IP address`와 컴퓨터 내 특정 소프트웨어를 지칭하는 `Port 번호` 를 합쳐서 **Socket**이라 한다.
* 컴퓨터 내에서는 Socket을 **Table 형태**로 관리한다.
* Port만 다르면, 한 개의 컴퓨터 내에서도 두 개의 컴퓨터가 통신하는 것이 가능하며, Host-to-Host, Process-to-Process만 가능하다면 LAN 뿐만 아니라, 지역적인 위치에 상관없이 통신이 가능하다.


### Client and Server Architecture
<img width="400" src="https://user-images.githubusercontent.com/64299475/140792124-e858ff07-e637-459f-b8f8-c892e9b56d33.png">


* **Socket Server** : Socket을 사용해서 통신 받아주는 모든 프로그램
* **Socket Client** : Socket을 사용해서 다른 프로그램에 요구하는 모든 프로그램 `web server, email client, mobile game, etc...`
* **TCP와 UDP는 철저하게 1:1이다.** 예를 들어, 카카오톡 서버가 있고, 수많은 클라이언트가 존재한다면, 클라이언트들은 logical하게 채팅방을 만든다. 서버에는 채팅방에 대한 정보가 있고, 그 속에 참여하고 있는 수많은 유저들이 있다. 
* 따라서, TCP/UDP를 쓴다면, 클라이언트 1번이 채팅방에 글을 썼을 때 통신 방식은 다음과 같다. 클라이언트 1번과 서버가 1대1로 연결되고, 다른 클라이언트와 서버도 다시 각각 1대1로 연결되는 형식이며, 서버는 1번으로부터 받은 정보를 각 클라이언트들에게 독립적으로 전달한다.

### Echo Server in Python
   
```python
  import socket
  
  HOST = '127.0.0.1'
  PORT = 65432
  
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))
      s.listen()
      conn, addr = s.accept()
      with conn:
          print('Connected by', addr)
          while True:
              data = conn.recv(1024)
              if not data:
                  break
              conn.sendall(data)
```

### Echo Client in Python

```python
  import socket
  
  HOST = '127.0.0.1'
  PORT = 65432
  
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, PORT))
      s.sendall(b'Hello, world')
      data = s.recv(1024)
      
  print('Received', repr(data))
```

  

## ZeroMQ
<img width="500" src="https://user-images.githubusercontent.com/64299475/140793771-0c3cb508-97ca-40ee-9472-e5075a969ef4.png">

* ZeroMQ는 안정적인 서비스를 빠르게 구현할 수 있도록 개발 된 Messaging library이다.
* TCP 외에도 `IPC, TIPC,...`를 지원한다.
* ZeroMQ API는 전통적인 Socket Programming 방식을 유지 하지만, **Many to Many**가 가능하다.
* 클라우드 컴퓨팅 위에서 동작한다.

### Patterns
* 각 패턴은 특정 네트워크 토폴로지를 정의하며, 모든 패턴은 인터넷 규모에 맞게 사용할 수 있다.
* **Request-reply** (service bus) : 여러 개의 통신 소프트웨어들이 서로 Request하고 Response 받는 것
* **Publish-subscribe** (data distribution tree) : 가입자가 가입함으로써 본인의 정보를 뿌리면 Subscriber가 받아서 처리하는 것
* **Push-pull** (parallelised pipeline, fan-in-fan-out) : 정보를 만들어내고 수집하는 자들끼리 병렬 처리가 큰 규모로 이루어진다는 것
* **Exclusive-pair** : 1대 1 형태

### Client & Worker
<img width="500" src="https://user-images.githubusercontent.com/64299475/140793539-12fd41cb-c896-4fff-8e85-c131f3b43e94.png">

* Client의 요청을 받아서 Broker가 처리하는 형식이다. `n:n 지원`이 가능하다.

### Publish & Subscriber
<img width="500" src="https://user-images.githubusercontent.com/64299475/140793516-765f4847-e22c-4843-bfb7-181de692dbba.png">


* Publisher가 Subscriber들에게 한 번에 정보를 뿌리는 `1:n` 형식이다.
* Publisher가 여러 개일 수도 있다.

<img width="500" alt="스크린샷 2021-11-09 오전 2 58 06" src="https://user-images.githubusercontent.com/64299475/140793636-697b1353-106a-44cf-aca2-e77936df6459.png">


## RabbitMQ

<img width="500" src="https://user-images.githubusercontent.com/64299475/140793945-f83ec64a-3ded-4cbd-8bb3-8e9211920385.png">


* ZeroMQ은 독립적이고 대등 관계이지만 RabbitMQ는 **중앙 집중**이 필요하다. `AMQP, STOMP, MQTT,...`
* 통신 회사에서 `1:m` 으로 보낼 때 자주 사용한다. 보내는 곳은 하나지만 받을 곳은 매우 많다.
* 클라우드 컴퓨팅 위에서 동작한다.





