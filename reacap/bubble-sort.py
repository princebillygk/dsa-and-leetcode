arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("iteration: ", i,  " arr: ", arr)

print("result: ", arr)
