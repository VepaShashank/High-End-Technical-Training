a=input()
b=int(input())
if((ord(a)+b)>122):
    print(chr(ord(a)+b)-26)
else:
    print(chr(ord(a)+b))
    
