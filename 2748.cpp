#include <iostream>
using namespace std;

int main() {
	int n;
	long tmp, p0 = 0, p1 = 1;
	cin >> n;
	for (int i = 0; i < n-1; i++) {
		tmp = p0 + p1;
		p0 = p1;
		p1 = tmp;
	}
	cout << p1;
	return 0;
}