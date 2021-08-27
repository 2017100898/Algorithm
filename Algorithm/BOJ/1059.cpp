// [1059] 좋은 구간
// 브루트포스 알고리즘

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    int L, x, n;
    int A, B;
    int res = 0;
    vector<int> vec;

    //집합 S의 크기 input
    cin >> L;

    //집합 S에 포함되는 정수 input 후 vector에 insert
    for (int i = 0; i < L; i++) {
        cin >> x;
        vec.push_back(x);
    }

    //n input
    cin >> n;
    vec.push_back(n);

    //sorting
    sort(vec.begin(), vec.end());

    //begin+1 ~ end-1까지
    for (int i = 0; i < vec.size(); i++) {
        if (vec[i] == n && i != 0 && i != (vec.size() - 1)) {
            A = vec[i - 1] + 1;
            B = vec[i + 1] - 1;
        }

        else if (vec[i] == n && i == 0) {
            A = 1;
            B = vec[i + 1] - 1;
        }

        else if (vec[i] == n && i == (vec.size() - 1)) {
            A = vec[i - 1] + 1;
            B = n;
        }
    }

    for (int i = A; i <= n; i++) {
        for (int j = B; j >= n; j--) {
            if (i < j) {
                res++;
            }
        }
    }
    cout << res;
}