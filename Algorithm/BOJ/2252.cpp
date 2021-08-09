// [2252] 줄 세우기
// 그래프 이론
// 위상 정렬

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

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