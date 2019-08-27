# File: hashlib_sha1.py
# 
# Calculate the SHA1 digest
import hashlib

from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())
