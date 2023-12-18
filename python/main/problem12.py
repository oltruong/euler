import math


def get_problem12():
    return find_first_triangle_number_with_divisors(500)


def number_of_divisors(triangle_number):
    square = int(math.sqrt(triangle_number))

    counter = 2
    for i in range(2, square):
        if triangle_number % i == 0:
            counter += 2

    if square * square == triangle_number:
        counter += 1

    return counter

def find_first_triangle_number_with_divisors(min_number_of_divisors):
    triangle_number = 28
    next = 8

    while number_of_divisors(triangle_number) <= min_number_of_divisors:
        triangle_number += next
        next += 1

    return triangle_number
