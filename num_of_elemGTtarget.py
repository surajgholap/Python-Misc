# Given a sorted list of numbers and a target Z,
# return the number of pairs according to following definition: (X,Y) where X+Y >= Z


def num_of_elems(nums, target):
    l = 0
    r = len(nums)-1
    count = 0
    while l < r:
        # print(l, r)
        if nums[l] + nums[r] >= target:
            count += r-l
            r -= 1
        else:
            l += 1
    return count


arr = [1, 3, 7, 9, 10, 11]
Z = 7
print(num_of_elems(arr, Z))
