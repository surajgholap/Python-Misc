# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# Example 1 - Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


def sort_colors(nums):
    start = 0
    end = len(nums)-1
    i = 0
    while(i <= end):
        if nums[i] == 0:
            nums[i], nums[start] = nums[start], nums[i]
            start += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[end] = nums[end], nums[i]
            end -= 1
        else:
            i += 1
    return nums


print(sort_colors([1]))
print(sort_colors([2, 0, 1]))
