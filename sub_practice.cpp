#include<bits\stdc++.h>
using namespace std;

void subset(int arr[],int n,int index,int sum,int target,string current)
{
    if(sum==target)
    {
        cout<<current<<endl;
        return;
    }
    if(index==n||sum>target)
    {
        return;
    }

    subset(arr,n,index+1,sum+arr[index],target,current+to_string(arr[index])+" ");
    subset(arr,n,index+1,sum,target,current);

}

int main()
{
    int n;
    cout<<"Enter N:";
    cin>>n;
    int arr[n];
    cout<<"Enter Set:";
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }

    int target;
    cout<<"Target:";
    cin>>target;
    subset(arr,n,0,0,target," ");
}