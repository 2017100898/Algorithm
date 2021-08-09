// [11404] 플로이드
// 그래프 이론
// 플로이드-와샬

#include <iostream>
#define INF 10000001
using namespace std;

int arr[101][101];

void Floyd(int n){
    for(int m = 1; m<=n; m++){
        for(int s=1; s<=n; s++){
            for(int e=1; e<=n; e++){
                if(arr[s][e] > arr[s][m] + arr[m][e]){
                    arr[s][e] = arr[s][m] + arr[m][e];
                }
            }
        }
    }
}

int main(){
    cin.tie(0);
    int n, m, u, v, w;
    cin >> n >> m;

    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++) {
            if(i!=j)
                arr[i][j] = INF;
        }
    }

    for(int i = 0; i<m; i++){
        cin>> u>> v>> w;
        if(arr[u][v] == INF) {
            arr[u][v] = w;
        }
        else{
            if(arr[u][v] > w){
                arr[u][v] = w;
            }
        }
    }

    Floyd(n);

    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(arr[i][j]==INF){
                cout<< 0 <<' ';
            }
            else{
                cout<<arr[i][j] <<' ';
            }
        }
        cout<<'\n';
    }
}