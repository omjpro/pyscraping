# threads_test.py
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s" % i)
print("Start")

thread = []

for i in range(5):
    t = threading.Thread(target=long_task)
    thread.append(t)

for t in thread:
    t.start()

for t in thread:
    t.join()

print("End")