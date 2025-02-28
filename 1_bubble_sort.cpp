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

int cnt=1;
while(cnt<n)
{
  //5for(int j=1;j<n;j++)
  for(int i=0;i<n-cnt;i++)
  {
   if(ar[i]>ar[i+1])
   {
      int temp=ar[i];
      ar[i]=ar[i+1];
      ar[i+1]=temp;
   }

  }
  cnt ++;
}

for(int i=0;i<n;i++)
   {
      cout<<ar[i]<<" ";
   }

}