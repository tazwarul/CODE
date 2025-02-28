#include <iostream>
#include <string>
using namespace std;

int patternMatching(string text, string pattern)
{
    int n = text.length();
    int m = pattern.length();
    for (int i = 0; i <= n - m; i++)
    {
        if (text.substr(i, m) == pattern)
        {
            return i;
    
        }
    }
    return -1;
}

int main()
{
    string text, pattern;
    cout << "Enter the text: ";
    cin >> text;
    cout << "Enter the pattern: ";
    cin >> pattern;
    int result = patternMatching(text, pattern);
    if (result == -1)
    {
        cout << "Pattern not found!";
    }
    else
    {
        cout << "Pattern found at index: " << result;
    }
    return 0;
}
