#!/usr/bin/python3
''' method determines if given data set represents UTF-8 encoding '''


def validUTF8(data) -> bool:
    ''' returns bool '''
    remainingBytes = 0

    for num in data:
        if remainingBytes == 0:
            if num >> 7 == 0b0:
                continue
            elif num >> 5 == 0b110:
                remainingBytes = 1
            elif num >> 4 == 0b1110:
                remainingBytes = 2
            elif num >> 3 == 0b11110:
                remainingBytes = 3
            else:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            remainingBytes -= 1

    return remainingBytes == 0
