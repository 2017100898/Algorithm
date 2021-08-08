// [1202] 보석 도둑
// 그리디 알고리즘
// 우선순위 큐

#include <iostream>
#include <queue>
#include <algorithm>
#include <stdio.h>
using namespace std;

pair<int, int> gold[300001];
int bag[300001];
priority_queue<long long int> pq;

int main(){
    long long int N, K;
    int num1, num2;
    int num;
    long long int result = 0;
    cin>>N>>K;

    //보석 정보
    for(long long int i=0; i<N; i++){
        cin>>num1>>num2;
        gold[i].first = num1;
        gold[i].second = num2;
    }
    
    //가방 정보
    for(long long int j=0; j < K; j++){
        cin>>num;
        bag[j] = num;
    }

    sort(gold, gold+N);
    sort(bag, bag+K);
    
    long long int i = 0; // bag
    long long int j = 0; // gold
    
    while(1){
        while(bag[i] >= (gold[j]).first){
            pq.push(gold[j].second);
            j++;
        }
            
        if(pq.size() <= 0){
            i++;
        }
            
        else{
            result += pq.top();
            pq.pop();
            i++;
        }
        
        if(j>=N && pq.size() <=0){
            cout<<result;
            exit(0);
        }
        
        if(i>=K){
            cout << result;
            exit(0);
        }
    }
    
    return 0;
}
