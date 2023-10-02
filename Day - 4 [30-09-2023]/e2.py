a=int(input())
for i in range(a):
    for j in range(i+1):
        print(' ',end='')
    for k in range(a-i):
        print(' *',end=' ')
    print()

