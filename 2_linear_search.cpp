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

   int v;
   cin>>v;
   int flag=0;

for(int i=0;i<n;i++)
{
    if(ar[i]==v)
    {
     flag=1;
     break;
    }
}

if(flag=1)

{
    cout<<"Founded";

}
else
cout<<"Not Founded";
}