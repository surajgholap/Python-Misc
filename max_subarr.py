def maxSubArray(nums) -> int:
    i = len(nums)
    ma = -1000
    while i >= 0:
        for j in range(0, i):
            an = sum(nums[j:i])
            print(i, j, an)
            if an > ma:
                ma = an
        i -= 1
    return ma


n = [-2, -1]
print(maxSubArray(n))
