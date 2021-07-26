
### GCD (최대공약수)

1. GCD(int a, int b)    
:  a (큰 수) % b (작은 수) = c
2. b % c ... 재귀로 반복
3. if a%b == 0 일 때    
: b가 GCD

> 🌈 GCD(a, b, c, d) == GCD(a, GCD(b, GCD(c, d)))

<br>

BOJ 9613에서 구현한 GCD는 다음과 같다.	  
함수에 들어오기 전에 a와 b 사이의 min, max를 파악해 미리 a를 max 값으로 설정해주는 작업이 필요하다.


```C++

long long GCD(int a, int b){
    if(a%b== 0){
        return b;
    }

    else{
        int c = a%b;
        return GCD(b, c);
    }
}

```

평소 재귀 공부가 필요하다는 생각을 했는데, GCD로 재귀의 흐름까지 파악해볼 수 있어서 좋았다.	   
문제가 GCD 합을 구하는 것이라, result 값이 매우 커질 것으로 예상해 long long type으로 설정했다.
