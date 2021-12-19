# 재귀 (Recursion)
## Recursive Call
* **Direct recursion** : 함수 내에서 본인을 호출하는 재귀
* **Indirect recursion** : 자신을 호출한 함수를 다시 호출하는 재귀

## Case
* **Base case** : 재귀가 아닌 형태의 탈출 조건
* **General (or recursive) case** : Base가 아니면 Recursive하게 설계하며, 자기자신보다 더 작아질 수 있도록 만들어야 한다.

## Recursion의 특징
* 재귀는 반복문보다 연산 처리 및 속도 면에서 **덜 효율적**이지만 코드가 깔끔하다.
* 재귀는 끝내는 조건 (Base Case)을 만들어줘야 하고 갱신이 없으면 끝내지 못 할 수도 있다.
* 팩토리얼 구현 시 재귀가 적합 하고, *피보나치 수열은 적합하지 않다.*
	* 재귀는 이미 연산했던 값을 또다시 연산하기 때문에 계산하는 피보나치 수가 높아질 수록 연산 효율이 급격히 떨어진다.
	* 예를 들어 피보나치 10은 109번, 11은 177번의 연산을 한다.
* 재귀 함수 구현 시, call by value로 큰 배열을 계속 넘기면 메모리, 비용이 커지며 과부하가 발생할 수 있다.
* 파라미터를 넘길 때 **pass by value로 넘기면 치명적이며,** pointer는 recursive 구현하는데 부담이 적기 때문에 괜찮다.
* **Recursive solution은 언제 사용하는가?**
	* Shallow depth : call 하는 구조가 깊게 들어가지 않을 때만 재귀를 쓰는 것이 좋다.
	* Efficiency : 계산량이 많지 않았으면 좋겠을 때
	* Clarity : 명확하게 설계가 될 때
* Divide and Conquer : 점점 쪼개서 전체 문제를 푸는 방법 - `느려지는 단점이 있다.`

## 최적의 판단
* 세 가지 Question을 통해 재귀가 최적인지 아닌지 판단할 수 있다.
	* Base-Case Question : Base Case가 잘 만들어졌는가? non-recursive가 있는가?
	* Smaller-Caller Question : 원래 데이터보다 점점 작은 것을 다루게 되는가?
	* General-Case Question : 나머지 잘 종작하는가? 계산은 잘 하는가?


## Recursion 예시
### Factorial (팩토리얼)
* n! = n * (n-1)! 이 반복된다.
* 0! = 1 이라고 설정하면 탈출할 수 있다.

```cpp
int Factorial (int number)
{
	if(number == 0)
    		return 1;
    	else
        	 number * Factorial(number-1);
}
```

### 조합

```cpp
int Combinations(int n, int k)
{
    if(k == 1) //base1
    	 	return n;
    else if(n == k) //base2
    		return 1;
    else
    	return (Combinations(n-1,k)+ Combinations(n-1.k-1));
}
```

### x^n 값 구하기
* x^n = x * x^(n-1)
* base case : x^0 = 1

```cpp
int Power(int x, int n)
{
   if (n==0)
        return 1;
    else
    	return (x * Power(x, n-1));
}
```


## Run-time Stack (Call Stack)
<img width="300" src="https://user-images.githubusercontent.com/64299475/146687112-f9081f02-b73a-46bc-9954-722b11117a4f.png"> <img width="300" src="https://user-images.githubusercontent.com/64299475/146687110-bea6cd6c-5390-4946-97d4-616d4d380b3d.png">


* 현재 실행 중인 서브루틴에 대한 정보들을 담아두는 스택 구조의 메모리 영역이다.
* 이는 계산을 바로 못 하면 새로운 stack을 쌓아 계산 후 값을 반환하고 stack pop을 하는 형식이다.
* 과부하 시에는 stack overflow 되면서 죽는다.
* 각 Stack의 크기는 다르고, pointer를 내릴 때 얼마나 내려가야하는지도 함께 저장할 필요가 있다.

