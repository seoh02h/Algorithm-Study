#include <iostream>
using namespace std;
int dp[1000001] = { 0 };


int main() {
	int n;
	cin >> n;

	dp[2] = 1;
	dp[3] = 1;

	for (int i = 4; i <= n; i++) {
		dp[i] = dp[i - 1]+1;
		if (i % 3 == 0) {
			if (dp[i / 3] < dp[i]) {
				dp[i] = dp[i / 3]+1;
			}
		}
		if (i % 2 == 0) {
			if (dp[i / 2] < dp[i]) {
				dp[i] = dp[i / 2]+1;
			}
		}

	}
	cout << dp[n];

}

