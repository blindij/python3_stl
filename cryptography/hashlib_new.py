# File: hashlib_new.py
#
# Calculate a hash digest with the algorithm given in a string
import argparse
import hashlib
import sys

from hashlib_data import lorem

parser = argparse.ArgumentParser('hashlib demo')
parser.add_argument(
    'hash_name',
    choices=hashlib.algorithms_available,
    help='the name of the hash algorithms to use',
)

parser.add_argument(
    'data',
    nargs = '?',
    default = lorem,
    help = 'the input data to hash, defaults to lorem ipsum',
)

args = parser.parse_args()
h = hashlib.new(args.hash_name)
h.update(args.data.encode('utf-8'))
print(h.hexdigest())
