#include <bits/stdc++.h>
using namespace std;

int main()
{
    int l, h;
    cin >> l >> h;

    int limit = sqrt(h);

    vector<bool> range(h - l + 1, true);
    vector<bool> sieve(limit + 1, true);
    sieve[0] = sieve[1] = false;
    for(int i = 2; i * i <= limit; i++)
    {
        if(sieve[i])
        {
            for(int j = i * i; j <= limit; j += i)
                sieve[j] = false;
        }
    }
    for(int i = 2; i <= limit; i++)
    {
        if(sieve[i])
        {
            int start = max(i * i, ((l + i - 1) / i) * i);

            for(int j = start; j <= h; j += i)
                range[j - l] = false;
        }
    }
    if(l == 0) range[0] = false;
    if(l <= 1 && h >= 1) range[1 - l] = false;
    for(int i = 0; i <= h - l; i++)
    {
        if(range[i])
            cout << i + l << " ";
    }
}