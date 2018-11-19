#! /usr/bin/env python
# -*- coding: utf-8 -*-


# T: an array containing the values of the coins
# L: integer wich is the total to give back
# Output: Minimal number of coins needed to make a total of L
def dynamicCoinChange(T, L):

    Opt = [0 for i in range(0, L + 1)]

    n = len(T)
    for i in range(1, L + 1):
        smallest = float("inf")
        for j in range(0, n):
            if (T[j] <= i):
                smallest = min(smallest, Opt[i - T[j]])
        Opt[i] = 1 + smallest
    return Opt[L]


# Coin change situations
problems = [
    # [[1, 5, 10, 20, 50, 100, 200],  10000000],
    [[1, 3, 4], 20],
    [[1, 2, 3], 9],
    [[1, 2, 3], 10],
    [[1, 5], 13923],
    [[7, 22, 71, 231], 753],
    [[3, 5, 12], 25],
    [[800], 800],
    [[2], 50000]
]

# Test Loop
for T, L in problems:
    S = dynamicCoinChange(T, L)
    print "dynamicCoinChange(T, L)"
    print "T =", T
    print "L =", L
    print "Answer =", S
