// [5052] 전화번호 목록
// 트리
// 트라이

#include <iostream>
#include <vector>
using namespace std;

const int NUMBER = 10;
int toIndex(char ch) { return ch - '0'; }

struct TrieNode{
    TrieNode* child[NUMBER];

    TrieNode(): child() {}

    ~TrieNode(){
        for (int i=0;i<NUMBER;i++)
            if (child[i]) delete child[i];
    }

    void Insert(string& key, int index){
        if(index != key.length() -1){
            int next = toIndex(key[index]);
            if(child[next] == nullptr)
                child[next] = new TrieNode;
            child[next] -> Insert(key, index+1);
        }
    }

    bool Find(string& key, int depth){
        int next = toIndex(key[depth]);
        if(depth == key.length()-1 && child[next] != nullptr)
            return false;

        if(depth == key.length()-1 && child[next] == nullptr)
            return true;

        else{
            return child[next]-> Find(key, depth+1);

        }
    }
};

int main(){
    int T, N;
    string num;
    vector<string> vec;
    cin  >> T;

    for(int i = 0; i<T; i++){
        TrieNode root;

        int result = 0;
        cin >> N;

        for(int j = 0; j<N; j++){
            cin >> num;
            vec.push_back(num);
            root.Insert(num, 0);
        }

        for(int j = N-1; j >= 0; j--){
            if(!root.Find(vec[j], 0)){
                result = 1;
            }
            vec.pop_back();
        }

        if(result == 1)
            cout<<"NO" <<'\n';
        else
            cout<<"YES"<<'\n';

    }
    return 0;
}

