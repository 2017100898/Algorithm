#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

// K개의 랜선 소유, 길이 제각각임
// N개의 같은 길이로 만들고 싶음 (N개보다 많은 것은 괜찮음)
// 잘라서 남은 랜선은 버려야 함

int K, N, elem;
vector<int> vec;

int search(int mid) {
	int cnt = 0;


	for (int i = 0; i < K; i++) {
		cnt += (vec[i] / mid);
	}

	if (cnt >= N) {
		return 1;
	}

	else {
		return 0;
	}
}

int main() {

	unsigned int min_elem = 999999999;
	unsigned int max_elem = 1;
	unsigned int result = 0;
	

	cin >> K >> N;
	for (int i = 0; i < K; i++) {
		cin >> elem;
		vec.push_back(elem);
	
		if (min_elem >= elem) {
			min_elem = elem;
		}
		if (max_elem <= elem) {
			max_elem = elem;
		}
	}
	
	// parameteric search
	unsigned int left = 1;
	unsigned int right = max_elem;

	while (left <= right) {
		unsigned int mid = (left + right) / 2;

		if (search(mid)) {
			result = max(result, mid);
			left = mid + 1;
		}

		else {
			right = mid - 1;
		}
	}

	cout << result;
	
	return 0;
}