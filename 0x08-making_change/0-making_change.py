#!/usr/bin/python3
"""Task 0"""


def makeChange(coins, total):
    ''' determines fewest number of coins needed to
    meet given total '''
    if total <= 0:
        return (0)

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] != float('inf'):
        return dp[total]
    else:
        return (-1)
