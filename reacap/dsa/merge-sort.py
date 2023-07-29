l = [25, 21, 20, 9, 4, 3, 1]


def merge(l1, l2, l):
    i = j = 0
    while i + j < len(l):
        if j == len(l2) or (i < len(l1) and l1[i] < l2[j]):
            l[i + j] = l1[i]
            i += 1
        else:
            l[i + j] = l2[j]
            j += 1


def merge_sort(l):
    if len(l) < 2:
        return

    pivot = len(l) // 2
    l1 = l[:pivot]
    l2 = l[pivot:]

    print(l1, l2)
    merge_sort(l1)
    merge_sort(l2)
    print(l1, l2)

    merge(l1, l2, l)


print("Before sorted:", l)
merge_sort(l)
print("After sorted: ", l)
