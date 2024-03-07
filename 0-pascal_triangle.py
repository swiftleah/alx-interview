#!/usr/bin/python3
""" function pascal_triangle """

def pascal_triangle(n):
    """ Generates Pascal's triangle up to the nth row  with ints """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        next_row = [1]

        for j in range(1, i):
            next_row.append(prev_row[j - 1] + prev_row[j])
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
