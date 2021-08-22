// [1929] 소수
// 소수판정
// 정수론

#include<iostream>
using namespace std;

int main() {
    unsigned long long A, B;
    long long sosu;
    cin >> A >> B;

    int* arr = new int[B+1];
    arr[0] = 1;
    arr[1] = 1;

    for (unsigned long long i = 2; i <= B; i++) {
        if (arr[i] == 1) {
            continue;
        }

        sosu = i;
        for (unsigned long long j = 2 * i; j <= B; j += i)
            arr[j] = 1;

    }

    for (unsigned long long i = A ; i <= B; i++) {
        if (arr[i] != 1) {
            if (sosu==i)
                cout << i;
            else
                cout << i << '\n';
        }


    }

    delete[] arr;
    return 0;
}