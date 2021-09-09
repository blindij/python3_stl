# Use datetime class to hold values consisting of both dath and
# time components. As with date, several convenient class methods are 
# available for creating datetim instances from other common values
import datetime

print('Now   :', datetime.datetime.now())
print('Today :', datetime.datetime.today())
print('UTC Now:', datetime.datetime.utcnow())
print
FIELDS= [
    'year','month','day',
    'hour','minute','second',
    'microsecond',
]

d = datetime.datetime.now()
for attr in FIELDS:
    print('{:15}: {}'.format(attr, getattr(d,attr)))
