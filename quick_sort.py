def partition(l, h, a):
    "Returns partition in quick sort."
    pivot = a[h]
    i = l-1

    for j in range(l, h):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[h] = a[h], a[i+1]
    return i+1


def quicksort(l, h, a):
    "Quicksort implementation."
    if l < h:
        ind = partition(l, h, a)
        quicksort(l, ind-1, a)
        quicksort(ind+1, h, a)
    # return a

if __name__ == "__main__":
    arr = [3, 5, 1, 7, 8]
    n = len(arr)-1
    quicksort(0, n, arr)
    print(arr)
