import os

from lib.maximum_total import find_maximum_total


def get_problem18():
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/data/problem18.txt', 'r') as reader:
        return find_maximum_total([[int(v) for v in line.split(" ")] for line in reader.readlines()])
