# File: asyncio_client_coroutine.py
#
# The echo client using coroutine and the asyncio API streams for
# communication.
import asyncio
import logging
import ssl
import sys
MESSAGES = [
    b'This is the message. ',
    b'It will be sent ',
    b'in parts.',
]

SERVER_ADDRESS = ('localhost', 11111)

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(name)s: %(message)s',
    stream = sys.stderr,
)

log = logging.getLogger('main')
event_loop = asyncio.get_event_loop()

async def echo_client(server_address, messages):
    log = logging.getLogger('echo_client')
    log.debug('connecting to {} port {}'.format(*server_address))
# The certificate is created with mintest.com as the hostname. This name will
    # not match when the example code is executed elsewhere, so disable
    # hostname verification
    ssl_context = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH,
    )
    ssl_context.check_hostname = False
    ssl_context.load_verify_locations('mintest.crt')
    reader, writer = await asyncio.open_connection(
        *server_address, ssl=ssl_context)

    for msg in messages:
        writer.write(msg)
        log.debug('sending {!r}'.format(msg))
    # SSL does not support EOF, so send a null byte to indicate end of the
    # message
    writer.write(b'\x00')
    await writer.drain()
    log.debug('waiting for response')
    while True:
        data = await reader.read(128)
        if data:
            log.debug('received {!r}'.format(data))
        else:
            log.debug('closing')
            writer.close()
            return

try:
    event_loop.run_until_complete(
        echo_client(SERVER_ADDRESS, MESSAGES)
    )
finally:
    log.debug('closing event loop')
    event_loop.close()

