#!/usr/bin/python3
"""This is a script that solves the N-Queens Problem"""


from sys import argv


def markBoard(N, board, i, j):
    """Helper function to mark the board when a queen is placed"""
    board[i][j] = False
    for k in range(0, N):
        board[i][k] = False
        board[k][j] = False
        if i + k < N and j + k < N:
            board[i+k][j+k] = False
        if i + k < N and j - k >= 0:
            board[i+k][j-k] = False
        if i - k >= 0 and j + k < N:
            board[i-k][j+k] = False
        if i - k >= 0 and j - k >= 0:
            board[i-k][j-k] = False


def nQueens(N, board=None, path=None, i=0):
    """Recursive function to look for all solutions to a given N"""
    if path is None:
        path = list()
    if board is None:
        board = [[True]*N for _ in range(N)]
    if i == N:
        return True
    for j in range(N):
        if board[i][j]:
            path.append([i, j])
            board_copy = [x.copy() for x in board]
            markBoard(N, board_copy, i, j)
            if nQueens(N, board_copy, path, i+1):
                print(path)
            path.pop()
    return False


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    N = argv[1]
    if not N.isnumeric():
        print("N must be a number")
        exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    nQueens(N)
