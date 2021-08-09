// [1956] 운동
// 그래프 이론
// 플로이드-와샬

#include <iostream>
#define INF 10000001
using namespace std;

int arr[401][401];

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

    int min = INF;

    for(int i=1; i<=n-1; i++){
        for(int j=i+1; j<=n; j++) {
            if (min > arr[i][j]+arr[j][i])
                min = arr[i][j]+arr[j][i];
        }
    }

    for(int i=1; i<=n; i++){
        if (min > arr[i][i])
            min = arr[i][i];
    }

    if(min==INF){
        cout<< -1;
    }
    else {
        cout << min;
    }

}