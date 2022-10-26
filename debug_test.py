# from queue import SimpleQueue
import time
#
#
# q = SimpleQueue()
#
# while 1:
#     q.put(1)
#     q.get()

from line_profiler_pycharm import *
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import threading


@profile
def f1():
    print("f")
    time.sleep(1)

@profile
def f2():
    print("f")

@profile
def f3():
    print("f")

@profile
def f4():
    print("f")

@profile
def f5():
    print("f")


def f6(): print("f")

def f7():
    print("f")
    time.sleep(1)
    return 5


@profile
def runner(f):
    val = None
    def func():
        nonlocal val
        print(threading.current_thread().name)
        val = f()

    t = threading.Thread(target=func, name=str(f))
    t.start()
    t.join()
    return val

f6 = profile(f6)
f7 = profile(f7)

    #     runner()                                   1112223334123123456789
@profile
def scheduler():
    funcs = [f1, f2, f3, f4, f5, f6, f7]
    futures = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for f in funcs:
        #     t = threading.Thread(target=lambda: runner(f))
        #     t.start()
        #     t.join()
            future = executor.submit(lambda: runner(f))
            futures.append(future)

        print("waiting...")
        done, undone = wait(futures, return_when=ALL_COMPLETED)
        print("ok...")
        print(done, undone)


t = threading.Thread(target=scheduler)
t.start()
t.join()
print("done")

# while 1:
#     PyCharmLineProfiler.get_instance().enable_by_count()
#     PyCharmLineProfiler.get_instance().disable_by_count()
#     q.put(1)
#     q.get()


# @profile
# def f3():
#     print("hello")
#
# @profile
# def f1():
#     # PyCharmLineProfiler.get_instance().enable()
#     print("f1")
#     f3()
#
# @profile
# def f2():
#     t = threading.Thread(target=f1)
#     t.start()
#     t.join()
#
# PyCharmLineProfiler.get_instance().enable_by_count()
# f2()
