import os

from lib.maximum_total import find_maximum_total


def get_problem67():
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/data/problem67.txt', 'r') as reader:
        return find_maximum_total([[int(v) for v in line.split(" ")] for line in reader.readlines()])
