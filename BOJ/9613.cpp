// [9613] GCD 합
// 정수론
// 유클리드 호제법

#include<iostream>
#include<algorithm>
using namespace std;

long long GCD(int a, int b);

int main(){
    cin.tie(0);
    int t, n, num;
    cin>> t;

    for(int i= 0; i<t; i++){
        cin>>n;
        long long result = 0;
        int arr[101];
        for(int j = 0; j<n; j++){
            cin >> num;
            arr[j] = num;
        }

        for(int j = 0; j<n-1; j++){
            for(int k=j+1; k<n; k++){
                result += GCD(max(arr[j],arr[k]), min(arr[j],arr[k]));
            }
        }
        cout<<result<<'\n';
    }
    return 0;
}

long long GCD(int a, int b){
    if( a%b == 0){
        return b;
    }

    else{
        int c = a%b;
        return GCD(b, c);
    }
}