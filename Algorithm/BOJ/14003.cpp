// [14003] 가장 긴 증가하는 부분 수열 5
// 가장 긴 증가하는 부분 수열: o(n log n)
// 이분 탐색

#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

vector<long> vec;
stack<long> st;
long arr[1000001][2];

int main(){
    cin.tie(0);
    int N, index, maxIndex  = 0;
    long A;

    cin >> N; //수열의 크기

    // 1. for문 돌면서 숫자 A를 N개 만큼 입력 받음
    // 2. arr[i][0]에 숫자 A 저장
    // 3. vec 비었을 때: A를 vec에 넣음
    //    vec 차있을 때: vec의 마지막 숫자보다 A가 크면 vec.push_back
    //                   A가 더 작으면 lower_bound 이분탐색 돌려서 적절한 index값 찾음
    // 4. arr[i][1]에 할당 된 vec index 저장
    // 5. arr[i][1] 뒤에서부터 순회하여 vec.size에서 0까지 해당하는 값 하나씩 추출해서 stack에 push
    // 6. stack 값 하나씩 출력

    for(int i= 0; i<N; i++){

        cin>>A;
        arr[i][0] = A;

        if(vec.empty()){  // vec 비었을 때
            vec.push_back(A);
            index = 0;
        }

        else{ //vec에 숫자 존재할 때
            if(vec.back() < A){ //vec.back 보다 A가 클 때
                vec.push_back(A);
                index = vec.size() - 1;
            }

            else{//vec.back 보다 A가 작을 때 -> lower_bound 이분탐색
                index = lower_bound(vec.begin(), vec.end(), A) - vec.begin();
                vec[index] = A;
            }
        }

        // maxIndex는 꾸준히 업데이트
        if(index > maxIndex)
            maxIndex = index;

        //
        arr[i][1] = index;
    }

    // vec.size 를 통해 가장 긴 부분 수열의 길이 출력
    cout<< vec.size() <<'\n';

    int a = maxIndex;

    // arr[i][1] 뒤에서부터 순환 -> a값 하나씩 줄여가며 증가수열에 해당하는 값 파악 후 stack에 삽입
    // vec.size부터 0까지...
    for(int i = N-1; i>=0; i--){
        if(arr[i][1] == a){
            st.push(arr[i][0]);
            a--;
        }
        if(a < 0){
            break;
        }
    }

    // stack 값 하나씩 빼면서 출력
    while(!st.empty()){
        cout<<st.top()<<' ';
        st.pop();
    }
}