#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int n;
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	vector<pair<int, int>> v;

	cin >> n;
	int st, et;
	for (int i = 0; i < n; i++) {
		cin >> st >> et;
		v.push_back({ et, st });
	}
	sort(v.begin(), v.end());
	int cnt = 0;
	int t = 0;
	for (int i = 0; i < n; i++) {
		if (t <= v[i].second) {
			t = v[i].first;
			cnt++;
		}
	}
	cout << cnt;
}