# Given two positive integers n and k.
# A factor of an integer n is defined as an integer i where n % i == 0.
# Consider a list of all factors of n sorted in ascending order, return the
# kth factor in this list or return -1 if n has less than k factors.
# Example 1:
#
# Input: n = 12, k = 3
# Output: 3
# Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
#  Example 2:
# bs =[1,2,3]
# as =[12,6,4] --> bs + as[::-1]
# Input: n = 7, k = 2
# Output: 7
# Explanation: Factors list is [1, 7], the 2nd factor is 7.
# Example 3:
#
# Input: n = 4, k = 4
# Output: -1
# Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should
# bs = [1,2]
# as = [4,]
# return -1.


def kth_factor(n, k):
    factors = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            factors.append(i)
    factors.append(n)

    if len(factors) < k:
        return -1
    else:
        return factors[k-1]


print(kth_factor(12, 3))
print(kth_factor(7, 2))
print(kth_factor(4, 4))
print(kth_factor(1, 1))
print(kth_factor(1000, 3))
