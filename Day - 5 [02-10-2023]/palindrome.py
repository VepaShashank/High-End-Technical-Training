s=input()
i=0
j=len(s)-1
while(i<j):
    if s[i]!=s[j]:
        print("Not Palindrome")
        break
    i+=1
    j-=1
else:
    print("Palindrome")