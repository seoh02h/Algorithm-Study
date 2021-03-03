#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
	int n, a,b=-1;
	cin >> n;
	a = n / 5;
	n -= a * 5;
	for (int i = 0; i <= a; i++) {
		n += i * 5;
		if (n % 2 == 0) {
			b = n / 2;
			break;
		}
		a--;
	}
	if (b == -1) {
		cout << "-1";
	}
	else {
		cout << a + b;
	}

}