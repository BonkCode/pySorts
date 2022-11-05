from .sorts.insertsort import insertsort
from .sorts.mergesort import mergesort
from .sorts.quicksort import quicksort
from .sorts.randquicksort import randquicksort

class Sort():
    @staticmethod
    def insertsort(arr):
        return insertsort(arr)

    @staticmethod
    def mergesort(arr):
        return mergesort(arr)

    @staticmethod
    def quicksort(arr):
        return quicksort(arr)

    @staticmethod
    def randquicksort(arr):
        return randquicksort(arr)
