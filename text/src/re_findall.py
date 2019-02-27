import re

text  = 'abxzzabxxxzzzz'
text2 = 'abbaaabbbbaaaa'

pattern = 'ab'

for match in re.findall(pattern,text):
    print('Found {!r}'.format(match))
