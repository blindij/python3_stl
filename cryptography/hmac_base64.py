# File: hmac_base64.py
#
# Here `digest()` is used to produce a binary base64 digest
import base64
import hmac
import hashlib

with open('hashlib_data.py','rb') as f:
    body = f.read()

hash = hmac.new(
    b'secret-shared-key-goes-here',
    body,
    hashlib.sha256,
)

digest = hash.digest()
print(base64.encodestring(digest))
