#include <iostream>
#include <vector>
using namespace std;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int arr[51][51];
int marked[51][51];
int m, n;
void search(int i, int j) {
	int x, y;
	for (int k = 0; k < 4; k++) {
		x = i + dx[k];
		y = j + dy[k];
		if (x > -1 && x<m && y>-1 && y < n && marked[x][y] == 0 && arr[x][y] == 1) {
			marked[x][y] = 1;
			search(x, y);
		}
	}
}
int count() {
	int k, x, y, ans=0;
	cin >> m >> n >> k;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			arr[i][j] = 0;
			marked[i][j] = 0;
		}
	}
	for (int i = 0; i < k; i++) {
		cin >> x >> y;
		arr[x][y] = 1;
	}
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i][j] == 1 && marked[i][j] == 0) {
				marked[i][j] = 1;
				search(i, j);
				ans++;
				
			}
		}
	}
	return ans;

}
int main() {
	int t;
	cin >> t;	
	vector<int> res(t);
	for (int i = 0; i < t; i++) res[i]=count();
	for (int i = 0; i < t; i++) cout << res[i] << '\n';

}