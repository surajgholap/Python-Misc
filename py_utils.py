from functools import reduce

# map function
squares = map(lambda x: x**2, [1, 2, 3, 4])
print("Squares are {}".format(list(squares)))
num1 = [1, 2, 3]
num2 = [4, 5, 6]
print("Sum of 2 lists: {}".format(list(map(lambda x, y: x+y, num1, num2))))
# filter function
nums = [1, 2, 3, 4, 5, 6]
print("Even numbers are : {}".format(list(filter(lambda x: x % 2 == 0, nums))))
# reduce function
print("Greatest num is: {}".format(reduce(lambda a, b: a if (a > b)
                                          else b, nums)))
