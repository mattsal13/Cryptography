import os
from functions import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

## The first CBC ciphertext.
CBC_1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
## The AES algorithm only accepts <class 'bytes'>. Will get an error if trying to use hex. 
key = '140b41b22a29beb4061bda66b6747e14'
iv = CBC_1[:16] ## The first 16 bytes of the ciphertext. 

## Note that the length of CBC_1 is 128. Now the IV is padded on to the beginning, and is 16 characters long.
# print(f'len(CBC_1) == {len(CBC_1)} and IV == {iv}')

'''
The formula for decryption is m_i = c_i XOR D(c_(i+1)). The length of CBC_1 is 128 characters, which represents 8 * 128 = 1024 bytes.
We have to partition the message into 128 byte pieces for AES decryption. 
'''

## A dictionary containing the CT pieces. Note that 8 * 16 = 128.
cipher_dict = dict()
# In reverse.
for i in range(8)[::-1]:
    cipher_dict[f'{i}'] = CBC_1[16*i :16*(i + 1)]

## Before decrypting the blocks we'll need to know how to XOR these b'hex' strings.
int_value = int.from_bytes(b'4ca00ff4c898d61e', "big")

def bytes_to_int(bytes):
    return int.from_bytes(bytes, "big")

## The bytes class if formatted like b'\x00\x05'. To convert back to bytes, we define
def int_to_bytes(int_val):
    return int_val.to_bytes(2, 'big')

## Almost ready to unwrap the message. I can't find anything that inverts AES...

## 256 is in BITS, which is 32 BYTES
cipher = Cipher(algorithms.AES256(key), modes.CBC(iv))

ct = CBC_1[16:] # has hex-length 112 = 16 * 8. 
decryptor = cipher.decryptor()

## Writes the message in hexadecimal.
mes = decryptor.update(ct)
mes_decoded = mes.decode('utf_16')
print(f"First message decoded: {mes_decoded}")

'''The second CBC code (same key)'''

# cbc_2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.encode('utf_8')

# key = '140b41b22a29beb4061bda66b6747e14'.encode('utf_8')
# iv = cbc_2[:16]
# print(iv)
# # ## Initialize an instance of the Cipher class.
# cipher2 = Cipher(algorithms.AES(key), modes.CBC(iv))

# ct2 = cbc_2[16:]
# decrypt = cipher2.decryptor()

# mes = decryptor.update(ct2)
# print(f'Decrypted message: {mes}')
# mes_decoded2 = mes.decode('utf_8')
# print(mes_decoded2)

something = os.urandom(16)

print(something)
int_val = (int.from_bytes(something, 'big'))
print(hex(int_val))