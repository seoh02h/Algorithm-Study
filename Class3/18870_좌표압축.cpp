#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<int> v(n); 

    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    vector<int> cv(v); 
    sort(cv.begin(), cv.end());

    cv.erase(unique(cv.begin(), cv.end()), cv.end());
    for (int i = 0; i < n; i++)
    {
        auto it = lower_bound(cv.begin(), cv.end(), v[i]);
        cout << it - cv.begin() << ' ';
    }

    return 0;
}