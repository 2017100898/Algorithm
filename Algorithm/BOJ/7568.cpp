#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    int N;
    int weight[50], height[50], rank[50] = {0};
    
    cin >> N;
    
    for(int i = 0; i < N; i++){
        int x, y;
        cin >> x >> y;
        
        weight[i] = x;
        height[i] = y;
    }
    
    
    //weight
    for(int i = 0; i < N; i++){
        int temp = 1;
        for(int j = 0; j < N; j++){
            if(i != j){
                if(weight[i] < weight[j]){
                    if(height[i] < height[j]){
                        temp++;
                    }
                }
            }
        }
        rank[i] = temp;
        cout << rank[i] <<" ";
    }
    
    return 0;
}
