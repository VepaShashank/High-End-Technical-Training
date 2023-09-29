def toh(n,source,auxilary,destination):
    if n==0:
        return
    toh(n-1,source,destination,auxilary)
    print("Disk ",n," Moved from ",source,"to ",destination)
    toh(n-1,auxilary,source,destination)
n=int(input())
source,auxilary,destination=input().split()
toh(n,source,auxilary,destination)
    