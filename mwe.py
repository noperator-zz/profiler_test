from line_profiler_pycharm import profile
import threading
import time


@profile
def f1():
    print("f1")
    time.sleep(1)

@profile
def f2():
    t = threading.Thread(target=f1)
    t.start()
    t.join()
    print("done")

f2()
