// [2960] 에라토스테네스의 체
// 정수론
// 소수판정
// 에라토스테네스의 체

#include <iostream>
#include<cmath>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <string>
using namespace std;

int arr[1001];

int main(){
    int N, K;
    cin >> N >> K;
    int cnt = 0;
    
    for (int i = 2; i <= N; i++){
        for (int j = i; j <= N; j+=i){
            
            if(arr[j]==0){
                arr[j] = 1;
                cnt++;
                if(cnt == K){
                    cout<< j;
                    exit(0);
                }
            }
        }
    }
    
    
    return 0;
}
