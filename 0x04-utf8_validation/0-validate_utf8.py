#!/usr/bin/python3

'''
Write a method that determines if a given data set represents a valid UTF-8
encoding.
'''


def validUTF8(data):
    '''
    Validate function
    '''
    number_of_bytes = 0

    for byte in data:
        mask = 1 << 7

        if not number_of_bytes:
            while byte & mask:
                number_of_bytes += 1
                mask >>= 1

            if not number_of_bytes:
                continue

            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False

        number_of_bytes -= 1

    return number_of_bytes == 0
