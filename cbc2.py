import os
from functions import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

cbc = b'4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
key = b'140b41b22a29beb4061bda66b6747e14'

## QUESTION: do i need to reverse cbc?

## Encryption only takes in byte classes, so we need to convert these. Could probably just use b 'asdf' etc. Note that block size is 16 bytes. 
# cbc_bin = int(cbc, 16).to_bytes(len(cbc) // 2, byteorder='big')
# key_bin = int(key, 16).to_bytes(len(key) // 2, byteorder='big')


print(f'Number of bytes of cbc and the key, respectively: {len(cbc)} and {len(key)}.')

## AES encryption must take in a 16-byte IV:
iv = cbc[:16]

print(f'Number of bytes for the iv: {len(iv)}.')

# Create an instance of the Cipher class.
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

# The ciphertext to be decrypted will be cbc minus the first 16 bytes.
ct = cbc[16:]

# Note that block length is 16 bytes. If cipher length is a multiple of 16, need to add a dummy block.
print(f'Number of bytes of the ciphertext: {len(ct)}')

# This value is 112, which is a multiple of 16.

# So update this with a dummy block:
# if len(ct) % 16 == 0:
#     for _ in range(16):
#         ct = ct + b'\x10'

# Decryption
decrypt = cipher.decryptor()

mes = decrypt.update(ct) + decrypt.finalize()
print(mes)
# dec_mes = mes.decode('utf_8', errors='ignore')
# print(dec_mes)


'''Example to test that it's working.'''
## 'hello world' has length 11. So block size of 5?
# encryptor = cipher.encryptor()
# ct = encryptor.update(b"hello world" + b'\x05\x05\x05\x05\x05') + encryptor.finalize()

# decryptor = cipher.decryptor()
# mes = decryptor.update(ct) + decryptor.finalize()

# print(mes)