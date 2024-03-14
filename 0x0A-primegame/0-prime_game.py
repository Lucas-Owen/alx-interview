#!/usr/bin/python3
"""This module defines the isWinner function"""


def isWinner(x, nums):
    """
    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 upto and including n, they take turns choosing a prime
    from the set and removing that number and its multiples from the set.
    The player that cannot make a move loses the game.
    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    this function returns who the winner of each game is
    """
    if type(nums) is not list:
        return None
    nums = [num for num in nums if type(num) is int]
    if x < 0 or nums is None or not nums:
        return None
    # True is Ben, False is Maria
    scores = {True: 0, False: 0, None: 0}
    rounds_played = 0
    while rounds_played < x:
        game_round = nums[rounds_played % len(nums)]
        round_winner = True
        sieve = [False] + [True] * (game_round-1)
        j = 1
        while j < game_round:
            round_winner = not round_winner
            for multiple in range(j+1, game_round+1, j+1):
                sieve[multiple-1] = False
            while j < game_round and not sieve[j]:
                j += 1
        scores[round_winner] += 1
        rounds_played += 1
    if scores[True] == scores[False]:
        return None
    return 'Ben' if scores[True] > scores[False] else 'Maria'
