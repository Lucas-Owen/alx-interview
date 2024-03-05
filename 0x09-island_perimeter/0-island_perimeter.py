#!/usr/bin/python3
"""This module defines the island_perimeter function"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn't have “lakes” (water inside that isn't connected to
    the water surrounding the island)
    """
    # Count the number of zeros around each 1 (excluding diagonally)
    perimeter = 0
    rows = len(grid)
    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j]:
                if i-1 < 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i+1 >= rows or grid[i+1][j] == 0:
                    perimeter += 1
                if j-1 < 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j+1 >= cols or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter
