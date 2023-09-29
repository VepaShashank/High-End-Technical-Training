# Factorial of a number
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)   
N=int(input("Enter the number to find factorial : "))
if(N<0):
    print('Enter a positive number!')
elif(N==0):
    print('fact of 0 is 1')
else:
    print('Factorial of', N ,'is' ,fact(N))