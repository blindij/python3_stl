# File: asyncio_create_task.py
#
# Example where tasks are created with create_task().
import asyncio

async def task_func():
    print('in task func')
    return 'the task_func result'

async def main(loop):
    print('in main loop: creating task')
    task = loop.create_task(task_func())
    print('in main loop: waiting for {!r}'.format(task))
    return_value = await task
    print('in main loop: task completed {!r}'.format(task))
    print('return value: {!r}'.format(return_value))

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
