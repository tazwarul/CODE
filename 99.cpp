#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, c;
    cout << "Enter N and C: ";
    cin >> n >> c;
    int p[n];
    cout<<"P:";
    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
    }
    int we[n];
    cout<<"W:";
    for (int i = 0; i < n; i++)
    {
        cin >> we[i];
    }
    int T[n + 1][c + 1] = {0};

    for (int i = 0; i <= n; i++)
    {
        for (int w = 0; w <= c; w++)
        {
            if (i == 0 || w == 0)
            {
                T[i][w] = 0;
            }
            else if (we[i - 1] <= w)
            {
                T[i][w] = max(T[i - 1][w], p[i - 1] + T[i - 1][w - we[i - 1]]);
            }

            else
                T[i][w] = T[i - 1][w];
        }
    }


    cout<<endl<<"Max Profit: "<<T[n][c];
    return 0;
}