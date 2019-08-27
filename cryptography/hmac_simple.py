# File: hmac_simple.py
#
# HMAC algorithm is used for verifying the integrity of information passed 
# between applications. Here `new()` is used for calculating a message
# signature.
import hmac

digest_maker = hmac.new(b'secret-shared-key-goes-here')
with open('hashlib_data.py','rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)
