#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cout << "Enter N:";
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    int count = 1;
    while (count < n)
    {
        for (int i = 0; i < n - count; i++)
        {
            cout<<"Pass-"<<count<<"   ";
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
        }

        cout << endl;
       
        for (int i = 0; i < n; i++)
        {

            cout << a[i] << " ";
        }

        cout << endl;

        count++;
    }

    cout << endl;

    cout << "Total Passes:" << count - 1 << endl;

    cout << "Final Array : ";
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    return 0;
}