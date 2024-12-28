#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int N, M, elem;
vector<int> vec;

int isPossible(int mid) {
	int cnt = 0;

	for (int i = 0; i < N; i++) {
		if (vec[i] <= mid) {
			cnt += vec[i];
		}
		else {
			cnt += mid;
		}
	}

	if (cnt > M) {
		return 0;
	}

	else {
		return 1;
	}

}


int main() {
	int sum = 0;
	int max_val = 1;
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		cin >> elem; //각 지방의 예산 요청
		vec.push_back(elem);
		sum += elem;
		
		if (max_val <= elem) {
			max_val = elem;
		}
	}

	cin >> M; // 총 예산
	
	// parametric search
	
	//모든 요청이 배정될 수 있는 경우, 그대로 배정
	if (sum <= M) {
		cout << max_val;
	}

	// 모든 요청 배정 못 할 경우,
	// 정수 상한액을 정해서, 그 이상의 예산 요청은 모두 상한액 배정

	else {
		unsigned int left = 1;
		unsigned int right = max_val;
		unsigned int result = 0;

		while (left <= right) {
			unsigned int mid = (left + right) / 2;

			if (isPossible(mid)) {
				result = max(mid, result);
				left = mid + 1;
			}

			else {
				right = mid - 1;
			}

		}
	
		cout << result;
	}
	
	
	return 0;
}