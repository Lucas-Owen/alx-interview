#!/usr/bin/python3
"""This module defines the makeChange function"""


def makeChange(coins, total):
    """
    Given a list of coins of different values, returns the fewest
    number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    results = [total+1] * (total+1)
    results[0] = 0
    for i in range(1, len(results)):
        for coin in coins:
            prev = i - coin
            if prev >= 0:
                if results[prev] + 1 < results[i]:
                    results[i] = results[prev] + 1
    return results[total] if results[total] != total+1 else -1
