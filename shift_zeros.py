def shift(arr):
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == 0:
            arr[i:n-1] = arr[i+1:]
            arr[n-1] = 0
        else:
            i += 1
        if max(arr[i:]) == 0 and min(arr[i:]) == 0:
            break
        # print(arr)
    print(arr)


def shift2(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < n:
        arr[count] = 0
        count += 1
    print(arr)


a = [3, 4, 0, 1, 0, 4, 8]
shift(a)
shift2(a)
