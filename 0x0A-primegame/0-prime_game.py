#!/usr/bin/python3

'''
Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 up to and including n, they take turns choosing a prime number from the
set and removing that number and its multiples from the set. The player that
cannot make a move loses the game.
'''


def isWinner(x, nums):
    '''
    Function for game
    '''
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    n = max(nums)
    primes = [True for _ in range(1, n+1, 1)]
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue

        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x), nums):
        count_primes = len(list(filter(lambda x: x, primes[0: n])))
        ben_wins += count_primes % 2 == 0
        maria_wins += count_primes % 2 == 1

        if ben_wins == maria_wins:
            return None

        return 'Ben' if ben_wins > maria_wins else 'Maria'
