// [1072] 게임

#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    long long num1, num2;
    cin>> num2 >> num1;

    long long target= (long long)((num1*100/(num2)));

    target = target+1;
    if (target >= 100){
        cout<< -1;
        exit(0);
    }

    long double X = ((target*num2-num1*100)*1.0)/((100-target));

    if(X - (long long)X == 0){
        cout<<(long long)X;
    }
    else{
        cout << (long long)X+1;
    }
}