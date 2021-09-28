import socket

HOSTS = [
    'Bjrns-MBP-2',
    'pymotw.com',
    'www.python.org',
    'nosuchname',
]

for host in HOSTS:
    try:
        print('{}:{}'.format(host,socket.gethostbyname(host)))
    except socket.error as msg:
        print('{}:{}'.format(host, msg))
