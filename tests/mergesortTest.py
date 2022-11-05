import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.sort import Sort

def main():
    raise NotImplementedError()


def testMergeSort(array):
    assert sorted(array) == Sort.mergesort(array)


if __name__ == '__main__':
    main()
