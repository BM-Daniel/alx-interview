#!/usr/bin/python3

"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Pascal triangle function implemented
    """

    if n <= 0:
        return []

    result = [[1]]
    for row in range(1, n):
        rowArray = [1]

        for value in range(1, row):
            binomial = result[row - 1][value - 1] + result[row - 1][value]
            rowArray.append(binomial)
        rowArray.append(1)

        result.append(rowArray)

    return result
