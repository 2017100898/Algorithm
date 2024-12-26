#include <iostream>
#include <queue>
#include <functional>
using namespace std;

int main() {

	int N, my_num;
	int elem;
	int result = 0;
	priority_queue<int> pq;
	cin >> N;
	cin >> my_num;

	for (int i = 0; i < N - 1; i++) {
		cin >> elem;
		pq.push(elem);
	}

	while (!pq.empty()) {
		if (pq.top() >= my_num) {
			elem = pq.top();
			pq.pop();
			pq.push(elem - 1);
			my_num++;
			result++;
		}
		
		else {
			cout << result;
			return 0;
		}
	}

	if (pq.empty()) {
		cout << result;
	}

	return 0;

}