// [1806] 부분합
// 두 포인터

#include<iostream>
using namespace std;

int sliding(int* arr, int M, int N);

int main(){
    int N, M, number;
    cin>>N>>M;
    int arr[N+1];

    for (int i=0; i < N; i++){
        cin>> number;
        arr[i] = number;
        
    }
    
    cout<<sliding(arr, M, N);

}

int sliding(int* arr, int M, int N){
    int sum = 0;
    int start = 0;
    int minlen = 0;
    //len = end - start + 1;
    
    for(int end=0; end < N; end++){
        sum += arr[end];
        
        if (sum >= M) {
            if (minlen==0) {
                minlen = end-start+1;
            }
            else if (minlen > end-start+1) {
                minlen = end-start+1;
            }
            
            sum -= arr[start];
            start += 1;
            
            if(start<=end){
                sum -= arr[end];
                end--;
            }
        }
    }
    
    return minlen;
}

