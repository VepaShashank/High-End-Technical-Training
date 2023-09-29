#include <stdio.h>
int main()
{
int num, tmp, reverse = 0, digit_of_num, digitSum = 0 ;
printf("Enter a Number: \n");
scanf("%d", &num);
tmp = num;
while (tmp > 0)
{
digitSum = digitSum + tmp % 10; 
tmp = tmp / 10;
}
tmp = digitSum; 
printf("\n The sum of the digits = %d", tmp);
while (tmp > 0)
{
reverse = reverse * 10 + tmp % 10;
tmp = tmp / 10;
}
printf("\n The reverse of the digits = %d", reverse);
printf("\n The product of %d * %d = %d", digitSum, reverse, reverse * digitSum);
if (reverse * digitSum == num)
{
printf("\n %d is a Magic Number. ", num);
}
else
{
printf("\n %d is not a Magic Number. ", num);
}
return 0;
}
