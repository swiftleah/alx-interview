#!/usr/bin/python3
""" function island_perimeter """


def island_perimeter(grid):
    """ function returns perimeter of island in grid
    represented by 1's """
    oneCount = 0

    for row in grid:
        for element in row:
            if element == 1:
                oneCount += 1

    if oneCount == 0:
        return 0

    if oneCount == 1:
        result = 4
    else:
        result = ((oneCount * 2) + 2)
    return result
