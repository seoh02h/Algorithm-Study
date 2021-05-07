#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	vector<string> v1(n);
	vector<string> v2;
	for (int i = 0; i < n; i++) {
		cin >> v1[i];
	}

	
	sort(v1.begin(), v1.end());
	string s;
	for (int i = 0; i < m; i++) {
		cin >> s;
		if (binary_search(v1.begin(), v1.end(), s)) {
			v2.push_back(s);
		}
	}
	sort(v2.begin(), v2.end());
	cout << v2.size() << endl;

	for (int i = 0; i < v2.size(); i++) {
		cout << v2[i] << '\n';
	}
}