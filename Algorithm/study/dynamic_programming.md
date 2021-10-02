# Dynamic Programming
* 다이나믹 프로그래밍은 분할정복법과 마찬가지로 문제를 나눈 후에 나누어진 부분들을 먼저 푸는 알고리즘이다. 이때 인덱스를 효과적으로 설정하여 **작은 문제들의 중복 해결을 방지**한다.
* 상향식 해결법으로 **먼저 작은 문제 해결하고 결과를 큰 문제의 해결**로 확산한다.

## 방법론
1. 재귀 관계식을 정립한다.
2. 작은 사례를 먼저 해결하는 상향식 방법으로 진행한다.

## 예시
* [플로이드-워셜](https://github.com/2017100898/TIL/blob/main/Algorithm/study/floyd_warshall_algorithm.md)
* [이항계수](#Binomial-Coefficient)

---

# Binomial Coefficient
### Divide-and-Conquer
```python
def bin(n, k):
    if(k==0 or n==k):
        return 1
    else:
        return bin(n-1, k-1)+bin(n-1, k)
```

* nCk 을 구하기 위해 이 알고리즘이 계산하는 항의 개수는 `2*(nCk)-1`
* divide- conquer 로 구하는 것은 불가능하다.

### Dynamic Programming
1. 재귀 관계식을 정립
	* B[i][j] = B[i-1][j-1] + B[i-1][j]  (0<j<i)
	* B[i][j] = 1 (j=0 or j=i)
2. nCk를 구하기 위해서는 **B[0][0]부터 시작해서 위에서 아래로 재귀 관계식을 적용하여 배열을 채워나간다.** 결국 값은 B[n][k]에 저장이 된다. (파스칼의 삼각형)

```python
import numpy as np

def bin2(n, k):
    i = 0
    B = np.zeros((n+1, k+1), int)
    while(i <= n):
        j = 0
        while(j <= min(i, k)):
            if(j==0 or j==i):
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
            j+=1
        i+=1
        
    return B[n][k]
```

