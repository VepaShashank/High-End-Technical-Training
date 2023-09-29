#include<stdio.h>
int main() {
	
	int i,n;
	long long int f1=0,f2=1,f3;
	scanf("%d",&n);
	printf("%lld %lld ",f1,f2);
	for(i=0;i<=n;i++)
	{
		f3=f1+f2;
		printf("%lld ",f3);
		f1=f2;
		f2=f3;
	}
	printf("\n");	
	return 0;
}