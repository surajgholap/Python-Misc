def helper(num, arr):
    # if
    if arr[num] is not None:
        result = arr[num]
    if num == 0:
        result = 0
    elif num == 1 or num == 2:
        result = 1
    elif num == 3:
        result = 2
    else:
        result = helper(num-3, arr) + helper(num-1, arr)
    arr[num] = result
    return result


def sol(n):
    arr = [None]*(n+1)
    ans = helper(n, arr)
    return ans


print(sol(4))

print(sol(5))
print(sol(6))
