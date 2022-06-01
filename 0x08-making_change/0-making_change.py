#!/usr/bin/python3
'''
making change
'''


def makeChange(coins, total):
    '''
    returns minimum number of coins
    to make total
    '''
    if total == 0:
        return 0
    if not coins or min(coins) > total:
        return -1
    num = 0
    coins.sort(reverse=True)
    i = 0
    while i < len(coins):
        if coins[i] <= total:
            num += total // coins[i]
            total = total % coins[i]
        i += 1
    if total == 0:
        return num
    else:
        return -1
