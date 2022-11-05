import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import insertsortTest, mergesortTest, quicksortTest, randquicksortTest


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ITest():
    @classmethod
    def run_test(self, arrs):
        pass


class TestMode():
    class All(ITest):
        @classmethod
        def run_test(self, arrs):
            TestMode.Insert.run_test(arrs)
            TestMode.Merge.run_test(arrs)
            TestMode.Quick.run_test(arrs)
            TestMode.Randquick.run_test(arrs)

    class Insert(ITest):
        @classmethod
        def run_test(self, arrs):
            print(f"{bcolors.OKCYAN}Insert Sort:{bcolors.ENDC}", end=" ")
            for arr in arrs:
                try:
                    insertsortTest.testInsertionSort(arr)
                    print(f"{bcolors.OKGREEN}OK{bcolors.ENDC}", end=" ")
                except AssertionError:
                    print(f"{bcolors.FAIL}ERR{bcolors.ENDC}", end=" ")
            print()

    class Merge(ITest):
        @classmethod
        def run_test(self, arrs):
            print(f"{bcolors.OKCYAN}Merge Sort:{bcolors.ENDC}", end=" ")
            for arr in arrs:
                try:
                    mergesortTest.testMergeSort(arr)
                    print(f"{bcolors.OKGREEN}OK{bcolors.ENDC}", end=" ")
                except AssertionError:
                    print(f"{bcolors.FAIL}ERR{bcolors.ENDC}", end=" ")
            print()

    class Quick(ITest):
        @classmethod
        def run_test(self, arrs):
            print(f"{bcolors.OKCYAN}Quick Sort:{bcolors.ENDC}", end=" ")
            for arr in arrs:
                try:
                    quicksortTest.testQuickSort(arr)
                    print(f"{bcolors.OKGREEN}OK{bcolors.ENDC}", end=" ")
                except AssertionError:
                    print(f"{bcolors.FAIL}ERR{bcolors.ENDC}", end=" ")
            print()

    class Randquick(ITest):
        @classmethod
        def run_test(self, arrs):
            print(f"{bcolors.OKCYAN}Randomized quick Sort:{bcolors.ENDC}", end=" ")
            for arr in arrs:
                try:
                    randquicksortTest.testRandQuickSort(arr)
                    print(f"{bcolors.OKGREEN}OK{bcolors.ENDC}", end=" ")
                except AssertionError:
                    print(f"{bcolors.FAIL}ERR{bcolors.ENDC}", end=" ")
            print()


class ArgumentError(Exception):
    def __str__(self) -> str:
        return "Error: Incorrect args"

def main():
    arrays =\
    [
        [12, 11, 13, 5, 6],
        [1, 1, 1, 1, 1, 1],
        [-1, -2, -3],
        [5],
        [1, 2, 3, 4, 5],
        [1000000, 10000001, 10],
        [],
        [0]
    ]
    testModes =\
    {
        'all': TestMode.All,
        'insert': TestMode.Insert,
        'merge': TestMode.Merge,
        'quick': TestMode.Quick,
        'randquick': TestMode.Randquick
    }

    testMode = TestMode.All
    if len(sys.argv) > 2:
        raise ArgumentError
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() not in testModes:
            raise ArgumentError
        testMode = testModes[sys.argv[1].lower()]
    testMode.run_test(arrays)


if __name__ == '__main__':
    main()