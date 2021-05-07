#include <iostream>
#include <queue>
using namespace std;
int main() {
	priority_queue<int, vector<int>, less<int >> pq;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	int x;
	cin >> n;
	int res;
	for (int i = 0; i < n; i++) {

		cin >> x;
		if (x == 0) {
			if (pq.empty()) {
				cout << '0' << '\n';
			}
			else {
				res = pq.top();
				cout << res << '\n';
				pq.pop();
			}
		}
		else {
			pq.push(x);
		}
	}
}