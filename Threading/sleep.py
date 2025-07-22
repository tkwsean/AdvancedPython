from threading import Thread
import threading
from time import sleep


def NaturalNo():
    print(threading.current_thread().getName(), "Has Started")
    sleep(10)
    for x in range(10):
        print(x)
    print(threading.current_thread().getName(), "Has Ended")


t1 = Thread(target=NaturalNo)
t2 = Thread(target=NaturalNo)
t1.start()
t2.start()
