# File: asyncio_echo_client.py
#
# An echo client based on asyncio
import asyncio
import functools
import logging
import sys

MESSAGES = [
    b'This is the message. ',
    b'It will be sent ',
    b'in parts. ',
]

SERVER_ADDRESS = ('localhost', 11111)
#SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
    level = logging.DEBUG,
    format='%(name)s %(message)s',
    stream=sys.stderr,
)

log = logging.getLogger('main')
event_loop = asyncio.get_event_loop()


# The client protocol class defines the same methods as the server.
# The class constructor have two arguments,  a list of the messages and
# a Future object.
class EchoClient(asyncio.Protocol):
    def __init__(self, messages, future):
        super().__init__()
        self.messages = messages
        self.log = logging.getLogger('EchoClient')
        self.f = future

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log.debug(
            'connecting to {} port {}'.format(*self.address)
        )

        # This could be transport.writelines() except that
        # would makt it harder to show each part of the message
        # being sent.
        for msg in self.messages:
            transport.write(msg)
            self.log.debug('sending {!r}'.format(msg))
        if transport.can_write_eof():
            transport.write_eof()

    # The response from the server is logged
    def data_received(self, data):
        self.log.debug('received {!r}'.format(data))

    # The local transport is closed upon receiving EOF or connection
    # closed from the server side.
    def eof_received(self):
        self.log.debug('received EOF')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)

    def connection_lost(self, exc):
        self.log.debug('server closed connection')
        self.transport.close()
        if not self.f.done():
            self.set_result(True)
        super().connection_lost(exc)


client_completed = asyncio.Future()
client_factory = functools.partial(
    EchoClient,
    messages = MESSAGES,
    future=client_completed,
)

factory_coroutine = event_loop.create_connection(
    client_factory,
    *SERVER_ADDRESS,
)

log.debug('waiting for client to complete')
try:
    event_loop.run_until_complete(factory_coroutine)
    event_loop.run_until_complete(client_completed)
finally:
    log.debug('closing event loop')
    event_loop.close()
