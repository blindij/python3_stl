import re

address = re.compile(
'''
^
# An adress: username@domain.tld
# Ignore noreply addresses
(?!noreply@.*$)
[\w\d.+-]+    # Username
@
([\w\d.]+\.)+ # Domain name prefix
(com|org|edu) # Limit the allowed top-level domains.
$
''',
re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'noreply@example.com',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('  Match:', candidate[match.start():match.end()])
    else:
        print(' No match')
