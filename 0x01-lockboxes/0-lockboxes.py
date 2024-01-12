#!/usr/bin/python3
"""This module defines the canUnlockAll function"""
from functools import reduce


def openBox(boxes, box, opened, count=1):
    """Uses the keys in box to open other boxes"""
    # Use keys in this box to recursively open other boxes
    to_open = []
    # Open all boxes and collect keys
    for i in boxes[box]:
        if i < len(boxes) and not opened[i]:
            to_open.extend(
                j for j in boxes[i] if j < len(boxes) and not opened[i])
            opened[i] = True
            count += 1
    # Try to open all unopened boxes
    for j in to_open:
        if not opened[j]:
            opened[j] = True
            count += 1
    # Check if all boxes are opened
    if count == len(boxes):
        return True
    for j in to_open:
        if openBox(boxes, j, opened, count):
            return True
    return False


def canUnlockAll(boxes):
    """Determines if all boxes can be opened"""
    if not boxes:
        return True
    # List to keep track of opened boxes. The first one is always open
    opened = [True] + [False] * (len(boxes) - 1)
    openBox(boxes, 0, opened)
    return reduce(lambda b1, b2: b1 and b2, opened, True)
