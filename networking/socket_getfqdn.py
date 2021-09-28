import socket

for host in ['pymotw.com']:
    print('{:>10}:{}'.format(host, socket.getfqdn(host)))
