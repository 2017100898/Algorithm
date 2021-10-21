# 이분검색 알고리즘
* 정렬된 배열에서 특정한 값을 찾아내는 알고리즘
* W(n) = log n + 1

## 방법론 (recursion)
* 분할 : 배열을 반으로 나누어서 x가 중앙에 위치한 항목보다 작으면 왼쪽에 위치한 배열 반쪽을 선택하고, 그렇지 않으면 오른쪽의 배열 반쪽을 선택한다.
* 정복 : 선택된 반쪽 배열에서 x를 찾는다.

## Pseudo-code (recursion)
```cpp
index location(index low, index high){
	index mid;

	if(low > high)
		return 0;
	else{
		mid = (low+high)/2
		if(x==S[mid]) // n, S, x는 전역 변수로 지정
			return mid;
		else if (x<S[mid]) 
			return location(low, mid-1); //tail recursion
		else
			return location(mid+1, high);
	}
}

locationout = location(1, n);
```

## Pseudo-code (not recursion)
```cpp
void binsearch(int n, const keytype S[], keytype x, index& location){
	index low, high, mid;

	low = 1; high = n; 
	location = 0;
	
	while(low <= high && location == 0){
		mid = (low + high) / 2;
		if(x==S[mid])
			location = mid;
		else if(x<S[mid])
			high = mid - 1;
		else
			low = mid + 1;
	}
}

```

