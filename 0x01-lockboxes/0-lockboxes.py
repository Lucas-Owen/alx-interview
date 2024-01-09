#!/usr/bin/python3
"""This module defines the canUnlockAll function"""
from functools import reduce


def openBox(boxes, box, opened):
    """Opens a box and uses the keys in that box to open other boxes"""
    # Open current box
    opened[box] = True
    # Use keys in this box to recursively open other boxes
    for i in boxes[box]:
        if i < len(boxes) and not opened[i]:
            openBox(boxes, i, opened)


def canUnlockAll(boxes):
    """Determines if all boxes can be opened"""
    if not boxes:
        return True
    # List to keep track of opened boxes. The first one is always open
    opened = [False] * len(boxes)
    openBox(boxes, 0, opened)
    return reduce(lambda b1, b2: b1 and b2, opened, True)
