import threading
import time

l1 = []
lck1 = threading.Lock()

def f (a,b,l,v,lck):
    # with lck:
    time.sleep(5)
    l.append(v)
    print(a)
    return a + b

threading.Thread(target=f, args=(1,2,l1,1,lck1)).start()
threading.Thread(target=f, args=(2,3,l1,2,lck1)).start()
threading.Thread(target=f, args=(3,4,l1,3,lck1)).start()
print(l1)
print(f(4,5,l1,4,lck1))
print(l1)