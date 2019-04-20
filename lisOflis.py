class DataIterator:
    def __init__(self, d):
        self.iter = iter(d)

    def next(self):
        pass


def flatten(arr):
    "Returns flattened array."
    n = []
    helper(arr, n)
    return n


def helper(a, n):
    "Helper function for flatten."
    for i in a:
        if type(i) == list:
            helper(i, n)
        else:
            n.append(i)


if __name__ == "__main__":
    lis = [1, 2, [3, [4, 5]], 6]
    flat_arr = flatten(lis)
    print(flat_arr)
