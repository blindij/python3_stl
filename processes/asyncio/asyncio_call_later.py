# File: asyncio_call_later.py
#
# Example using asyncio callback, where the callback is postponed
# until some time has passed
import asyncio

def callback(n):
    print('callback{} invoked'.format(n))

async def main(loop):
    print('registrering callbacks')
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)

    await asyncio.sleep(0.4)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
