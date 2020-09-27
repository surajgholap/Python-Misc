def for_func(i, n, a):
    if i == n:
        return
    print(a[i])
    return for_func(i+1, n, a)


if __name__ == "__main__":
    arr = [2, 3, 5, 4, 4]
    for_func(0, len(arr), arr)
    # print(list(a))
