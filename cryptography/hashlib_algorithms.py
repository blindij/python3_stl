# File: hashlib_algorithms.py
#
# All cryptographic algorithms available with OpenSSL is provided by
# hashlib.
import hashlib

print('Guaranteed:\n{}\n'.format(', '.join(sorted(hashlib.algorithms_guaranteed))))
print('Available:\n{}'.format(', '.join(sorted(hashlib.algorithms_available))))
