#include<stdio.h>
int fun(int x, int y)
{
    if (y == 0) return 0;
    return (x + fun(x, y - 1));
}
int fun2(int a, int b)
{
    if (b == 0) return 1;
    return (a * fun2(a, b - 1));
}
int main()
{
    int result = fun2(2,3);
    printf("Result: %d\n",result);
    return 0;
}
