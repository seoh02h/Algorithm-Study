#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 1000000;
int N;
long long M;
long long tree[MAX];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> N >> M;

	long long low = 1, high = 0;

	for (int i = 0; i < N; i++) {
		cin >> tree[i];
		high = max(high, tree[i]);
	}

	long long result = 0;
	while (low <= high) {
		long long mid = (low + high) / 2;
		long long len = 0;
		for (int i = 0; i < N; i++) {
			if (tree[i] - mid > 0)
				len += tree[i] - mid;
		}
		if (len >= M) {
			result = max(result, mid);
			low = mid + 1;
		}
		else {
			high = mid - 1;
		}
	}
	cout << result;
	return 0;
}