num = int(input("Enter a number \n"))
sqr = num*num 
sum = 0
while sqr>0:
    sum =sum + sqr%10
    sqr = sqr//10

if (num == sum):
    print("Neon Number \n")
else:
    print("Not a Neon Number \n")
