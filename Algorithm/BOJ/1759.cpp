// [1759] 암호 만들기
// 브루트포스 알고리즘
// 조합론
// 백트래킹

#include<iostream>
#include<algorithm>
using namespace std;

int n, m;
char element;
char arr[15];
bool issued[15];
char newarr[15];
bool check = false;
int notcheck = 0;

void func(int k) {

	check = false;
	notcheck = 0;

	if (k == n) {
		for (int i = 0; i < n; i++) {
			if (arr[i] == 'a' || arr[i] == 'e' || arr[i] == 'i' || arr[i] == 'o' || arr[i] == 'u')
				check = true;
			else
				notcheck++;
		}

		if (check == true && notcheck >=2) {
			for (int i = 0; i < n; i++) {
				cout << arr[i];
			}
			cout << '\n';
			return;
		}
	}

	else {
		for (int i = 1; i <= m; i++) {
			if (k == 0 || arr[k-1] < newarr[i-1]) {
				arr[k] = newarr[i - 1];
				func(k + 1);
			}
		}
	}
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> m;
	
	for (int i = 0; i < m; i++) {
		cin >> element;
		newarr[i] = element;
	}

	sort(newarr, newarr + m);

	func(0);
}

