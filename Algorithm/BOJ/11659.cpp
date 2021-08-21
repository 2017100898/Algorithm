// [11659] 구간 합 구하기4
// 누적합

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <stdio.h>
using namespace std;

int main(){
    int N, M, num, R, L;
    cin>>N>>M;
    int arr[100001];
    int arr2[100001];
    int sum = 0;
    for(int i=0; i<N; i++){
        scanf("%d", &num);
        arr[i]=num;
    }
    arr2[0] = 0;
    for(int i=1; i<N+1; i++){
        sum+=arr[i-1];
        arr2[i]=sum;
    }

    for(int i=0; i<M; i++){
        scanf("%d", &L);
        scanf("%d", &R);
        printf("%d\n", arr2[R]-arr2[L-1]);
    }

    return 0;
}