#!/usr/bin/python3
"""This module defines the validUTF8 function"""


def validUTF8(data):
    """
    Checks if a sequence of bytes is valid utf8 encoding
    args:
        data: list(int) list of integers representing a sequence of bytes
    """
    data_iter = iter(data)
    try:
        while True:
            byte = next(data_iter)
            check_next = 0
            if byte >= 256 or byte < 0:
                return False
            if byte >> 7 == 0:
                check_next = 0
            elif byte >> 5 == 0b110:
                check_next = 1
            elif byte >> 4 == 0b1110:
                check_next = 2
            elif byte >> 3 == 0b11110:
                check_next = 3
            else:
                return False
            try:
                for _ in range(check_next):
                    byte = next(data_iter)
                    if byte >> 6 != 0b10:
                        return False
            except StopIteration:
                return False
    except StopIteration:
        return True
