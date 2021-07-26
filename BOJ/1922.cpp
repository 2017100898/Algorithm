// [1922] 네트워크 연결
// 최소 스패닝 트리
// 그래프 이론

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void unions(int a, int b);
int find(int a);
int parent[1001];

int main(){
    cin.tie(0);
    int N, M, a, b, c;
    priority_queue<vector<int>> que;
    cin>>N;
    cin>>M;

    for(int i=0; i<M; i++){
        cin>>a>>b>>c;
        que.push({-c, a, b});
    }

    for(int i=0; i<1001; i++){
        parent[i] = i;
    }

    int cnt = 0;
    int result = 0;

    while(que.empty() == 0 && cnt<N-1){
        if(que.top()[0] == 0){
            que.pop();
        }

        if(find(que.top()[1]) == find(que.top()[2])){
            que.pop();
        }

        else {
            unions(que.top()[1], que.top()[2]);
            result += (que.top()[0]);
            cnt++;
            que.pop();
        }
    }

    cout<< -1 * result;
    return 0;
}

void unions(int a, int b){
    int aRoot = find(a);
    int bRoot = find(b);
    parent[aRoot] = bRoot;
}

int find(int a){
    if(parent[a] == a) return a;
    else return parent[a] = find(parent[a]);
}