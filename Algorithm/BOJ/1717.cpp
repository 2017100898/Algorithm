// [1717] 집합의 표현
// 분리 집합

#include <iostream>
#include <vector>
using namespace std;
int N, M, cmd, a, b;
vector<int> parent;
void unions(int a, int b);
int find(int a);

int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>N>>M;

    for(int i=0; i<=N; i++){
        parent.push_back(i);
    }

    for(int i=0; i<M; i++){
        cin>>cmd >> a>> b;
        if(cmd == 0){
            unions(a, b);
        }

        else if(cmd==1){
            if(find(a) == find(b)){
                cout<< "YES"<<'\n';
            }
            else{
                cout<<"NO"<<'\n';
            }
        }
    }

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