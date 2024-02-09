import time
import logging
import timer

l = logging.getLogger()
logging.basicConfig(level=logging.INFO)

with timer.Timer(l):
    time.sleep(2)
now = time.time()
perf_timer = timer.Timer(l, max_frequency=1)

with perf_timer:
    print('Hello!')
with perf_timer:
    print('Hello again!')
