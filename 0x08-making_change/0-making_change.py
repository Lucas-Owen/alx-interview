#!/usr/bin/python3
"""This is makeChange function"""


def makeChange(coins, total, memo=None):
    """
    Given a list of coins of different values, returns the fewest
    number of coins needed to meet a given amount total
    """
    if memo is None:
        coins = sorted(coins, reverse=True)
        memo = {coin: 1 for coin in coins}
    if total == 0:
        return 0
    if total in memo:
        return memo[total]
    if total < 0:
        return -1
    res = []
    for coin in coins:
        tmp = makeChange(coins, total - coin, memo) if coin > 0 else -1
        if tmp >= 0:
            res.append(tmp + 1)
    memo[total] = -1 if len(res) == 0 else min(res)
    return memo[total]
