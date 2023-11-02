#!/usr/bin/python3

'''
The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem.
'''

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_queens = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_queens < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(n):
    '''
    Function
    '''
    if n == 0:
        return [[]]

    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)] for i in range(n_queens)
            for solution in inner_solution if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    '''
    Function
    '''
    (row1, col1) = square
    (row2, col2) = queen

    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    '''
    Function
    '''
    for queen in queens:
        if attack_queen(sqr, queen):
            return False

    return True


for answer in reversed(solve_nqueens(n_queens)):
    result = []

    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])

    print(result)
