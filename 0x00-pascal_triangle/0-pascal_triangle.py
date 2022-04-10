#!/usr/bin/python3
'''
returns a list of pascals series
'''


def factorial(n):
    if(n <= 1):
        return 1
    return n * factorial(n - 1)


def pascal_triangle(n):
    '''
    returns a list of pascal series
    '''
    result = []
    for i in range(n):
        res = []
        for j in range(i+1):
            res.append(factorial(i)//(factorial(j)*factorial(i-j)))

        result.append(res)

    return result


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
