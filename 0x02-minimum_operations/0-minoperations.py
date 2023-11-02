#!/usr/bin/python3

'''
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
'''


def minOperations(n):
    '''
    Operations function
    '''
    if n <= 1:
        return 0

    for operation in range(2, n + 1):
        if n % operation == 0:
            return minOperations(int(n / operation)) + operation
