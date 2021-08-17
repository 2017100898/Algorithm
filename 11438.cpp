// [11438] LCA2
// 최소 공통 조상
// 트리
// 희소 배열

#include <iostream>
#include <vector>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <cmath>
#define MAX 17
using namespace std;

vector<int> v[100001];
int depth[100001];
int arr[MAX][100001];
int LCA(int a, int b);
void dfs(int curr);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int M, T, num1, num2;
    cin >> M;

    fill(depth, depth+M+1, 0); //depth vec 0으로 초기화
    memset(arr, -1, sizeof(arr)); //arr 모든 값 -1으로 초기화

    depth[1] = 1; //root의 depth 설정

    for(int i = 1; i < M; i++){
        cin >> num1 >> num2;
        v[num1].push_back(num2);
        v[num2].push_back(num1);
    }

    // depth, arr[0][] 세팅
    dfs(1);

    // 나머지 arr 세팅
    for(int i = 1; i < MAX; i++){
        for(int j = 1; j <= M; j++){
            if(arr[i-1][j] == -1){
                arr[i][j] = -1;
            }
            else{
                arr[i][j] = arr[i-1][arr[i-1][j]];
            }
        }
    }

    cin >> T;

    for(int k = 0; k < T; k++){
        cin >> num1 >> num2;
        if(num1 ==1 || num2 ==1) cout << '1' <<'\n';
        else cout << LCA(num1, num2) << '\n';
    }

    return 0;
}

void dfs(int curr){
    for(auto next : v[curr]){
        if(depth[next] == 0){
            arr[0][next] = curr;
            depth[next] = depth[curr] + 1;
            dfs(next);
        }
    }
}

int LCA(int a, int b){

    if(depth[a] < depth[b]){
        swap(a, b);
    } //depth[a]가 더 크도록 맞춰줌

    int diff = depth[a] - depth[b];
    int powNum, K = 0;

    if(diff != 0){
        for(int i = MAX-1; i >= 0; i--){
            if(arr[i][a] == -1) continue;

            powNum = int(pow(2, i));
            if(diff >= powNum){
                diff -= powNum;
                a = arr[i][a];
            }
        }
    }

    if(a==b) return a;

    else{
        for(int i = MAX-1 ; i >= 0 ; i--){
            if(arr[i][a] == -1) continue;
            if(arr[i][a] != arr[i][b]){
                a = arr[i][a];
                b = arr[i][b];
            }
        }

        a = arr[0][a];
    }

    return a;

}