from threading import Thread
import threading


def even_odd():
    evenNo()
    print(threading.current_thread().getName())
    oddNo()


def evenNo():
    for x in range(10):
        if x % 2 == 0:
            print(x)
    print(threading.current_thread().getName())


def oddNo():
    for x in range(10):
        if x % 2 != 0:
            print(x)
    print(threading.current_thread().getName())


t = Thread(target=even_odd, name="Even-Odd Thread")
t.start()
