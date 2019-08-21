# File: asyncio_echo_server_coroutine.py
#
# Here is the echo server and client implemented with coroutines and the
# asyncio streams API. The examples operate at a lower abstraction level than
# the Protocol API.
import asyncio
import logging
import ssl
import sys

SERVER_ADDRESS = ('localhost', 11111)

# The server defines a coroutine to handle communication. Each time a client
# connects, a new instance of the coroutine is invoked.
async def echo(reader, writer):
    address = writer.get_extra_info('peername')
    log = logging.getLogger('echo_{}_{}'.format(*address))
    log.debug('connection accepted')

# To avoid blocking while reading., the coroutine uses await with the
# read() call to allow the event loop to carry on processing other tasks.
    while True:
        data = await reader.read(128)
        terminate = data.endswith(b'\x00')
        date = data.rstrip(b'\x00')
        if data:
            log.debug('received {!r}'.format(data))
            writer.write(data)
            await writer.drain()
            log.debug('sent {!r}'.format(data))
        else:
            # If the client has not sent any data, read() returns an empty byte string
            # to indicate that the connection is closed.
            log.debug('closing')
            writer.close()
            return

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')
event_loop = asyncio.get_event_loop()

# Create an SSLContext and pass the context to start_server()
# The certificate is created with mintest.com as hostname - disable hostname
# verification.
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.check_hostname = False
ssl_context.load_cert_chain('mintest.crt','mintest.key')

# Create the server and let the loop finish the coroutine before starting the
# real event loop.
factory = asyncio.start_server(echo, *SERVER_ADDRESS, ssl=ssl_context)

# Create the server and let the loop finish the coroutine before
# starting the real event loop.
factory = asyncio.start_server(echo, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug('starting up on {} port {}'.format(*SERVER_ADDRESS))

# The event loop needs to be executed to process events and handle client
# requests.
try:
    event_loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    log.debug('closing server')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('closing event loop')
    event_loop.close()
