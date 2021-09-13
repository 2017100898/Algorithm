// [1365] 꼬인 전깃줄
// 가장 긴 증가하는 부분 수열: o(n log n)

#include <iostream>
#include <vector>
using namespace std;

vector<int> vec;

int main(){

    int N, A;
    cin >> N;

    for(int i= 0; i<N; i++){
        cin>>A;

        if(vec.empty()){
            vec.push_back(A);
        }

        else{
            if(vec.back() < A){
                vec.push_back(A);
            }

            else{
                for(int v = 0; v<vec.size(); v++){
                    if(vec[v] >= A){
                        vec[v] = A;
                        break;
                    }
                }
            }
        }
    }

    cout<< N - vec.size();
}