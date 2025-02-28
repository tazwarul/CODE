#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int n, capacity;
    
    // ইউজার থেকে ইনপুট নেওয়া
    cout << "Enter number of items: ";
    cin >> n;

    int profit[n], weight[n];

    cout << "Enter the profits of items: ";
    for (int i = 0; i < n; i++) 
    {
        cin >> profit[i];
    }

    cout << "Enter the weights of items: ";
    for (int i = 0; i < n; i++) 
    {
        cin >> weight[i];
    }

    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    // DP টেবিল তৈরি (সবার শুরুতে 0 দেওয়া হয়েছে)
    int k[n + 1][capacity + 1] = {0}; 

    // টেবিল পূরণ করা হচ্ছে
    for (int i = 0; i <= n; i++) 
    {
        for (int w = 0; w <= capacity; w++) 
        {
            if (i == 0 || w == 0) 
            {
                k[i][w] = 0; // প্রথম সারি ও কলামে সবসময় 0 থাকবে
            }
            else if (weight[i - 1] <= w) 
            {
                k[i][w] = max(k[i - 1][w], profit[i - 1] + k[i - 1][w - weight[i - 1]]);
            }
            else 
            {
                k[i][w] = k[i - 1][w]; // ওজন না ধরলে আগের মান কপি করা হবে
            }
        }
    }

    // সর্বোচ্চ প্রফিট প্রিন্ট করা হচ্ছে
    cout << "Maximum Profit: " << k[n][capacity] << endl;

    return 0;
}
