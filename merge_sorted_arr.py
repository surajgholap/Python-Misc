def sol(arr1, m, arr2, n):
    i = 0
    j = 0
    while j < n and i < m:
        if arr1[i] <= arr2[j]:
            i += 1
        else:
            arr1[i+1:] = arr1[i:-1]
            arr1[i] = arr2[j]
            i += 1
            j += 1
    print(i, j, arr1)
    if j < n:
        arr1[i+1:] = arr2[j:]
        # i += 1
        # j += 1
    return arr1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(sol(nums1, m, nums2, n))
