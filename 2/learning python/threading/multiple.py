import threading
import time

def thread_function(name):
    print(f"Thread {name}: starting")
    time.sleep(2)
    print(f"Thread {name}: finishing")


threads = list()
for index in range(3):
    print("Main    : create and start thread ", index)
    x = threading.Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    print("Main    : before joining thread ", index)
    thread.join()
    print(f"Main    : thread {index} done")
