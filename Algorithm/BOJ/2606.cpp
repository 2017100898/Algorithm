// [2606] 바이러스
// 그래프 이론
// 그래프 탐색
// 깊이 우선 탐색

#include <iostream>
#include <vector>
using namespace std;

vector<int> adj[101];
bool visit[101];
int cnt = 0;

void dfs(int V){
    visit[V] = 1;

    for(int next: adj[V]){
        if(!visit[next]){
            cnt++;
            dfs(next);
        }
    }
}

int main(){
    int N, M, u, v;
    int V = 1;
    cin >> N >> M;

    for(int i = 0; i < M; i++){
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(V);
    cout << cnt;
}