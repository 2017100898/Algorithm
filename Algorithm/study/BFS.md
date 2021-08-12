# 너비우선탐색(BFS: Breadth First Search)
* 루트 노드에서 시작하여 한 단계 아래 깊이의 자식을 모두 탐색하는 과정을 반복하며 그래프를 탐색하는 알고리즘이다.
* Queue를 사용한다.

## 준비물
1. 그래프 정보를 저장한 인접 행렬
2. 방문 여부를 표시할 행렬

## 구현
```C++
void bfs(int V){
    visit[V] = 1;

    for(int next: adj[V]){
        if(!visit[next]){
            cout << next << " ";
            que.push(next);
            visit[next] = 1;
        }
    }

    while(!que.empty()){
        int a = que.front();
        que.pop();
        bfs(a);
    }
}
```