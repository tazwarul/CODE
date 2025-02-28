#include<bits/stdc++.h>
using namespace std;
class myqueue
{
  public:
  queue<int>v;
  void enqueue(int val)
  {
    v.push(val);
    cout<<" Enqueued "<<val<<endl;

  }

  void dequeue()
  {
    if(!v.empty())
    {
        cout<<" Dequeued "<<v.front()<<endl;
        v.pop();
    }

    else 
    {
        cout<<"queue is empty"<<endl;
    }
  }

  void display()
  {
    if(!v.empty())
    {
        queue<int>temp=v;
        cout<<"queue element : ";
        while(!temp.empty())
        {
          cout<<temp.front()<<endl;
          temp.pop();
        }
        cout<<endl;
    }
    else{
        cout<<"queue is empty:";
    }
  }
};

int main()
{
    myqueue q;
    int n;
    cout<<"Enter N: ";
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cout<<"Enter element: "<<i+1<<":";
        int x;
        cin>>x;
        q.enqueue(x);
        q.display();
    }
}