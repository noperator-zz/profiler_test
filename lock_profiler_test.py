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

    def test_func(self):
        time.sleep(0.1)


class Locker2(Lockable):
    _count = 0
    def __init__(self, l: Locker):
        super(Locker2, self).__init__()
        self._c = Locker2._count
        Locker2._count += 1
        self.l = l

    def acquire_lock(self, timeout=None):
        self.l.acquire_lock(timeout)

    def release_lock(self):
        self.l.release_lock()

    def __str__(self):
        return f"Locker_{self._c}"

    def test_func(self):
        time.sleep(0.5)


_l = Locker()

l = Locker2(_l)
l2 = Locker2(_l)
num = 1
e = threading.Event()

Lockable._Lockable__debug_level = Lockable._Lockable__DEBUG_TRACE
# with l.lock:
#     pass
#
# with l.lock():
#     pass
#
# l.test_func()
#
# Lockable.print_stats()
# quit()

def f():
    e.wait()
    for _ in range(num):
        l.test_func()
        l2.test_func()


def f2():
    def sub():
        with l.lock():
            with l2.lock():
                time.sleep(0.1)


        _l.test_func()

    e.wait()
    for _ in range(num):
        sub()

t1 = threading.Thread(target=f)
t2 = threading.Thread(target=f2)
t1.start()
t2.start()
print("start")
time.sleep(0.01)
e.set()

t2.join()
t1.join()

LockProfiler.dump_stats("output.json")
