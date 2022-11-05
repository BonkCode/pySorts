def randquicksort(arr: list, low=-1, high=-1):
    from random import randint

    sortedArr = arr.copy()

    if low == -1:
        low = 0
    if high == -1:
        high = len(sortedArr) - 1

    def partition(array, low, high):
        pivotIndex = randint(low, high)
        array[pivotIndex], array[high] = array[high], array[pivotIndex]
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def randquickSort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            randquickSort(array, low, pi - 1)
            randquickSort(array, pi + 1, high)

    randquickSort(sortedArr, low, high)
    return sortedArr


def main():
    raise NotImplementedError()


if __name__ == '__main__':
    main()
