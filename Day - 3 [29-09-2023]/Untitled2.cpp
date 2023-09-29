#include<stdio.h>
main() {
	int count=0,n=12;
	while(n)
	{
		count++;
		n=n&(n-1);
	}
	if(count==1)
	{
		printf("True");	
	}else {
		printf("False");
	}
}