import sys

sys.stdout.flush()

from threading import Thread
import threading


def evenNumber():
    for x in range(20):
        if x % 2 == 0:
            print(x)
    print(threading.current_thread().name)


print("Main thread starting")
t = Thread(target=evenNumber)
t.start()
t.join()
print("Main thread ending")
