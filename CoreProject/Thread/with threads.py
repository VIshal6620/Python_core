import threading


def hello():
    for i in range(1, 11):
        print('hello:', i)


def hi():
    for i in range(1, 11):
        print('hi:', i)


t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hi)

t1.start()
t2.start()