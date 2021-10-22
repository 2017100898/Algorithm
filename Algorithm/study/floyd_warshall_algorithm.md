# 플로이드-워셜 알고리즘
* 임의의 노드 s에서 e로 가는 데 걸리는 최단거리를 구하는 알고리즘이다.
* s와 e 사이의 노드 m에 대해, s에서 m까지의 최단거리와 m에서 e까지의 최단거리를 이용한다.

## 방법론
1. d의 모든 값을 INF로 초기화 하고 인접행렬을 입력 받아 값을 채운다.
2. 가운데 노드(m) - 시작 노드(s) - 마지막 노드(e) 순으로 for문을 돌린다.
	1. d[s][e] > d[s][m]+d[m][e] 일 때, d[s][e]를 d[s][m]+d[m][e]으로 업데이트한다.


## 구현1
```cpp
void Floyd(int n){
    for(int m = 1; m<=n; m++){
        for(int s=1; s<=n; s++){
            for(int e=1; e<=n; e++){
                if(arr[s][e] > arr[s][m] + arr[m][e]){
                    arr[s][e] = arr[s][m] + arr[m][e];
                }
            }
        }
    }
}
```
* T(n) = n³


## 구현2
> P[s][e]
> 1. s에서 e까지 가는 최단경로의 중간에 놓여있는 정점이 최소한 하나는 있는 경우 : 그 놓여있는 정점 중에서 가장 큰 인덱스
> 2. 없는 경우 : 0

```cpp
void Floyd2(int n, index P[][]){
	for(s = 1; s <= n ; s++){
		for(e = 1; e<=n; e++){
			P[i][j] = 0;	
		}
	}
    for(int m = 1; m<=n; m++){
        for(int s=1; s<=n; s++){
            for(int e=1; e<=n; e++){
                if(arr[s][e] > arr[s][m] + arr[m][e]){
		    P[s][e] = m;
                    arr[s][e] = arr[s][m] + arr[m][e];
                }
            }
        }
    }
}

void path(int q, r){ //최단 경로의 출력 
	if(P[q][r] != 0){
		path(q, P[q][r]);
		cout << "v" << P[q][r];
		path(P[q][r], r);
	}
}
```

<img width="364" alt="스크린샷 2021-10-22 오후 5 53 31" src="https://user-images.githubusercontent.com/64299475/138424782-94801069-a4a9-4299-b6af-793ad108a5bd.png"><img width="204" alt="스크린샷 2021-10-22 오후 5 53 47" src="https://user-images.githubusercontent.com/64299475/138424776-fa9355f3-654b-451b-870c-a4d6f6b73e4b.png">
