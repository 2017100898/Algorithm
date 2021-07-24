// [1306] 달려라 홍준
// 세그먼트 트리
// 슬라이딩 윈도우

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main(){
    int N, M;
    int num;
    cin>> N >> M;
    int* arr = new int[N];
    priority_queue<int> que;
    
    for(int i = 0 ; i<N; i++){
        cin>>num;
        arr[i]=num;
    }
    
    int start = 1;
    int maxnum = *max_element(arr, arr+(2*M-1));
    cout<<maxnum<<' ';

    
    for(int end = 2*M-1; end<N; end++){
        if(arr[start-1] != maxnum){
            if(arr[end] >= maxnum){
                maxnum = arr[end];
            }
        }
        
        else{
            if(arr[end] >= maxnum){
                maxnum = arr[end];
            }
            
            else{
                for(int i=start; i<end+1; i++)
                {
                    que.push(arr[i]);
                }
                maxnum = que.top();
                
                for(int i=start; i<end+1; i++)
                {
                    que.pop();
                }
            }
            
        }
        
        start++;
        if(end != N-1){
            cout<<maxnum<<' ';
        }
        else{
            cout<<maxnum;
        
        }
    }
    
    delete[] arr;
    return 0;
    
}
