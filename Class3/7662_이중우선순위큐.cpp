#include<iostream>
#include<set>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin >> t;
	while (t--) {
		multiset<int>arr;
		int n; cin >> n;
		for (int i = 0; i < n; i++) {
			char a; cin >> a;
			int x; cin >> x;
			if (a == 'I')
				arr.insert(x);

			else {
				if (arr.empty())
					continue;
				if (x == 1) {
					auto iter = arr.end();
					iter--;
					arr.erase(iter);
				}
				else {
					auto iter = arr.begin();
					arr.erase(iter);
				}
			}
		}
		if (arr.empty())
			cout << "EMPTY" << "\n";
		else {
			auto end = arr.end();
			end--;
			cout << *end << " " << *arr.begin() << "\n";
		}
	}
	return 0;
}