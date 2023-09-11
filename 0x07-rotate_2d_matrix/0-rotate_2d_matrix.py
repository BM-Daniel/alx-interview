#!/usr/bin/python3

'''
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
'''


def rotate_2d_matrix(matrix):
    '''Function to rotate the matrix'''
    rows = len(matrix)
    columns = len(matrix[0])

    '''For loop to find transpose of the matrix'''
    for i in range(rows):
        for j in range(i, columns):
            tempValue = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tempValue

    '''For loop to swap the digits in a row'''
    for i in range(rows):
        start = 0
        end = rows - 1

        while (start < end):
            tempValue = matrix[i][start]
            matrix[i][start] = matrix[i][end]
            matrix[i][end] = tempValue

            start += 1
            end -= 1
