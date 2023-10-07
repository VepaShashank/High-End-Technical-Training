a=list(map(int,input().split()))
n=len(a)
res=[0*n for i in range(n)]
count=[0*10 for i in range(10)]
for i in a:
    count[i]+=1
for i in range(1,10):
    count[i]+=count[i-1]
print(count)
for i in range(n-1,-1,-1):
    count[a[i]]-=1
    res[count[a[i]]]=a[i]
print(res)