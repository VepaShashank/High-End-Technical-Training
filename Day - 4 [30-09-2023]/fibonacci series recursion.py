def cse(x):
    if(x==0):
        return 0
    if(x==1):
        return 1
    if(x==2):
        return 1
    return cse(x-1) + cse(x-2)
for i in range(1,11):
    print(cse(i),end=" ")