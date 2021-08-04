// [2805] 나무 자르기
// 이분 탐색

#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    long long tree, T, num;
    cin >> tree >> T;

    long long arr[tree];

    for(long long i = 0; i<tree; i++){
        cin>>num;
        arr[i] = num;
    }

    if(tree==1){
        cout<<arr[0]-T;
        exit(0);
    }


    long long start =0;
    long long end = *max_element(arr , arr + tree);
    long long mid = (start+end)/2;
    long long result =0;

    while(1){

        long long sum = 0;
        mid = (start+end)/2;

        for(long long i = 0; i<tree; i++){
            if(arr[i] >= mid){
                sum += (arr[i]-mid);
            }
        }

        if(sum == T){
            result = mid;
            break;
        }

        else if (sum < T){
            end = mid;
            if(start > end){
                break;
            }
        }

        else if (sum > T){
            start = mid;
            result = mid;
            if(end == start+1){
                break;
            }
        }
    }

    cout << result;
}

