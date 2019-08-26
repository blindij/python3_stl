# File: asyncio_call_at.py
#
# Asyncio example showing how to schedule a callback at
# a specific time.
#
# The loop for this purpose relies on a monotonic clock,
# rather than a wall-time clock, to ensure that the 
# value of "now" never regresses. It is necessary to start
# from the internal state of that clock using the loop's
# time() method
#
# If asyncio.sleep() has a sleep interval shorter that the
# aggregated added time, the latest scheduled loops will
# not run. Experiment with the sleep setting to see the 
# effect.
import asyncio
import time

def callback(n, loop):
    print('callback {} invoked at {}'.format(n, loop.time()))


async def main(loop):
    now = loop.time()
    print('clock time: {}'.format(time.time()))
    print('loop time: {}'.format(now))

    print('registering callbacks')
    loop.call_at(now+3, callback, 1, loop)
    loop.call_at(now+1, callback, 2, loop)
    loop.call_soon(callback, 3, loop)

    await asyncio.sleep(5)


event_loop = asyncio.get_event_loop()
try:
    print('entering event_loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
