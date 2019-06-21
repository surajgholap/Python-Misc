# Normal method


def squares(nums):
    """ Calculates squares of a list of numbers
    without using generators

    Arguments:
        nums {list[int]} -- numbers to calculate squares.
    """
    result = []
    for i in nums:
        result.append(i * i)
    return result


# Generator method
"""
- Generators do not hold the entire result in memory and
hence are good for performance/speed when it comes to large inputs.
- It yield one result at a time.
Advantages over list:
- More readable, less code
"""


def gen_squares(nums):
    """Calculates the squares using generator

    Arguments:
        nums {list[int]} -- numbers to calculate squares.
    """
    for i in nums:
        yield i * i


if __name__ == "__main__":
    my_nums = [3, 4, 2, 5, 2]
    print(squares(my_nums))

    gen_nums = gen_squares(my_nums)
    # print(next(gen_nums))
    # print(next(gen_nums))
    # print(next(gen_nums))
    # print(next(gen_nums))
    for nums in gen_nums:
        print(nums)

    # Generators using list comprehensions
    gen_compr = (i * i for i in my_nums)
    for nums in gen_compr:
        print(nums)
