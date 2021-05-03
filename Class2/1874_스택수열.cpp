#include <iostream>
#include <stack>
#include <vector>
using namespace std;
int main() {
	vector<char> res;
	int n, x, max = 0;
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	stack<int> s;
	while (n--) {
		cin >> x;
		if (x > max) {
			for (int i = max + 1; i <= x; i++) {
				s.push(i);
				res.push_back('+');
			}
		}
		else {
			if (s.top() != x) {
				cout << "NO";
				return 0;
			}
		}
		s.pop();
		res.push_back('-');
		if (max < x) max = x;
	}
	for (int i = 0; i <res.size(); i++)
		cout << res[i] << '\n';
	
	return 0;
	
}