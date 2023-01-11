from XOR import *

msg = 'attack at dawn'

cipher = '09e1c5f70a65ac519458e7e53f36'

ascii = []

def bit_string(byte):
    byte_len = len(byte)
    string = ''
    for i in range(byte_len):
        string += str(byte[i])
    # Because bitwise gives the binary in reverse order.
    return string[::-1]

for char in msg:
    ascii.append(bit_string(bitwise(ord(char))))

# cipher_char = [cipher[i] + cipher[i + 1] for i in range(len(cipher)//2)]

## This is an ascii conversion from rapidtables.com
dawn = ['01100100', '01100001', '01110111', '01101110']
dawn_cipher = ['00110110', '00111111', '1110101', '11100111']

# Update these lists to be compatible with the bitwise function
dawn = list(map(lambda strng: [int(x) for x in strng], dawn))
dawn_cipher = list(map(lambda strng: [int(x) for x in strng], dawn_cipher))

# Now get the key:
key = [XOR(x, y) for (x, y) in zip(dawn, dawn_cipher)]

# Convert back to string form for display. Have to reverse because they are
# already in the right order.

# key = list(map(lambda lst: bit_string(lst)[::-1], key))

# I hand-checked this, it appears to be working. 
# print(key)

## Now we want to do XOR(dusk, key).
# Again, rapidtables.com
dusk = ['01100100', '01110101', '01110011', '01101011']
# Convert to lists for function to work:
dusk = list(map(lambda strng: [int(x) for x in strng], dusk))

dusk_cipher = [XOR(x, y) for (x, y) in zip(dusk, key)]

# For display we'll convert back to string.
dusk_cipher = list(map(lambda lst: bit_string(lst)[::-1], dusk_cipher))
print(dusk_cipher)