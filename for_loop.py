from line_profiler_pycharm import profile, PyCharmLineProfiler
import time
#
# @profile
# def heavy():
#     time.sleep(1)
#     return 1, 2, 3

@profile
def f2():
    for i in range(10):
        1
    1

f2()

# PyCharmLineProfiler.get_instance().dump_stats("f.pickle")
# stats = PyCharmLineProfiler.get_instance().get_stats().timings
# print(list(stats.keys())[0])
# stats[1, 2, 3]
# for f, entries in stats.items():
#     print(f)
#     for i in entries:
#         print(f" {i}")
# PyCharmLineProfiler.get_instance().print_stats()
