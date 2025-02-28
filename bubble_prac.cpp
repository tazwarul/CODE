#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cout << "Enter n:";
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    int cnt = 1;
    while (cnt < n)
    {
        for (int i = 0; i < n - cnt; i++)

        {
            if (a[i] > a[i + 1])
            {
                int temp = a[i];
                a[i] = a[i + 1];
                a[i + 1] = temp;

                for (int i = 0; i < n; i++)
                {
                    cout << a[i] << " ";
                }
                cout<<endl;
            }
        }cout<<endl;
        cnt++;
    }

    cout<<"Final Array is "; 
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    return 0;
}