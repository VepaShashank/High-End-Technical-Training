# Fibonacci sequence
def f(n):
   if n <= 1:
       return n
   else:
       return(f(n-1) + f(n-2))
N=int(input("Enter the number:"))
if N <=0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(N):
       print(f(i))