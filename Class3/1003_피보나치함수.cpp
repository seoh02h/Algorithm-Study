#include <iostream>
using namespace std;

int main() {
	int t;
	int zero[41];
	int one[41];
	zero[0] = 1;
	one[0] = 0;
	zero[1] = 0;
	one[1] = 1;
	int res_zero = 0;
	int res_one = 0;
	cin >> t;
	int n;
	for (int i = 2; i < 41; i++) {
		zero[i] = zero[i - 1] + zero[i - 2];
		one[i] = one[i - 1] + one[i - 2];
	}
	for (int i = 0; i < t; i++) {
		cin >> n; 
		cout << zero[n] << " " << one[n] << '\n';
	}
}