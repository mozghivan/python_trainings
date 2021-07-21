class User:
    a = 3
    b = [1]

    def __init__(self):
        self.c = []

    def printA(self):
        print(self.a)

user = User()
user1 = User()

user.a = 1          # immutable, user1.a value didn't change
user.b.append(2)    # mutable, user1.b values changed
user1.a = user.a        
print("user a  = ", user.a, "\t\t(immutable)") 
print("user b  = ", user.b, "\t(mutable)")
print("user1 a = ", user1.a, "\t\t(immutable)")
print("user1 b = ", user1.b, "\t(mutable)")

user.a = []
user1.a = []
user.a.append(3)    # mutable, but this didn't change user1.a value
user1.a.append(4)   # the same magic, why, how?
print("\nuser.a\t:", user.a, "\t(mutable)") 
print("user1.a\t:", user1.a, "\t(mutable)")