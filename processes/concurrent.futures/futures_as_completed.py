# File: futures_as_completed.py
#
# Invoking `result()` of a `Future` blocks until the task completes or is
# canceled. The results of the multiple tasks can be accessed as each task
# finishes or as they where scheduled.
from concurrent import futures
import random
import time

def task(n):
    time.sleep(random.random())
    return (n, n/10)


ex = futures.ThreadPoolExecutor(max_workers = 5)
print('main starting')

wait_for = [
    ex.submit(task, i) for i in range(5, 0, -1)
]

for f in futures.as_completed(wait_for):
    print('main: result: {}'.format(f.result()))
