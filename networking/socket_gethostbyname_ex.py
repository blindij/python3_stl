import socket

HOSTS = [
    'Bjrns-MBP-2',
    'pymotw.com',
    'www.python.org',
    'nosuchname',
]

for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print('Hostname:', name)
        print('Aliases:', aliases)
        print('Addresses:', addresses)
    except socket.error as msg:
        print('ERROR:', msg)
    print()
