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

# Lower bound / Upper bound
* Lower bound: 원하는 target 값 이상이 처음 나오는 값
	* 예를 들어  41 45 45 46 이 있을 때 Lower bound(45)는 처음 나오는 45가 된다.
* Upper bound: 원하는 값 target 초과인 값이 처음으로 나오는 위치
	* 예를 들어, 41 45 45 46 이 있을 때 Upper bound(45)는 46이 된다.

```Python
def lower_bound(target):
	left, right = 0, n - 1
	min_idx = n

	while left <= right:
		mid = (left + right) // 2 # 이진탐색과 달리, 일반적인 arr[mid]==target 은 없다
		if arr[mid] >= target: # 원하는 target 이상이 처음 나오는 값을 찾기 위함 !
			min_idx = min(min_idx, mid) # 값이 같을 때, 최소 index 를 갱신하기 위함
			right = mid - 1

		else:
			left = mid + 1

	return min_idx
```

* Upper bound - Lower bound == 배열 내 수의 개수
* 따라서, Upper bound == Lower bound일 때 배열 내 값이 없다고 본다.