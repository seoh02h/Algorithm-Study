#include <iostream>
#include <cstdlib>
#include <map>
#include <string>
using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);

	map<string, int> poketStr;
	map<int, string> poketNum;
	int N, M, num = 1;
	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		string str;
		cin >> str;
		poketStr.insert(make_pair(str, num));
		poketNum.insert(make_pair(num++, str));
	}

	for (int i = 0; i < M; i++)
	{
		char question[21];
		cin >> question;
		if (question[0] < 'A')
		{
			int qNum = atoi(question);
			cout << poketNum[qNum] << '\n';
		}
		else
		{
			cout << poketStr[question] << '\n';
		}
	}
	return 0;
}