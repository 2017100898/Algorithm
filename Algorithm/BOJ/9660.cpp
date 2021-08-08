// [9660] 돌 게임 6
// 게임 이론

#include<iostream>
#include<algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    unsigned long long num;
    cin >> num;
    if (num <= 7) {
        if (num == 2 || num == 7) {
            cout << "CY";
        }

        else {
            cout << "SK";
        }
    }

    else {

        if (num % 7 == 2 || num % 7 == 0) {
            cout << "CY";
        }

        else {
            cout << "SK";
        }

    }

}
