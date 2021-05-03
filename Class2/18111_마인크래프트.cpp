#include <iostream>
#include <vector>

using namespace std;

int land[501][501] = { 0, };
int N, M, B;

int main() {
	cin >> N >> M >> B;

	int min = 260;
	int max = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> land[i][j];

			if (land[i][j] < min)
				min = land[i][j];

			if (land[i][j] > max)
				max = land[i][j];
		}
	}

	int time = 1000000000;
	int height = 0;

	bool can_build = false;

	for (int i = min; i <= max; i++) {
		int sum_build = 0;
		int sum_remove = 0;

		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				int temp = i - land[j][k];

				if (temp < 0)
					sum_remove += temp * -1;
				else
					sum_build += temp;
			}
		}

		if (sum_build <= sum_remove + B) {
			int temp = sum_build + sum_remove * 2;
			if (time > temp) {
				time = temp;
				height = i;
			}

			if (temp == time)
				if (height < i)
					height = i;
		}
	}

	printf("%d %d\n", time, height);
}