// [9663] N-Queen
// 브루트포스 알고리즘
// 백트래킹

#include <iostream>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <cmath>
using namespace std;

int N;
int cnt;
int arr[17];
bool used[17];

int func(int n){
    if(N < n){ //틀이 꽉 찼을 때
        cnt++;
    }
    
    // 틀에 아직 공간이 있을 때
    for(int i = 1; i<N+1; i++){
        if(used[i]==0){
            arr[n] = i;
            bool tf = true;
            for(int j = 1; j<n; j++){
                if(n != 1 && (arr[n-j]+j == arr[n] || arr[n-j]-j == arr[n])){
                    tf = false;
                }
            }
            
            if(tf == true){
                used[i] = 1;
                func(n+1);
                used[i] = 0;
            }
            
        }
    }

    return 0;
}

int main(){
    cin>>N;
    cnt = 0;
    func(1);
    cout<<cnt;
}

