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
    if x < 0 or nums is None or x >= len(nums):
        return None
    # True is Ben, False is Maria
    scores = {True: 0, False: 0, None: 0}
    for i in range(x):
        game_round = nums[i]
        round_winner = True
        sieve = list(range(2, game_round+1))
        while len(sieve) > 0:
            round_winner = not round_winner
            n = sieve[0]
            for multiple in range(n, game_round+1, n):
                try:
                    sieve.remove(multiple)
                except ValueError:
                    pass
        scores[round_winner] += 1
    if scores[True] == scores[False]:
        return None
    return 'Ben' if scores[True] > scores[False] else 'Maria'
