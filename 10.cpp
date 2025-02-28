#include<bits\stdc++.h>
using namespace std;
void toh(int n,char src,char aux,char dest)
{
    if(n==1)
    {
        cout<<"Move disk- "<<n<<" From "<<src<<" To "<<dest<<endl;
        return ;
    }
    toh(n-1,src,dest ,aux);
    cout<<"Move disk- "<<n<<" From "<<src<<" To "<<dest<<endl;
    toh(n-1,aux,src ,dest);
}
int main()
{
    int n;
    cout<<"Enter N: ";
    cin>>n;
    toh(n,'A','B','C');

}