## This function will convert a decimal into a bitwise string
## and then perform XOR operation

def bitwise(n):
    bit_string = []
    remainder = n
    
    while remainder >= 1:
        # coefficient of 2**k
        new_bit = int(remainder % 2)
        bit_string.append(new_bit)

        # update
        remainder -= new_bit 
        remainder = int(remainder / 2)

    # Note! This is the reverse of the usual representation.
    return bit_string

## Go back to decimal representation.
def decimal(byte):
    byte_len = len(byte)
    n = 0

    for i in range(byte_len):
        n += byte[i] * 2**i

    return n
    
## defining XOR on a bit LIST
def XOR(byte1, byte2):
    m = max(len(byte1), len(byte2))
    new_byte = []
    for i in range(m):
        try:
            new_byte.append((byte1[i] + byte2[i]) % 2)
        except IndexError:
            try:
                new_byte.append(byte1[i])
            except IndexError:
                new_byte.append(byte2[i])
    
    return new_byte

# XOR on bit STRINGS. Returns a STRING.
def XORs(byte1, byte2):
    m = max(len(byte1), len(byte2))
    new_byte = []
    for i in range(m):
        try:
            new_byte.append((int(byte1[i]) + int(byte2[i])) % 2)
        except IndexError:
            try:
                new_byte.append(int(byte1[i]))
            except IndexError:
                new_byte.append(int(byte2[i]))
    
    return new_byte

example = XOR(bitwise(8), bitwise(25))

## Now define XOR arithmetic.
def XORa(x, y):
    return decimal(XOR(bitwise(x), bitwise(y)))

# Should return 17.
# print(XORa(8, 25))
# print(XORa(45, 45))
# print(XORa(8, 16))