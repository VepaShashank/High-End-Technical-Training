#include<stdio.h>
main() {
	int a = 10;
	if(a>100 || a++<200 || a++==12)
	{
		printf("Hello %d",a);
	}
	else{
		printf("Hi %d",a);
	}
}