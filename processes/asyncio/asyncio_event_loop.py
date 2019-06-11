# File: asyncio_future_event_loop.py
# 
# Example showing the use of a Future object.
# A Future is a the result of work that has not
# been completed yet. The event loop wathc for a
# Future object's state to indicate that it is done.
import asyncio

def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)

event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    print('scheduling mark done')
    event_loop.call_soon(mark_done, all_done, 'the result')
    print('entering event_loop')
    result = event_loop.run_until_complete(all_done)
    print('returned result: {!r}'.format(result))
finally:
    print('closing event loop')
    event_loop.close()

print('future result: {!r}'.format(all_done.result()))
