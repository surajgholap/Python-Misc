def merge(arr1, arr2):
    "Merges two sorted array"
    count1 = 0
    count2 = 0
    res_arr = []
    while count1 < len(arr1) and count2 < len(arr2):
        if arr1[count1] <= arr2[count2]:
            res_arr.append(arr1[count1])
            count1 += 1
        else:
            res_arr.append(arr2[count2])
            count2 += 1
        # print(res_arr)
    while count1 < len(arr1):
        res_arr.append(arr1[count1])
        count1 += 1
    while count2 < len(arr2):
        res_arr.append(arr2[count2])
        count2 += 1
    return res_arr


def sort(arr):
    "Recursively sorts the array with the help of merge function"
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    print(left, right)
    return merge(left, right)


if __name__ == "__main__":
    print(sort([10, 3, 5, 7]))
