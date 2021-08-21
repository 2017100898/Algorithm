// [1475] 방 번호
// 구현

#include<iostream>
using namespace std;

int main() {
    string number;
    cin >> number;
    string set = "0123456789";

    int arr[11] = {};

    for (int i = 0; i < number.length(); i++) {
        for (int j = 0; j < set.length(); j++) {
            if (number[i] == set[j])
                arr[j]++;
        }
    }

    arr[10] = ((max((int)arr[9], (int)arr[6]) - min((int)arr[9], (int)arr[6])+1)/2) + min((int)arr[9], (int)arr[6]);
    arr[9] = 0;
    arr[6] = 0;

    int max = arr[0];
    for (int j = 0; j < 11; j++) {
        if (arr[j] > max)
            max = arr[j];
    }

    cout << max;
}