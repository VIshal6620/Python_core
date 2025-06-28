import threading
def hello():
    for i in range(15):
        print("Hello",i)

def hi():
    for i in range(15):
        print("hi",i)

# create threads
hello_thread = threading.Thread(target=hello)
hi_thread = threading.Thread(target=hi)


#start threads
hello_thread.start()
hi_thread.start()


#Main thread continues without waiting for the other threads to complete
print("\nThreads started\n")