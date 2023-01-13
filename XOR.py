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
    # Need to reverse the bytes so XOR goes from least to greatest, then reverse back.
    byte1 = byte1[::-1]
    byte2 = byte2[::-1]
    # The result of XOR will always be <= in length to the max. 
    m = max(len(byte1), len(byte2))
    new_byte = []
    # Operation
    for i in range(m):
        try:
            new_byte.append((int(byte1[i]) + int(byte2[i])) % 2)
        except IndexError:
            try:
                new_byte.append(int(byte1[i]))
            except IndexError:
                new_byte.append(int(byte2[i]))
    
    # Reverse back.
    new_byte = new_byte[::-1]
    # Note: new_byte may have leading zeros! This will eliminate leading zeros until
    # either a 1 is detected or we hit the very last bit, in which case we just return 0.
    counter = 0
    zero_bit = True
    L = len(new_byte) 
    while counter <= L - 2 and zero_bit:
        if new_byte[0] == 1:
            zero_bit = False
        else:
            new_byte.pop(0)
            counter += 1
    # Finally return a string.
    new_byte = [str(x) for x in new_byte]
    return ''.join(new_byte)

## Now define XOR arithmetic.
def XORa(x, y):
    return decimal(XOR(bitwise(x), bitwise(y)))

print(XORs('100101', '101010111'))
print(XORs('100101011', '101010111'))