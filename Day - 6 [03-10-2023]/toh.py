def toh(n,source,auxilary,destination):
    if n>0:
        toh(n-1,source,destination,auxilary)
        print(source,"-->",destination)
        toh(n-1,auxilary,source,destination,)
n=int(input("Enter the number of disks:"))
source='A';auxilary='B';destination='C'
toh(n,source,auxilary,destination)
