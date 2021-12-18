# 재귀 (Recursion)
## Recursive Call
* Direct recursion : 함수 내에서 본인을 호출하는 재귀
* Indirect recursion : 자신을 호출한 함수를 다시 호출하는 재귀

## Case
* Base case : 재귀가 아닌 형태의 탈출 조건
* general (recursive) case : Base가 아니면 Recursive하게 설계하며, 자기자신보다 더 작아질 수 있도록 만들어야 한다.

## Recursion의 특징
* 재귀는 반복문보다 연산 처리 및 속도 면에서 덜 효율적이지만 코드가 깔끔하다.
* 재귀는 끝내는 조건을 만들어줘야 하고 갱신이 없으면 끝내지 못 할 수도 있다.
* call by value로 큰 배열을 계속 넘기면 메모리, 비용이 커지며 과부하가 발생할 수 있다.
* 팩토리얼 구현 시 재귀가 적합 하고, 피보나치 수열은 적합하지 않다.
* 파라미터를 넘길 때 pass by value로 넘기면 치명적이며, pointer는 recursive 구현하는데 부담이 적기 때문에 괜찮다.
* Recursive solution은 언제 사용하는가?
	* Shallow depth : call 하는 구조가 깊게 들어가지 않을 때만 재귀를 쓰는 것이 좋다.
	* efficiency : 계산량이 많지 않았으면 좋겠을 때
	* clarity : 명확하게 설계가 될 때

## 최적의 판단
* Base-Case Question : Base Case가 잘 만들어졌는가? non-recursive가 있는가?
* Smaller-Caller Question : 원래 데이터보다 점점 작은 것을 다루게 되는가?
* General-Case Question : 나머지 잘 종작하는가? 계산은 잘 하는가?
* 세 가지 Question을 통해 재귀가 최적인지 아닌지 판단할 수 있다.

## Run-time Stack (Call Stack)
* 현재 실행 중인 서브루틴에 대한 정보들을 담아두는 스택 구조의 메모리 영역이다.

