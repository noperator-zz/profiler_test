from test_jig_util.Lockable import Lockable, dont_lock
import timeit
import time


class Locker(Lockable):
    def __init__(self):
        super(Locker, self).__init__()
        pass

    # @dont_lock
    def test_func(self):
        time.sleep(0.001)
        return


def run_test(obj, num=100):
    def f(obj, num):
        func = obj.test_func
        for _ in range(num):
            func()

    duration = timeit.timeit(lambda: f(obj, num), number=1)
    return num / duration


def main():
    lockable: Lockable = Locker()

    # When running from pycharm, uncomment this line to let the CPU usage go down after starting the process
    # time.sleep(5)

    print(f"{run_test(lockable)}")
    print(f"{run_test(lockable)}")
    print(f"{run_test(lockable)}")
    print(f"{run_test(lockable)}")



# Performance:
#  No Tracing                                          : 300000
#  __DEBUG_TRACE                                       : 16000
#  __DEBUG_TRACE | __DEBUG_TRACE_STACK (all frames)    : 1100

# Lockable._Lockable__debug_level = Lockable._Lockable__DEBUG_TRACE
if __name__ == "__main__":
    main()
    # Lockable.generate_html("output.html")
