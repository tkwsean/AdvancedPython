from threading import Thread
import threading


class MyThread:
    def naturalNo(self):
        for x in range(10):
            print(x)


myobj = MyThread()
t = Thread(target=myobj.naturalNo())
t.start()
