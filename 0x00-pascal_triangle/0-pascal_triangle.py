#!/usr/bin/python3
import math

"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Pascal triangle function implemented
    """
    result = []

    if n <= 0:
        return result

    for row in range(0, n):
        rowArray = []

        for value in range(0, row + 1):
            binomial = int(math.factorial(row) /
                           (math.factorial(value) *
                            math.factorial(row - value)))
            rowArray.append(binomial)

        result.append(rowArray)

    return result
