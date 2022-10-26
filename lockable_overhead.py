import threading

from test_jig_util.Lockable import Lockable, dont_lock
import timeit
import time
import functools


def locker2(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper


class Normal:
    def __init__(self):
        super(Normal, self).__init__()
        pass

    def test_func(self):
        return


class Locker(Lockable):
    def __init__(self):
        super(Locker, self).__init__()
        pass

    # @dont_lock
    def test_func(self):
        return

    # def test_func2(self):
    #     with self.lock:
    #         pass


def run_test(obj, num=100000):
    def f(obj, num):
        func = obj.test_func
        # print(func.__name__)
        # try:
        #     print(func.__wrapped__.__name__)
        # except:
        #     print("no wrapper")
        for _ in range(num):
            func()

    duration = timeit.timeit(lambda: f(obj, num), number=1)
    return num / duration


def main():
    def run(a, b):
        Lockable._Lockable__debug_level = 0
        plain_calls = run_test(a)
        Lockable._Lockable__debug_level = Lockable._Lockable__DEBUG_TRACE
        lockable_calls = run_test(b)
        slowdown = plain_calls / lockable_calls
        print(f"{plain_calls:.0f} / {lockable_calls:.0f} = {slowdown:.3f}x slowdown")

    plain = Normal()
    lockable = Locker()

    # When running from pycharm, uncomment this line to let the CPU usage go down after starting the process
    # time.sleep(5)
    for _ in range(5):
        # run(plain, lockable)
        run(lockable, lockable)

    # with lockable.lock:
    #     print("with lock")
    #
    # with lockable.lock(1):
    #     print("with lock")
    #
    # with lockable.lock():
    #     print("with lock")


if __name__ == "__main__":
    main()

# 3x slowdown, 595ns per lock, 240K iterations
