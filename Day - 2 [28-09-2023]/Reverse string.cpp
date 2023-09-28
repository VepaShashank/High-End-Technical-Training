#include <stdio.h>
#include <string.h>
#include <ctype.h>
void revstr(char *str1)
{
    int left = 0, right = strlen(str1) - 1;
    while (left < right)
    {
        while (!isalpha(str1[left]) && left < right)
            left++;
        while (!isalpha(str1[right]) && left < right)
            right--;
        if (isalpha(str1[left]) && isalpha(str1[right]))
        {
            char temp = str1[left];
            str1[left] = str1[right];
            str1[right] = temp;
        }
        left++;
        right--;
    }
}
int main()
{
    char str[50];
    printf("Enter the string: ");
    gets(str);
    revstr(str);
    printf("reverse of the given string: %s\n", str);
    return 0;
}
