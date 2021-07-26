import threading

def thread_func(word):
    print(word)

string = "some random text"
words = string.split()
for word in words:
    threading.Thread(target=thread_func, args=(word,)).start() #why immutable type should be passed in args?