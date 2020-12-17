def make_map(nums):
    mao = {}
    for i in nums:
        try:
            mao[i] += 1
        except KeyError:
            mao[i] = 1
    return mao


nums = [1, 2, 3, 2, 4, 3, 7, 5, 6, 8, 6]
print(make_map(nums))
