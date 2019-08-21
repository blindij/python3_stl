# File: ayncio_getaddrinfo.py
#
# Show the use of getaddrinfo() to convert a hostname and port number to
# an IP or IPv6 address. The return value is a list of tuples containing
# the address family, address type, protocol, the canonical name for the
# server, a socket address.
import asyncio
import logging
import socket
import sys


TARGETS = [
    ('pymotw.com','https'),
    ('doughellmann.com', 'https'),
    ('python.org', 'https'),
]


async def main(loop, targets):
    for target in targets:
        info = await loop.getaddrinfo(
            *target,
            proto=socket.IPPROTO_TCP,
        )

        for host in info:
            print('{:20}:{}'.format(target[0], host[4][0]))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, TARGETS))
finally:
    event_loop.close()
