#include<stdio.h>
int main() {
	int a=10;
	int b=++a + a++ - --a - ++a + a++;
	printf("a=%d \n",a);
	printf("b%=%d \n",b);
}