// [20414] MVP 다이아몬드 (Normal)
// 다이나믹 프로그래밍

#include<iostream>
using namespace std;

int main() {
	int number;
	int b, s, g, p, d;
	int result = 0;
	cin >> number;
	cin >> s >> g >> p >> d;

	b= s-1;
	s= g-1;
	g= p-1;
	p = d-1;

	char level;
	char* arr = new char[number+1];
	int* arr2 = new int[number + 1];

	for (int i = 0; i < number; i++) {
		cin >> level;
		arr[i] = level;

		if (level == 'B')
			arr2[i] = b;
		else if (level == 'S')
			arr2[i] = s;
		else if (level == 'G')
			arr2[i] = g;
		else if (level == 'P')
			arr2[i] = p;
		else if (level == 'D')
			arr2[i] = d;
	}


	for (int i = 0; i < number-1; i++) {
		int j = i + 1;

		if (arr[i] == 'D') {
			arr2[i] = d;
		}

		if (arr2[i]<=arr2[j] && arr[j] != 'D') {
			arr2[j] = arr2[j] - arr2[i];
		}

		else if (arr2[i] <= arr2[j] && arr[j] == 'D') {
			arr2[j] = d;
		}

		else if (arr2[j] < arr2[i]) {
			arr2[i] = arr2[j];
			arr2[j] = 0;
		}
	}

	for (int i = 0; i < number ; i++) {
		result += (int)arr2[i];
	}

	cout << result;

	delete[] arr;
	delete[] arr2;
}