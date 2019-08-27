# File: hashlib_md5.py
#
# Calculate teh MD5 hash - digest - for a block of data.
import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())
