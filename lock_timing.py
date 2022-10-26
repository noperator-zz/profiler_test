from test_jig_util.Lockable import Lockable
from lock_profiler import LockProfiler
import time
import threading

Lockable._Lockable__debug_level = Lockable._Lockable__DEBUG_TRACE

class Locker(Lockable):
    def __init__(self):
        super(Locker, self).__init__()
        pass

l = Locker()
e = threading.Event()
e2 = threading.Event()

def f():
    with l.lock:
        with l.lock:
            time.sleep(0.1)

def f2():
    with l.lock:
        time.sleep(0.5)

t = threading.Thread(target=f2)
t.start()

with l.lock:
#     e.set()
#     e2.wait()
    time.sleep(0.1)
    f()

t.join()

LockProfiler.dump_stats("output.json")
# LockProfiler._dump_stats_for_pycharm()
