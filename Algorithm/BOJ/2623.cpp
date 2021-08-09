// [2623] 음악프로그램
// 그래프 이론
// 위상 정렬

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(){
    int N, M, s, u, v;
    int cnt = 0;
    cin>> N >> M;

    vector<vector<int>> adj(N+1, vector<int>());
    vector<int> idg(N+1, 0);
    queue<int> result;

    for(int i = 0; i < M; i++){
        cin >> s;

        int arr[s+1];

        for(int j=0; j<s; j++) {
            cin >> u;
            arr[j] = u;
        }

        for(int j=0; j<s-1; j++){
            u = arr[j];
            v = arr[j+1];
            adj[u].push_back(v);
            idg[v]++;
        }
    }

    while(result.size() != N){
        for(int i = 1; i < adj.size(); i++){
            cnt++;
            if(idg[i] == 0){
                idg[i] = -1; // 삭제
                result.push(i);
                for(int v: adj[i]){
                    idg[v]--;
                }
                cnt = 0;
            }
            if(cnt>N){
                cout<<0;
                return 0;
            }
        }
    }

    while(!result.empty()){
        cout<<result.front() <<'\n';
        result.pop();
    }

}