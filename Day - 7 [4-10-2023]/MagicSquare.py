import numpy as np
n = int(input("Enter order of the matrix : "))
matrix = np.zeros((n,n),dtype=int)
n_square = n**2
magic_number = n_square * ( n_square + 1) 
magic_number = magic_number//(2 * n)
row = n //2
column = n-1
matrix[row][column] = 1

for i in range(2, n_square + 1):
    row = row -1
    column = column + 1
    if row == -1 and column == n:
        matrix[row+1][column-2] = i
        row = row+1
        column = column-2   
    elif row == -1 and column<= n -1:
        matrix[n -1][column] = i
        row = n-1
    elif column == n and row <= n -1:
        matrix[row][0] = i
        column = 0
    elif matrix[row][column] != 0:
        matrix[row+1][column - 2] = i
        column = column - 2
        row = row + 1 
    else: 
        matrix[row][column] = i
 
print(matrix)