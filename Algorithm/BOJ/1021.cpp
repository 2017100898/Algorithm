// [1021] 회전하는 큐
// 덱

#include<iostream>
#include<deque>
using namespace std;

int i = 0;
int N, M, elem, result = 0;
deque<int> que;
deque<int> queTarget;

void toFront() {
    while (que.front() != queTarget.front()) {
        que.push_front(que.back());
        que.pop_back();
        result++;
    }

    que.pop_front();
    queTarget.pop_front();
    i = 0;
}

void toBack() {

    while (que.front() != queTarget.front()) {
        que.push_back(que.front());
        que.pop_front();
        result++;
    }

    que.pop_front();
    queTarget.pop_front();
    i = 0;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        cin >> elem;
        queTarget.push_back(elem);
    }

    for (int i = 0; i < N; i++) {
        que.push_back(i + 1);
    }

    while(!queTarget.empty()){


        if (que[i] == queTarget.front()) {
            if (i > (que.size() / 2)) {
                toFront();
            }

            else {
                toBack();
            }

        }

        else {
            i++;
        }
    }

    cout << result;
}
