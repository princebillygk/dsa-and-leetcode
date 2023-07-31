def quicksort(array):
    pivotIdx = len(array) - 1
    if (pivotIdx < 1):
        return array
    pivotVal = array[pivotIdx]

    i = 0
    while i < pivotIdx:
        if array[i] > pivotVal:
            array[pivotIdx] = array[i]
            pivotIdx -= 1
            array[i] = array[pivotIdx]
            array[pivotIdx] = pivotVal
        else:
            i += 1

    return quicksort(array[:pivotIdx]) + [pivotVal] + quicksort(array[pivotIdx + 1:])


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
