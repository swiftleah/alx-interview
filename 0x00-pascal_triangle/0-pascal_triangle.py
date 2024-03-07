#!/usr/bin/python3
""" function pascal_triangle """

def pascal_triangle(n):
    """ function generates pascals triangle using ints to nth row """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        next_row = [1]

        for k in range(1, i):
            next_row.append(prev_row[k - 1] + prev_row[k])
        next_row.append(1)

        triangle.append(next_row)

    return triangle

def print_triangle(triangle):
    """ Print the Pascal's triangle """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
