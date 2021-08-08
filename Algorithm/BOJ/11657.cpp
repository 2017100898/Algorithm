// [11657] 타임머신
// 벨만-포드
// 그래프 이론

#include <iostream>
using namespace std;

struct Tree{
    int u;
    int v;
    int weight;
};

bool dfs(Tree tree[], long long dist[], int start);
int N, M, A, B, C;
const long long INF = 10e9;

int main(){
    cin>>N>>M;
    Tree tree[M+1];

    for(int i = 0; i < M; i++){
        cin >> A >> B >> C;
        tree[i].u = A;
        tree[i].v = B;
        tree[i].weight = C;
    }

    long long dist[N+1];
    for(int i = 0; i <= N; i++){
        dist[i] = INF;
    }

    bool result = dfs(tree, dist, 1);

    if(result)
        cout<<"-1"<<'\n';

    else{
        for(int i=2; i<N+1; i++){

            if(dist[i] == INF){
                cout<<"-1"<<'\n';
            }
            else
                cout<<dist[i]<<'\n';
        }
    }
}

bool dfs(Tree tree[], long long dist[], int start){
    dist[start] = 0;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            int current = tree[j].u;
            int next = tree[j].v;
            int weight = tree[j].weight;

            if ((dist[current] != INF) && (dist[next] > dist[current] + weight)){
                dist[next]= dist[current] + weight;
                if(i==N-1){
                    return true;
                }
            }
        }
    }

    return false;
};