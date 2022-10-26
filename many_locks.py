from test_jig_util.Lockable import Lockable
from lock_profiler import LockProfiler

Lockable._Lockable__debug_level = Lockable._Lockable__DEBUG_TRACE


class Locker(Lockable):
    _count = 0
    def __init__(self):
        super(Locker, self).__init__()
        self._c = Locker._count
        Locker._count += 1

    def __str__(self):
        return f"Locker_{self._c}"


locks = [Locker() for _ in range(3)]

def f():
    for l in locks:
        with l.lock:
            pass

f()

LockProfiler.dump_stats("output.json")
