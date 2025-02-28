#include<bits/stdc++.h>
using namespace std;
int main()
{
   int n;
   cin>>n;
   int a[n];
   for(int i=0;i<n;i++)
   {
    cin>>a[i];
   }
   int x;
   cin>>x;

   int l=0;
   int r=n-1;
   int index=-1;

   while(l<=r)
   {
      int mid=(l+r)/2;
      if(a[mid]==x)
      {
         index=mid;
         break;
      }
      else if(x>a[mid])

      {
         l=mid+1;
      }

      else 
      {
         r=mid-1;
      }

   }


   if(index==-1)
   {
      cout<<"No";
   }

   else
   cout<<"Index :"<<index;
   return 0;
}