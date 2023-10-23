#!/usr/bin/python3

'''
Given a pile of coins of different values, determine the fewest number of coins
needed to meet a given amount total
'''


def makeChange(coins, total):
    '''
    Function to provide the change
    '''
    if total <= 0:
        return 0

    remaining = total
    count_coins = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)

    n = len(coins)
    while remaining > 0:
        if coin_index >= n:
            return -1

        if remaining - sorted_coins[coin_index] >= 0:
            remaining -= sorted_coins[coin_index]
            count_coins += 1
        else:
            coin_index += 1

    return count_coins
