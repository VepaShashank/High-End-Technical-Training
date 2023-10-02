def cse(*y):
    print("Hi",y)
def ece(*x):
    print("Hello",x)
ece('training')
cse(69)

def cse():
    print("Hi")
def ece(x=20,y=10):
    print("Hello",x+y)
ece(69,96)
