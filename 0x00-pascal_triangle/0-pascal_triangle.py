#!/usr/bin/python3
import math


def pascal_triangle(n):
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
