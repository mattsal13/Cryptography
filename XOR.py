import codecs
import binascii
import random

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

# print(XORs('100101', '101010111'))
# print(XORs('100101011', '101010111'))

## Defining XOR when the messages are written in hexadecimal.

def XOR_hex(hex1, hex2):

    # Fill with zeroes so that they are the same length. 
    if len(hex1) > len(hex2):
        hex2 = hex2.zfill(len(hex1))
    elif len(hex1) < len(hex2):
        hex1 = hex1.zfill(len(hex2))

    # Separates the hex encoded message into bytes (2 hexadecimals) to prepare for ascii translation.
    # Note that the messages are allowed to have unequal lengths. 
    hex1_chrs = [hex1[i] + hex1[i + 1] for i in range(0, len(hex1), 2)]
    hex2_chrs = [hex2[i] + hex2[i + 1] for i in range(0, len(hex2), 2)]

    # Binary conversion.
    hex1_bin = ["{0:08b}".format(int(chr, 16)) for chr in hex1_chrs]
    hex2_bin = ["{0:08b}".format(int(chr, 16)) for chr in hex2_chrs]

    # XOR the two lists
    xor = [XORs(x, y) for (x, y) in zip(hex1_bin, hex2_bin)]

    # Convert back to hex. Make sure they are 2 characters each. Then put back together to get a string.
    xor_hex = [hex(int(bin_string, 2)).lstrip('0x').zfill(2) for bin_string in xor]
    xor_string = ''.join(xor_hex)

    return xor_string


def hex_to_ascii(hex):
    hex_chrs = [hex[i] + hex[i + 1] for i in range(0, len(hex), 2)]
    ascii_chrs = []

    for char in hex_chrs:
        try:
            ascii_chrs.append(bytearray.fromhex(char).decode())
        except UnicodeDecodeError:
            ascii_chrs.append('_')
    
    return ascii_chrs

def get_letter_index(lst):
    counter = 0
    M = len(lst)
    index_list = []
    while counter < M:
        if lst[counter].isalpha():
            index_list.append(counter)
            counter += 1
        else:
            counter += 1
    return index_list

