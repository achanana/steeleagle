import time
import logging
import timer

l = logging.getLogger()
logging.basicConfig(level=logging.INFO)

with timer.Timer(l):
    time.sleep(2)
