# 피보나치 수열
> F0 = 0  
> F1 = 1  
> Fn = Fn-1 = Fn-2  

## 재귀적 방법
```cpp
int fib(int n){
	if(n<=1)
		return n;
	else
		return fib(n-1) + fib(n-2);
}
```

<img width="358" alt="스크린샷 2021-10-21 오전 12 18 06" src="https://user-images.githubusercontent.com/64299475/138121818-a9ccb022-0e27-41a1-a414-2beafc9b6edd.png">

* 같은 피보나치 수를 중복적으로 계산하므로 수행 속도가 매우 느리다.
* T(n) = 2^(n/2)

## 반복적 방법
```cpp
int fib2 (int n){
	index i;
	int f[0..n];
	f[0] = 0;
	if(n>0){
		f[1] = 1;
		for(i=2; i<=n; i++)
			f[i] = f[i-1] + f[i-2];
	return f[n];
}
```

<img width="428" alt="스크린샷 2021-10-21 오전 12 21 41" src="https://user-images.githubusercontent.com/64299475/138122466-f5be3b80-ba32-4578-b4e5-de3de4cdc04e.png">

* 중복 계산이 없기 때문에 반복 알고리즘은 수행 속도가 훨씬 빠르다.
* T(n) = n + 1