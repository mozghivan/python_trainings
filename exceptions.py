class TheNumberIs12(Exception):
    pass

def func(a, b):
    if(a == 12 or b == 12):
        raise TheNumberIs12
    else: 
        return a + b

try:
    func(1,12)
except TheNumberIs12:
    print("shit!")