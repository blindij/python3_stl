# File: asyncio_coroutine.py
#
# This is an example of instantiating a coroutine
# Coroutine is a special function which give up
# control to the caller without losinig its state.
import asyncio

async def coroutine():
    print('in coroutine')

event_loop = asyncio.get_event_loop()

try:
    print('starting coroutine')
    coro = coroutine()
    print('entering event loop')
    event_loop.run_until_complete(coro)
finally:
    print('closing event loop')
    event_loop.close()
