#include <iostream>
#include <vector>
using namespace std;

vector<int> vec;

int main(){

    int N, A;
    cin >> N;

    for(int i= 0; i<N; i++){
        cin>>A;

        if(vec.empty()){ //처음에만 시도
            vec.push_back(A);
        }

        else{ //일반적인 시도
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

    cout<<  vec.size();
}