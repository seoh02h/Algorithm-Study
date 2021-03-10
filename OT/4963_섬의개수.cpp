#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int map[51][51], marked[51][51];
int w, h;
int dx[8] = { 0,1,1,1,0,-1,-1,-1 };
int dy[8] = { -1,-1,0,1,1,1,0,-1 };
void search(int i, int j) {
	int x, y;
	for (int k = 0; k < 8; k++) {
		x = j + dx[k];
		y = i + dy[k];
		if (x >= 0 && x < w && y >= 0 && y < h && map[y][x] == 1 && marked[y][x] == 0) {
			marked[y][x] = 1;
			search(y, x);
			
		}
	}
}
int main() {
	
	while (true) {
		cin >> w >> h;
		int cnt=0;
		if (w + h == 0) {
			break;
		}
		else {
			for (int i = 0; i < h; i++) {
				for (int j = 0; j < w; j++) {
					cin >> map[i][j];
				}
			}
			for (int i = 0; i < h; i++) {
				for (int j = 0; j < w; j++) {
					if (map[i][j] == 1 && marked[i][j] == 0) {
						marked[i][j] = 1; 
						search(i, j);
						cnt++;
					}
					
				}
			}
			cout << cnt << '\n';
		}
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				map[i][j] = 0;
				marked[i][j] = 0;

			}
			cnt = 0;
		}
	}
}