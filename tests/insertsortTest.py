import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.sort import Sort


def main():
    arrays =\
    [
        [12, 11, 13, 5, 6],
        [1, 1, 1, 1, 1, 1],
        [-1, -2, -3],
        [5],
        [1, 2, 3, 4, 5],
        [1000000, 10000001, 10],
    ]

    for array in arrays:
        try:
            testInsertionSort(array)
        except AssertionError as _ex:
            print(f"sort failed: \nmessage: {_ex}\narray: {array}")


def testInsertionSort(array):
    assert sorted(array) == Sort.insertsort(array)


if __name__ == '__main__':
    main()
