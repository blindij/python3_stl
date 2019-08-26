# File: asyncio_echo_server_protocol.py
#
# This is an implementation of an simple echo server, using the
# concuurency concepts in asyncio. A client can connect to the server,
# send some data, and then receive the same data as a response. Each
# time an I/O operation is initiated, the executing code gives up
# control to the event loop, allowing other tasks to run until the I/O
# is ready.
import asyncio
import logging
import sys

SERVER_ADDRESS = ('localhost', 11111)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)

log = logging.getLogger('main')
event_loop = asyncio.get_event_loop()

# The server defines a subclass of asyncio.Protocol to handle client
# communication. The protocol object's methods are invoked by events
# associated with the server socket.
class EchoServer(asyncio.Protocol):

    # Each new client connection triggers a call to connection_made().
    # The transport argument is an instance of asyncio.Transport.
    # Asyncio.Transport provides an abstraction for doing asyncronous
    # I/O using socket.
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log = logging.getLogger(
            'EchoServer_{}_{}'.format(*self.address)
        )

    # When the connection is established, the client sends data. The
    # data_received() method is invoked as the server receives data. A
    # response is sent back to the client with transport.write()
    def data_received(self, data):
        self.log.debug('received {!r}'.format(data))
        self.transport.write(data)
        self.log.debug('sent {!r}'.format(data))

    
    # When and EOF is encountered, the eof_received() method is called.
    # The EOF is sent back to the client to indicate that it was
    # received. Not all transports support an EOF. The protocol asks
    # first whether it is safe to send EOF.
    def eof_received(self):
        self.log.debug('received EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()


    # The connection_lost() is called when a connection is closed,
    # either normally or as the result of an error. In the case of an
    # error, the argument holds an excepition object
    def connection_lost(self, error):
        if error:
            self.log.error('ERROR: {}'.format(error))
        else:
            self.log.debug('closing')
        super().connection_lost(error)

# Create the server  and let the loop finish  the coroutine before
# starting the real event loop
factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug('starting up on {} port {}'.format(*SERVER_ADDRESS))

# Run event_loop, enter the event loop permanently to handle all
# connections.
try:
    event_loop.run_forever()
finally:
    log.debug('closing server')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('closing event loop')
    event_loop.close()
