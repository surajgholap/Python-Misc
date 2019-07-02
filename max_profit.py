def max_diff(nums):
    """
    Returns maximum difference between two elements and their index
    such that larger element appears after the smaller number in O(n^2)

    Arguments:
        nums {list[int]} -- list of elements
    """
    max_val = nums[1] - nums[0]
    buy, sell = 0, 1
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            val = nums[i] - nums[j]
            if val > max_val:
                max_val = val
                buy, sell = j, i
    return max_val, buy, sell


def max_diff2(nums):
    """
    Returns maximum difference between two elements and their index
    such that larger element appears after the smaller number in O(n)

    Arguments:
        nums {list[int]} -- list of elements
    """
    min_idx_val = nums[0]
    max_val = nums[1] - nums[0]
    buy, sell = 0, 1
    for i in range(len(nums)-1):
        val = nums[i] - min_idx_val
        if val > max_val:
            max_val = val
            sell = i
        if nums[i] < min_idx_val:
            min_idx_val = nums[i]
            buy = i
    return max_val, buy, sell


nums = [1, 322, 0, 55, 3, 6664, 64, 0]
max_pro, buy, sell = max_diff(nums)
print("Maximum profit should be {} for buy index {} and sell index {}".format(
    max_pro, buy, sell))
max_pro2, buy2, sell2 = max_diff2(nums)
print("Maximum profit should be {} for buy index {} and sell index {}".format(
    max_pro2, buy2, sell2))
