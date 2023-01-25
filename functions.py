def hexor(hex1, hex2):
    ## Input should be entered with 0x prefix
    return "{0:02x}".format(hex1 ^ hex2)

def hex_to_ascii(hex):
    hex_chrs = [hex[i] + hex[i + 1] for i in range(0, len(hex), 2)]
    ascii_chrs = []

    for char in hex_chrs:
        ## This is specific to the xor assignment. Need to keep track of places where spaces xor each other out.
        if char == '00':
            ascii_chrs.append('0')
        else:
            try:
                ascii_chrs.append(bytearray.fromhex(char).decode())

            except UnicodeDecodeError:
                ascii_chrs.append('_')
    
    return ascii_chrs

# print(hexor(0x435adc, 0x3fac123))