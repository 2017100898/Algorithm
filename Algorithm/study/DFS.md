# 깊이우선탐색(DFS: Depth First Search)
* 루트 노드에서 시작하여 최대한 진입할 수 있는 깊이의 자식 노드까지 모두 탐색한 뒤, 자식 노드가 없으면 다시 위로 올라가 새로운 자식 노드를 탐색하는 방법이다.
* 부모 노드로 되돌아오는 과정을 백트래킹이라 부른다.
* 그래프는 인접 행렬 또는 인접 리스트로 나타낼 수 있다.
* DFS는 꼭 **재귀함수**를 이용하여 작성한다.

## 구현

```C++
void dfs(int V){
    visit[V] = 1;

    for(int next: adj[V]){
        if(!visit[next]){
            cout << next << ' ';
            dfs(next);
        }
    }
}
```

```Python
def dfs(vertex):
	for curr_v in graph[vertex]:
		if not visited[curr_v]:
			visited[curr_v] = True
			dfs(curr_v)
```

## 백트래킹
* 모든 경우의 수를 모두 고려하는 알고리즘이다. BFS보다 DFS로 구현하는 것이 편리하다.
* 그러나 Tree의 깊이가 무한대가 되는 경우 (미로찾기 등에서 사이클이 발생하는 경우)에서는 DFS보다 BFS를 사용하는 것이 편리하다.