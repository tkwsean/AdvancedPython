from threading import Thread
import threading


class MyThread:
    def naturalNo(self):
        print("Thread name is:", threading.current_thread().name)
        if threading.current_thread() != threading.main_thread():
            for x in range(10):
                print(x)
        else:
            print("Hey this is not a new thread")


myobj = MyThread()
t = Thread(target=myobj.naturalNo)
t.start()
t.join()  # Optional: ensures main thread waits for output
