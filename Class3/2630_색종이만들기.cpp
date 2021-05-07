#include <iostream>
#include <vector>
using namespace std;
int paper[129][129];
int b = 0, w = 0;
int n;

void check(int x, int y, int size) {
	if (size == 0)
		return;

	int flag1;
	int flag2 = 1;
	flag1 = paper[x][y];
	for (int i = x; i < x+size; i++) {
		if (!flag2) break;
		for (int j = y; j < y+size; j++) {
			if (flag1 != paper[i][j]) {
				flag2 = 0;
				break;
			}
			
		}
	}
	if (flag2 == 1) {
		if (flag1 == 1) {
			w++;
			return;
		}
		else {
			b++;
			return;
		}
	}
	check(x, y, size / 2);
	check(x + size / 2, y, size / 2);
	check(x, y + size / 2, size / 2);
	check(x + size / 2, y + size / 2, size / 2);

	}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {

		for (int j = 0; j < n; j++) {
			cin >> paper[i][j];
		}

	}

	check(0, 0, n);
	cout << b << '\n' << w;
}