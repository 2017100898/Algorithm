// 21921 블로그
// 슬라이딩 윈도우
// 누적 합

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    int N, T;
    int num;
    int result = 0;
    int start = 0;
    int sum = 0;
    int cnt = 1;
    
    cin>>N>>T;
    int arr[N];
    
    for (int i = 0; i<N; i++){
        cin>>num;
        arr[i] = num;
    }
    
    for (int end = 0; end < N; end++){
        
        if (end < T){
            sum += arr[end];
            result = sum;
        }
        
        else{
            sum -= arr[start];
            start++;
            sum += arr[end];

            if (result < sum){
                result = sum;
                cnt = 1;
            }
            
            else if (result == sum){
                cnt++;
            }
        }
        
        
    }
    
    if(result != 0){
        cout<< result<<'\n';
        cout<<cnt;
    }
    
    else{
        cout<<"SAD";
    }
    
    return 0;
}
