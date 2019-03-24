arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def bst(a, l, h, ele):
    mid = (h-l) // 2
    if h-l < 0:
        return False
    # print(mid)
    if a[mid] == ele:
        return mid
    elif a[mid] < ele:
        return bst(a[mid:], mid+1, len(a[mid:])-1, ele)
    elif a[mid] > ele:
        return bst(a[:mid], 0, mid-1, ele)


print(bst(arr, 0, len(arr)-1, 3))
# print(bst(arr, 0, len(arr)-1, 21))
print(bst(arr, 0, len(arr)-1, 8))
