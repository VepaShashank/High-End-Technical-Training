def cse(x):
    print("Hi")
    print(x)
    print(x-2)
def ece(x):
    print("Hello")
    cse(x+3)
    print(x)
ece(5)
cse(4)
print(2)