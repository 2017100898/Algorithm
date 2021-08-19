// [1753] 최단경로
// 그래프 이론
// 다익스트라

#include <iostream>
#include <vector>
#include <utility>
#include <queue>
#define INF 1000009
using namespace std;

int D[20001];
vector<pair<int, int>> vec[20001];
priority_queue<pair<int, int>> que;
int V, E, K, u, v, w, to, weight;

//다익스트라
int func(int start) {
    que.push({0, start});

    while (!que.empty()) {
        int cost = -que.top().first;
        int A = que.top().second;
        que.pop();

        if(D[A]<cost)
            continue;

        for (int i = 0; i < vec[A].size(); i++) {
            to = vec[A][i].first; // v
            weight = vec[A][i].second; //w

            if (D[to] > D[A] + weight) {
                D[to] = D[A] + weight;
                que.push({-D[to], to});
            }
        }
    }

    return 0;
}


int main() {

    cin >> V >> E;
    cin >> K;

    for(int i = 1; i<=V; i++){
        D[i] = INF; //K 에서 부터의 거리 모두 INF로 설정
    }

    D[K] = 0; //K에서 K는 거리 0 설정

    for(int i = 0; i<E; i++) {
        cin >> u >> v >> w;
        vec[u].emplace_back(make_pair(v, w));
    }

    func(K);

    for(int i = 1; i<=V; i++){
        if(D[i] == INF){
            cout<<"INF"<<'\n';
        }
        else {
            cout << D[i] << '\n';
        }
    }

    return 0;
}