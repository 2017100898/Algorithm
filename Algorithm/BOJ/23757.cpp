#include <iostream>
#include <queue>
#include <functional>

using namespace std;

int main() {

	int N, M;
	priority_queue<int> c_list;
	vector<int> w_list;
	int elem, w_size, c_size;

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		cin >> elem;
		c_list.push(elem);
	}

	for (int i = 0; i < M; i++) {
		cin >> elem;
		w_list.push_back(elem);
	}
	
	for (int i = 0; i < M ; i++){
		
		if (c_list.empty()) {
			cout << 0;
			return 0;
		}

		w_size = w_list.at(i);
		c_size = c_list.top();

		if (w_size <= c_size) {
			c_list.pop();
			
			if (w_size != c_size) {
				c_list.push(c_size - w_size);
			}
		}

		else {
			cout << 0;
			return 0;
		}
	}
	cout << 1;
	
	return 0;
}