a=92
print(chr(a))

b=input()
print(ord(b)-64)

c=input()
print(ord(c)-96)

d=input()
if(ord(d)>96):
    print(ord(d)-96)
else:
    print(ord(d)-64)
    
e=input()
e1=int(input())
print(chr(ord(e)+e1))