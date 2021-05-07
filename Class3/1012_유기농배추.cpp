#include <iostream>
#include<cstring>
using namespace std;

int dy[4] = { 1,-1, 0, 0 };
int dx[4] = { 0,0,1,-1 };
int M, N, K;
int arr[51][51] = { 0 };
int visited[51][51] = { 0 };

void dfs(int y, int x) {
	for (int i = 0; i < 4; i++) {
		int ny = y + dy[i];
		int nx = x + dx[i];
		if (ny < 0 || ny >= N || nx<0 || nx>=M)
			continue;
		if (arr[ny][nx] && !visited[ny][nx]) {
			visited[ny][nx]++;
			dfs(ny, nx);
		}
	}
}

int main() {
	int t, x, y;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> M >> N >> K;
		memset(arr, 0, sizeof(arr));
		memset(visited, 0, sizeof(visited));

		int res = 0;
		for (int j = 0; j < K; j++) {
			cin >> x >> y;
			arr[y][x] = 1;
		}

		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				if (arr[j][k] && !visited[j][k]) {
					res++;
					visited[j][k]++;
					dfs(j, k);
				}
			}
		}
		cout << res << '\n';
	}
}