#include<bits/stdc++.h>
using namespace std;
int main()
{
   int n;
   cout<<"Enter N:";
   cin>>n;
   int ar[n];
   for(int i=0;i<n;i++)
   {
      cin>>ar[i];
   }

   for(int i=1;i<n;i++)
   {
    for(int j=0;j<n-i;i++)
    {
        if(ar[j]>ar[j+1])
   {
      int temp=ar[j];
      ar[j]=ar[j+1];
      ar[j+1]=temp;
   }
    }
   }

   for(int i=0;i<n;i++)
   {
      cout<<ar[i]<<" ";
   }
   return 0;
}