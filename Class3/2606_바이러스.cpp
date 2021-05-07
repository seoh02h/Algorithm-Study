#include <iostream>
#include <vector>
#include <queue>
using namespace std;
vector < vector <int> > c(101, vector <int>(101, 0));

vector<int> l;
int visited[101] = { 0 };
int cnt = 0;
int n, t;

void dfs(int x) {
	for (int i = 2; i <= n; i++) {
		if (c[x][i] == 1 && visited[i] == 0) {
			visited[i] = 1;
			cnt++;
			dfs(i);
		}
	}
}

void bfs(int x) {
	queue<int> q;
	q.push(x);
	while (!q.empty()) {
		int node = q.front();
		q.pop();
		for (int i = 1; i <= n; i++) {
			if (!visited[i] && c[node][i] == 1) {
				q.push(i);
				visited[i] = 1;
				cnt++;
			}
		}
	}
}

int main() {
	cin >> n >> t;


	int a, b;
	for (int i = 0; i < t; i++) {
		cin >> a >> b;
		c[a][b] = 1;
		c[b][a] = 1;
	}
	visited[1] = 1;
	//dfs(1);
	bfs(1);
	cout << cnt;
}