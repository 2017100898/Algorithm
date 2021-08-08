// [4358] 생태학
// 문자열
// 트리를 사용한 집합과 맵
// 해시를 사용한 집합과 맵

#include <iostream>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

vector<string> tree;

int main(){
    char c[51];
    string str;
    int i = 0;

    while (1) {
        cin.getline(c, 50);
        if (cin.eof() == true) {
            break;
            }
        
        str = c;
        tree.push_back(str);
        i++;
    }

    
    sort(tree.begin(), tree.end());
    int start = 0;
    int num = 1;
    
    for(int end = 1; end < i+1; end++){
        if(tree[start] == tree[end]){
            num++;
        }
        
        else{
            cout<<fixed;
            cout.precision(4);
            cout<< tree[start] << " " << (num*100.0)/(i) << '\n';
            num = 1;
            start = end;
        }
    }
    
    return 0;
}
