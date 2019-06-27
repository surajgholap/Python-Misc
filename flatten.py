import collections


class DataIterator:
    def __init__(self, d):
        self.new = []
        self.__build(d)

    def __build(self, a):
        for i in a:
            if isinstance(i, list):
                self.__build(i)
            else:
                self.new.append(i)

    def next(self):
        "return the next element in the iterable."
        # try:
        #     return next(self.new)
        # except:
        #     pass
        try:
            return next(self.new)
        except StopIteration:
            return ("End of the iterable")
        except TypeError:
            self.new = iter(self.new)
            return next(self.new)

    def has_next(self):
        # TODO
        if not next(self.new):
            return False
        return True


def flatten(arr):
    "Returns flattened array."
    n = []
    helper(arr, n)
    return n


def helper(a, n):
    "Helper function for flatten."
    for i in a:
        if isinstance(i, list):
            helper(i, n)
        else:
            n.append(i)


def gene_flatten(arr):
    """ Return flattened generator object.

    Arguments:
        arr {list[*list]} -- contains list of lists to flatten
    """
    for i in arr:
        if isinstance(i, list):
            yield from gene_flatten(i)
        else:
            yield i


if __name__ == "__main__":
    lis = [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]
    print("Original list is {}".format(lis))
    flat_arr = flatten(lis)
    print(flat_arr)

    iter_arr = DataIterator(lis)
    # print(iter_arr.next())
    # print(iter_arr.has_next())
    # print(iter_arr.next())
    # print(iter_arr.has_next())
    print()
    gen_arr = gene_flatten(lis)
    print(next(gen_arr))
    print(next(gen_arr))
    print(next(gen_arr))
    print(next(gen_arr))
    print()
    for i in gen_arr:
        print(i)
