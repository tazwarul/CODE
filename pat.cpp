#include<bits/stdc++.h>
using namespace std;
int pat(string text,string pattern)
{
    int n=text.length();
    int m=pattern.length();

    for(int i=0;i<=n-m;i++)
    {
        if(text.substr(i,m)==pattern)
        {
            return i;
        }
       
    }
    return -1;

}
int main()
{
   string text,pattern;
   cout<<"Enter text: ";
   cin>>text;
   cout<<"Enter pattern: ";
   cin>>pattern;

   int result= pat(text,pattern);
   if(result==-1)
   {
     cout<<"None"<<endl;
   }
   else
   {
    cout<<"found at "<<result;
   }

   return 0;
}