from XOR import * 

PT = 'attack at dawn'
CT = '6c73d5240a948c86981bc294814d'

PT_ascii = [ord(char) for char in PT]
PT_ascii_bin = ["{0:08b}".format(int) for int in PT_ascii]

CT_chrs = [CT[i] + CT[i + 1] for i in range(len(CT) // 2)]
CT_chrs_bin = ["{0:08b}".format(int(chr, 16)) for chr in CT_chrs]

# print(PT_ascii)
# print()
# print(PT_ascii_bin)
# print()
# print(CT_chrs_bin)

## Now we XOR the PT and CT together to get the key. 

key_chrs = [XORs(x, y) for (x,y) in zip(PT_ascii_bin, CT_chrs_bin)]

print()
print(f'Key: {key_chrs}')
print()

## Now translate 'attack at dusk'. (check this by doing the last three letters by hand)

PT2 = 'attack at dusk'
PT2_ascii = [ord(chr) for chr in PT2]
PT2_bin = ["{0:08b}".format(int) for int in PT2_ascii]

CT2_bin = [XORs(x, y) for (x, y) in zip(key_chrs, PT2_bin)]
CT2_hex = [hex(int(byte, 2)).lstrip('0x') for byte in CT2_bin]

## These should only differ in the last 3 bytes (ie last 6 hex digits)
print('Attack at dawn: ' + '6c73d5240a948c86981bc294814d')
print()
print('Attack at dusk: ' + ''.join(CT2_hex))