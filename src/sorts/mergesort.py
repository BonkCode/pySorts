

def mergesort(arr: list):
    def msort(arr: list):
        if len(arr) > 1:
            m = len(arr) // 2
            L = arr[:m]
            R = arr[m:]
            msort(L)
            msort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    sortedArr = arr.copy()
    msort(sortedArr)
    return sortedArr
 

if __name__ == '__main__':
    pass
