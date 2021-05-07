#include<iostream>
using namespace std;

int arr[1001][1001];
int visited[1001][1001] = { 0 };
int m, n;
int dx[4] = { 0, 0, 1, 1 };
int dy[4] = { 0, 1, 0, 1 };
int main() {
	cin >> m >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[n][m];
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[n][m];
		}
	}

}