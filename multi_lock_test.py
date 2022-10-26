import threading
from test_jig_util.Lockable import Lockable
from lock_profiler import LockProfiler
import time


class Locker(Lockable):
    _count = 0
    def __init__(self):
        super(Locker, self).__init__()
        self._c = Locker._count
        Locker._count += 1

    def __str__(self):
        return f"Locker_{self._c}"


l = Locker()
l2 = Locker()

def f():
    f2()

def f2():
    with l.lock:
        with l2.lock:
            pass

Lockable._Lockable__debug_level = Lockable._Lockable__DEBUG_TRACE
for _ in range(100):
    f()

LockProfiler.dump_stats("output.json")
# LockProfiler._dump_stats_for_pycharm()
