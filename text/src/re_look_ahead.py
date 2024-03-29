import re

address = re.compile(
'''
# A name is made up of letters, and may include "."
# for title abbreviations and middle initials.
((?P<name>
 ([\w.,]+\s+)*[\w.,]+
 )
 \s+
 ) # The name is no longer optional


# LOOKAHEAD
# Email addresses are wrapped in angle brackets, but only
# if both are present or neither is
(?=(<.*>$)    # Remainder wrapped in angle brackets
 |
 ([^<].*[^>]$) # Remainder *not* wrapped in angle brackets
 )

<? # Optional opening angle bracket

# The address itself: username@domain.tld
(?P<email>
 [\w\d.+-]+    # Username
 @
 ([\w\d.]+\.)+ # Domain name prefix
 (com|org|edu) # Limit the allowed to-level domains
 )

 >? # Optional closing angle bracket
 ''',
 re.VERBOSE)


candidates=[
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    u'First Last <first.last@example.com>',
    u'No brackets first.last@example.com>',
    u'First Last',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
    u'<first.last@example.com>',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('Name:', match.groupdict()['name'])
        print('Email:', match.groupdict()['email'])
    else:
        print('No match')
