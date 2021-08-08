// [2075] N번째 큰 수
// 우선순위 큐
// 정렬

#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N, elem;
    cin >> N;
    priority_queue<int, vector<int>, greater<int>> que;


    for (int i = 0; i < (N*N); i++) {
        cin >> elem;

        if (i < N) {
            que.push(elem);
        }
    
        else {
            if (elem > que.top()) {
                que.pop();
                que.push(elem);
            }
        }
    }

    cout << que.top();

}
