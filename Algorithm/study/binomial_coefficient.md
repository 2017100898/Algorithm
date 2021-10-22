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
<img width="308" alt="스크린샷 2021-10-22 오후 5 35 37" src="https://user-images.githubusercontent.com/64299475/138421989-25bcf05b-29a9-4da4-a292-64068371f285.png">


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
