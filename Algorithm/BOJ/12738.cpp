// [12738] 가장 긴 증가하는 부분 수열 3
// 가장 긴 증가하는 부분 수열: o(n log n)
// 이분 탐색

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<long> vec;

int main(){
    cin.tie(0);
    int N, index;
    long A;

    cin >> N;

    for(int i= 0; i<N; i++){
        cin>>A;

        if(vec.empty()){ //처음에만 시도
            vec.push_back(A);
        }

        else{ //일반적인 시도
             // vec.back 보다 A가 더 클 때
            if(vec.back() < A) vec.push_back(A);

            else{ // vec.back 보다 A가 작을 때
                  // lower_bound 이분탐색을 통한 적절한 index 파악
                index = lower_bound(vec.begin(), vec.end(), A) - vec.begin();
                vec[index] = A;
            }
        }
    }

    // vec.size 출력
    cout<< vec.size();
}