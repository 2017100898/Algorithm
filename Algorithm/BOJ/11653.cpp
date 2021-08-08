// [11653] 소인수분해
// 정수론
// 소수 판정

#include<iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long N;
    cin >> N;

    long long element = 2;

    while (1) {

        if (N <= 1) {
            return 0;
        }

        else {

            if (N < (element * element)) {
                cout << N;
                return 0;
            }

            else if (N % element == 0 && N >= (element * element)) {
                cout << element << '\n';
                N /= element;
            }

            else if (N % element != 0 && element % 2 == 1) {
                element += 2;
            }

            else if (N % element != 0 && element % 2 == 0) {
                element += 1;
            }
        }
    }
}

