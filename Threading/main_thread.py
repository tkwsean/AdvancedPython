import threading

threading.current_thread().name = "Sean Thread"

if threading.current_thread() == threading.main_thread():
    for x in range(10):
        if x % 2 == 0:
            print(x)
else:
    print("The running thread is not a Main Thread")

print(threading.current_thread().getName())
