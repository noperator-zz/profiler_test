from line_profiler import show_text, load_stats

stats = load_stats("f.pickle")
show_text(stats.timings, stats.unit)
