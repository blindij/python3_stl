import socket

hostname, aliases, addresses = socket.gethostbyaddr('10.24.59.12')
print('Hostname:', hostname)
print('Aliases:', aliases)
print('Addresses', addresses)
