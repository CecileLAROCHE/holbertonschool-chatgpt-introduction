#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer for which to compute the factorial.

    Returns:
        int: The factorial of n. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)

