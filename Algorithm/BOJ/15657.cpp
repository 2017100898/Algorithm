// [15657] N과 M (8)
// 백트래킹

#include<iostream>
#include<algorithm>
using namespace std;

int n, m;
int arr[9];
int element;
int newarr[9];
bool issued[9];


void func(int k) {

    if (k == m) {
        for (int i = 0; i < m; i++) {
            cout << arr[i] << " ";
        }
        cout << '\n';
        return;
    }

    else {
        for (int i =1; i <= n; i++) {
            //if(!issued[i]){
            if (k == 0 || arr[k - 1] <= newarr[i - 1]) {
                arr[k] = newarr[i - 1];
                issued[i] = 1;
                func(k + 1);
                issued[i] = 0;
            }
        }
    }

}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> element;
        newarr[i] = element;
    }

    sort(newarr, newarr + n);

    func(0);
}

