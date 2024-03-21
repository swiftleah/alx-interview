#!/usr/bin/python3
''' method that calculates fewest number operations needed to do something
'''


def minOperations(n):
    ''' calculates the fewest number of operations needed to result
    in exactly n H characters in the file '''
    if not isinstance(n, int):
        return 0
    operationcount = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            operationcount += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            operationcount += 2
        elif clipboard > 0:
            done += clipboard
            operationcount += 1
    return operationcount
