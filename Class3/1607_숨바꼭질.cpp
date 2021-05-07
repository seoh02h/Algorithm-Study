#include <iostream>
#include <vector>
#include <queue>
using namespace std;
bool visited[100001] = { 0 };
int path[100001] = { 0 };
int main() {
	int t, n, m, k;
	int x, y;
	int res;
	cin >> n >> k;
	queue<int> q;
	q.push(n);
	while (!q.empty()) {
		int w = q.front();
		if (w == k)
			break;
		q.pop();
		if (visited[w + 1] == 0 && w + 1 >= 0&& w + 1 < 100001) {
			visited[w + 1] = true;
			q.push(w + 1);
			path[w + 1] = path[w] + 1;
		}if (visited[w - 1] == 0 && w - 1 >= 0&& w - 1 < 100001) {
			visited[w - 1] = true;
			q.push(w - 1);
			path[w - 1] = path[w] + 1;
		}
		if (visited[w * 2] == 0 && w * 2 >= 0 && w * 2 < 100001) {
			visited[w * 2] = true;
			q.push(w * 2);
			path[w * 2] = path[w] + 1;
		}
	}
	cout << path[k];


}