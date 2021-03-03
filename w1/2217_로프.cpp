#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, res=0, max=0, tmp;
	cin >> n;
	vector<int> v(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}
	sort(v.rbegin(), v.rend());
	for (int i = 0; i < n; i++) {
		tmp = v[i] * (i + 1);
		if (tmp > max) {
			max = tmp;
		}
	}
	cout << max;
}