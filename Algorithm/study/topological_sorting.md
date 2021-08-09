# 위상정렬

* 유향 그래프의 정점들을 변의 방향을 거스르지 않도록 나열하는 것을 뜻한다.
* 위상정렬을 가장 잘 설명할 수 있는 예로는 대학의 선수과목 구조가 있다.

### 방법론
1. 준비물
	1. 그래프 정보를 저장할 vector<vecter> adj 인접 행렬을 만든다.
	2. indegree 값을 저장할 vector indegree를 만든다.
	3. 정렬을 위한 Queue를 만든다.
2. adj를 채우고 indegree를 업데이트 한다.
3. adj를 순회하며 indegree[i] == 0 인 정점을 찾으면, 해당 정점의 indegree[i]를 삭제한다.
4. Queue에 i를 넣는다.
5. adj[i] 내의 모든 v에 대해 indegree[v]--를 실행한다.
6. Queue의 크기가 정점의 개수가 될 때까지 3-5 과정을 반복한다.
7. Queue의 값을 pop 하여 결과를 도출한다.

### 구현
#### BOJ [2252] 줄세우기

```C++

int main(){
    int N, M, u, v;
    cin>> N >> M;

    vector<vector<int>> adj(N+1, vector<int>());
    vector<int> idg(N+1, 0);
    queue<int> result;

    for(int i = 0; i < M; i++){
        cin >> u>> v;
        adj[u].push_back(v);
        idg[v]++;
    }

    while(result.size() != N){
        for(int i = 1; i < adj.size(); i++){
            if(idg[i] == 0){
                idg[i] = -1; // 삭제
                result.push(i);
                for(int v: adj[i]){
                    idg[v]--;
                }
            }
        }
    }

    while(!result.empty()){
        cout<<result.front() <<' ';
        result.pop();
    }

}
```