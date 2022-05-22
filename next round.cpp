#include<iostream.h>
using namespace std;
main()
{
	int n,k,i;
	int a[100];
	int sum=0;
	
	cin>> n >> k;
	
	for(i=1;i<=n;i++)
	{
		cin>>a[i];	
	}
	
	for(i=1;i<=n;i++)
	{
		if(a[i]>0 && a[i]>=a[k])
		{
			sum=sum+1;
		}
		
	}
	cout<<sum;
		
}

	

