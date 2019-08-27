# File: hmac_sha.py
#
# The HMAC module use MD5 as the default cryptographic algorithm. Here is how
# SHA1 can be used instead.
import hmac
import hashlib

digest_maker = hmac.new(b'secret-shared-key-goes-here',
                        b'',
                        'sha1'
)

with  open('hmac_sha.py','rb') as f:
    while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)
