"""Define amazing number as: its value is less than or equal to its index.
Given a circular array, find the starting position, such that the total number
 of amazing numbers in the array is maximized.
Example 1: 0, 1, 2, 3
Ouptut: 0. When starting point at position 0, all the elements in the array
are equal to its index. So all the numbers are amazing number.
Example 2: 1, 0 , 0
Output: 1. When starting point at position 1, the array becomes 0, 0, 1.
All the elements are amazing number.
If there are multiple positions, return the smallest one.
"""


def amaze_check(arr, idx):
    "Calculates the number of amazing numbers in the arr starting from idx."
    new = arr + arr
    count = 0
    for i, j in zip(list(range(len(arr))), list(range(idx, idx+len(arr)))):
        if i >= new[j]:
            count += 1
    return count


if __name__ == "__main__":
    ser = [4, 0, 1, 2, -1]
    ans = 0
    res = 0
    ser_size = len(ser)
    for l in range(ser_size):
        temp = amaze_check(ser, l)
        # print(l, ans)
        # print(l, temp)
        if ans < temp:
            ans = temp
            res = l
    print(res)
