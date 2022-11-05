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
    def run_test(self, testDataArr: list[list], function: callable = None, message:str = f"{bcolors.OKCYAN}Test:{bcolors.ENDC}"):
        print(message, end=" ")
        for testData in testDataArr:
            try:
                function(testData)
                print(f"{bcolors.OKGREEN}OK{bcolors.ENDC}", end=" ")
            except AssertionError:
                print(f"{bcolors.FAIL}ERR{bcolors.ENDC}", end=" ")
        print()


class TestMode():
    class All(ITest):
        @classmethod
        def run_test(self, arrs, func=None, ):
            TestMode.Insert.run_test(arrs)
            TestMode.Merge.run_test(arrs)
            TestMode.Quick.run_test(arrs)
            TestMode.Randquick.run_test(arrs)

    class Insert(ITest):
        @classmethod
        def run_test(self, arrs):
            super().run_test(arrs, insertsortTest.testInsertionSort, f"{bcolors.OKCYAN}Insert Sort:{bcolors.ENDC}")

    class Merge(ITest):
        @classmethod
        def run_test(self, arrs):
            super().run_test(arrs, mergesortTest.testMergeSort, f"{bcolors.OKCYAN}Merge Sort:{bcolors.ENDC}")

    class Quick(ITest):
        @classmethod
        def run_test(self, arrs):
            super().run_test(arrs, quicksortTest.testQuickSort, f"{bcolors.OKCYAN}Quick Sort:{bcolors.ENDC}")

    class Randquick(ITest):
        @classmethod
        def run_test(self, arrs):
            super().run_test(arrs, randquicksortTest.testRandQuickSort, f"{bcolors.OKCYAN}Randomized quick Sort:{bcolors.ENDC}")


class ArgumentError(Exception):
    def __str__(self) -> str:
        return f"Error: Incorrect args: Expected arg count: 1; Expected argument list: {[i for i in testModes.keys()]}"


testModes =\
    {
        'all': TestMode.All,
        'insert': TestMode.Insert,
        'merge': TestMode.Merge,
        'quick': TestMode.Quick,
        'randquick': TestMode.Randquick
    }


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
        [0],
        [-1, -2, -3, 4, 5, 6],
        ['q', 'w', 'e'],
        [['e', 'e', 'eee'], ['q', 'q'], ['w']],
        [[], [], []],
        [[]],
        [[[[[]]]], []]
    ]

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