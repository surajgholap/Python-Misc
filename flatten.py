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


if __name__ == "__main__":
    lis = [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]
    flat_arr = flatten(lis)
    gen_arr = DataIterator(lis)
    print(gen_arr.next())
    # print(gen_arr.has_next())
    print(gen_arr.next())
    # print(gen_arr.has_next())
    print(gen_arr.next())
    print(gen_arr.next())
    print(gen_arr.next())
    print(gen_arr.next())
    print(gen_arr.next())
    print(gen_arr.next())
    print(flat_arr)
