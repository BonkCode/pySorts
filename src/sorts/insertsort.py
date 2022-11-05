def insertsort(arr: list):
    sortedArr = arr.copy()
    for i in range(1, len(sortedArr)):
        key = sortedArr[i]

        j = i - 1
        while j >= 0 and key < sortedArr[j] :
                sortedArr[j + 1] = sortedArr[j]
                j -= 1
        sortedArr[j + 1] = key
    return sortedArr


def main():
    pass


if __name__ == '__main__':
    main()
