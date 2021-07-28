// [1197] 최소 스패닝 트리
// 최소 스패닝 트리

#include<iostream>
#include<stack>
#include<queue>
using namespace std;

// cycle 확인을 위한 array
int cycle[10001];

// tree 구조체
struct Info{
    long long weight;
    long long u;
    long long v;
};

// weight 값으로 pq 정렬
struct compare{
    bool operator()(Info &A, Info &B){
        return A.weight > B.weight;
    }
};

// 가장 높게 있는 조상값
int getParent(int u){
    if(cycle[u]==u)
        return u;
    return getParent(cycle[u]);
}

// union : cycle 업데이트
void unionParent(int u, int v){
    u = getParent(u);
    v = getParent(v);
    if(u<v) cycle[v] = u;
    else cycle[u] = v;
}

// cycle 확인
bool cycled(int u, int v){
    u = getParent(u);
    v = getParent(v);
    if(u==v) return true;
    else return false;
}

int main() {
    int V, E;
    long long A, B, C;
    long long result = 0;
    priority_queue<Info, vector<Info>, compare> que;
    cin>>V>>E;

    Info info[E];

    // u, v, weight 입력 받은 후 pq.push
    for(int i = 0; i < E; i++){
        cin>>A>>B>>C;
        info[i].u = A;
        info[i].v = B;
        info[i].weight = C;
        que.push(info[i]);
    }

    // i번 index를 i와 매칭
    for(int i=0;i<=V;i++){
        cycle[i] = i;
    }

    while(!que.empty()){
        // 사이클이 아닐 경우 Que.top weight 합쳐주고 pop
        if(!cycled(min(que.top().u, que.top().v), max(que.top().u, que.top().v))){
            result += que.top().weight;
            unionParent(que.top().u, que.top().v);
            que.pop();
        }
            // 사이클일 경우 패스
        else
            que.pop();
    }

    cout << result;
    return 0;
}