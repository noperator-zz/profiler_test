from line_profiler_pycharm import profile, PyCharmLineProfiler
import threading
import time


@profile
def f1():
    for i in range(10):
        print("f1")
    # time.sleep(1)
    time.sleep(1)

@profile
def f2():
    t = threading.Thread(target=f1)
    t.start()
    t.join()
    print("done")

f2()

# print(PyCharmLineProfiler.get_instance().get_stats())
PyCharmLineProfiler.get_instance().print_stats()
