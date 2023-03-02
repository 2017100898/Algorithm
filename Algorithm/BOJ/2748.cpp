#include<iostream>
using namespace std;

int main() {
	
	long long num;
	cin >> num;
	long long a = 0; 
	long long b = 1;
	long long c = 0;
	
	if (num == 0) {
		cout << c;
	}

	else {
		c = 1;

		for (long long i = 1; i < num; i++) {
			c = a + b;
			a = b;
			b = c;
		}
		cout << c;
	}
	
}