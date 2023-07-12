#!/usr/bin/python3
"""
    Method that calculates the fewest number of operations needed,
    to result in exactly n H characters in the file.
"""

def minOperations(n):
    """ 
        Calculates the fewest number of operations needed
        to result in exactly n H characters in the file

        Args:
            n: repetitions of H

        Returns:
            number of operations (Copy & Paste) to reach n Hs
    """
    operations = 0
    summation = 1
    carrier = 0

    while summation != n:
        if n % summation == 0:
            carrier = summation
            summation *= 2
        else:
            summation += summation
        operations += 1

    return operations
