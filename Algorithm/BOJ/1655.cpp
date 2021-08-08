// [1655] 가운데를 말해요
// 우선순위 큐

#include <iostream>
#include <queue>
#include <stdio.h>
using namespace std;

int main(){
    int test, num;
    priority_queue<int> maxque;
    priority_queue<int, vector<int>, greater<int>> minque;
    scanf("%d", &test);

    for(int i=1; i<=test; i++){
        scanf("%d", &num);
        if(maxque.size() - minque.size() == 0){
            maxque.push(num);
        }

        else
            minque.push(num);

        if(!maxque.empty() && !minque.empty()){
            if(maxque.top()>minque.top()){
                maxque.push(minque.top());
                minque.pop();
                minque.push(maxque.top());
                maxque.pop();
            }
        }
        cout<<maxque.top()<<'\n';
    }
    return 0;
}