// [2568] 전깃줄 - 2
// 가장 긴 증가하는 부분 수열: o(n log n)

#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

vector<long> vec;
stack<long> st;
long arr[1000001][2] = {0, };

int main(){
    cin.tie(0);
    int N, index, maxIndex  = 0;
    long A, B, maxB = 0;
    cin >> N;

    for(int i= 0; i<N; i++) {
        cin >> B >> A;
        arr[B - 1][0] = A;
        if(maxB < B) maxB = B;
    }

    for(int i = 0; i<maxB; i++){
        if(arr[i][0] > 0) {
            if (vec.empty()) {
                vec.push_back(arr[i][0]);
                index = 0;
            }

            else {
                if (vec.back() < arr[i][0]) {
                    vec.push_back(arr[i][0]);
                    index = vec.size() - 1;
                }

                else {
                    //lower_bound 이분탐색
                    index = lower_bound(vec.begin(), vec.end(), arr[i][0]) - vec.begin();
                    vec[index] = arr[i][0];
                }
            }

            if (index > maxIndex)
                maxIndex = index;

            arr[i][1] = index;
        }

        else {
            arr[i][1] = -1;
        }
    }

    cout<< N - vec.size() <<'\n';

    int a = maxIndex;

    for(int k= maxB-1; k>=0; k--){
        if(arr[k][1]!=-1) {
            if (arr[k][1] != a) {
                st.push(k + 1);

            } else {
                a--;
            }
        }
    }

    while(!st.empty()){
        cout<<st.top()<<'\n';
        st.pop();
    }
}

