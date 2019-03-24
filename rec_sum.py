def rec_sum(arr, t):
    if arr:
        t = arr[0] + rec_sum(arr[1:], t)
    return t


def rec_helper(arr):
    total = 0
    return rec_sum(arr, total)

if __name__ == "__main__":
    print(rec_helper([1, 3, 4, 5]))
