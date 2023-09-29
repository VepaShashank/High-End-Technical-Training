#include<stdio.h>
main() {
	int a[]={1,2,3,4,5,6,7,};
	int x=0,i=0;
	for(i=0;i<=8;i++)
	x=x^i;
	for(i=0;i<8-1;i++)
	x=x^a[i];
	printf("%d",x);
}