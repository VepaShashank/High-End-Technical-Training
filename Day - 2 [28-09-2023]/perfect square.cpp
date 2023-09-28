#include <stdio.h>
#include <math.h>

int main() {
	int i,squareroot,n,m;
	printf("Enter 1st number : ");
	scanf("%d",&n);
	printf("Enter 2nd number : ");
	scanf("%d",&m);
 
    printf("between %d & %d, The perfect squares are : \n",n,m);
    for(i=n;i<=m;i++)
	{
        squareroot=sqrt(i);
        if(squareroot*squareroot==i)
		{
            printf("%d\n",i);
        }
    }
    return 0;
}