def prod(arr1, arr2):
    "Returns product of product of all the nums in arr1 and arr2"
    res1, res2 = 1, 1
    for i in arr1:
        res1 *= i
    for i in arr2:
        res2 *= i
    return res1 * res2


def replace_pro(arr):
    "Replaces ith position with the product of other pos"
    new = [0] * len(arr)
    for i in range(len(arr)):
        new[i] = prod(arr[:i], arr[i+1:])
    return new

if __name__ == "__main__":
    a = [1, 2, 3]
    new = replace_pro(a)
    print(new)
