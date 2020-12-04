#!/usr/bin/env python

""" Testing fibonacci Algorithms using recursive vs. DP """

from sys import setrecursionlimit
setrecursionlimit(10000000)

def fib_recursive(n):
    """ return the n th fibonacci number recursive """
    if n <= 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_memoization(n, memo):
    """ return n th using memoiztion """
    if n in memo:
        return memo[n]
    else:
        if n < 3:
            memo[n] = 1
            return 1
        else:
            fib = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
            memo[n] = fib
            return fib

def fib_bottom_up(n):
    """ the bottom up algorithm """
    fib_pp = 1
    fib_p  = 1
    fib_cur = 1

    for _ in range(3, n + 1):
        fib_cur = fib_pp + fib_p
        fib_pp = fib_p
        fib_p = fib_cur

    return fib_cur


def test():
    __name__ = "saleh"
    print(__name__)


def main():
    """main body"""

    print(">>> ", fib_recursive(20))

    memo = {}
    print(">>> ", fib_memoization(20000, memo))

    print(">>> ", fib_bottom_up(20000))


if __name__ == "__main__":
    import profile
    profile.run("main()")
