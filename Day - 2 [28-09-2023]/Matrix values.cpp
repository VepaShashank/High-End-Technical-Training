#include <stdio.h>
int main() {
    int r,c,i,j,matrix[10][10];
    printf("Enter the number of rows: ");
    scanf("%d",&r);
    printf("Enter the number of columns: ");
    scanf("%d",&c);
    printf("Enter the elements of the matrix:\n");
    for(i=0;i<r;i++) {
        for(j=0;j<c;j++){
            scanf("%d",&matrix[i][j]);
        }
    }
    printf("Matrix:\n");
    for(i=0;i<r;i++){
        for(j=0;j<c;j++){
            printf("%d  ",matrix[i][j]);
        }
        printf("\n");
    }
}
