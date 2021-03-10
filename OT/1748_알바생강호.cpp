#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
	int n, tip;
	long long sum = 0;
	cin >> n;
	vector<int> vec(n);
	for (int i = 0; i < n; i++) {
		cin >> vec[i];
	}
	sort(vec.rbegin(), vec.rend());
	for (int i = 0; i < n; i++) {
		tip = vec[i] - i;
		if (tip > 0) {
			sum += tip;
		}
	}
	cout << sum;
}