import threading

from pyDAQ.UniversalIO import UniversalIO
from test_jig_util.Lockable import Lockable, dont_lock
from lock_profiler import LockProfiler
import time
import sys

Lockable._Lockable__debug_level = Lockable._Lockable__DEBUG_TRACE
d = UniversalIO()
Lockable._Lockable__debug_level = 0
Lockable.clear_trace()

d["IO1"].mode = "op"
d["IO1"].mode = "ip"
d["IO1"].value = 1
e = time.perf_counter() + 1
# i = 0
# while time.perf_counter() < e:
#     # d.write("read adc108")
#     inp = d["I2C1"].read_reg_bit(112, 0, 5, 'B', tries=1)
#     i += 1
# t = time.perf_counter() - t
d["IO1"].mode = "op"
Lockable._Lockable__debug_level = Lockable._Lockable__DEBUG_TRACE

class Locker(Lockable):
    def __init__(self):
        super(Locker, self).__init__()
        pass

l = Locker()
e = threading.Event()
def f():
    e.wait()
    for _ in range(5):
        # print(f"{threading.get_ident()} w")
        with l.lock:
            # print(f"{threading.get_ident()} s")
            # print(threading.get_ident())
            time.sleep(0.1)
            # print(f"{threading.get_ident()} f")
        # d["IO1"].mode = "op"



ti = time.perf_counter()
ts = [threading.Thread(target=f) for _ in range(10)]
for t in ts:
    t.start()
e.set()
for t in ts:
    t.join()
print(time.perf_counter() - ti)
Lockable._Lockable__debug_level = 0
LockProfiler.dump_stats("output.json")
# print(i)
