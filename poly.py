class Polynomial:
    """
    Represents polynomials functions
    """

    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        self._mao = {}
        for idx, val in enumerate(reversed(self.nums)):
            self._mao[idx] = val
        return " + ".join(reversed([str(v) if i == 0 else "{}x^{}".format(v, i)
                                    for i, v in self._mao.items()]))

    # def __repr__(self):
    #     return " + ".join(reversed([str(v) if i == 0 else "{}x^{}".format(v, i)
    #                                 for i, v in self._mao.items()]))


def add(*other):
    l = min([len(i) for i in other])
    print(l)


poly1 = Polynomial([2, 3, 4, 2])
poly2 = Polynomial([1, 2, 3])
print("Polynomial 1 is: {}".format(poly1))
print("Polynomial 2 is: {}".format(poly2))
# add(poly1, poly2)
print(repr(list(poly1)))


def maxProfit(costPerCut, salePrice, lengths):
    # Write your code here
    res = []
    print(lengths)
    min_size = min(lengths)
    for i in (min_size, 0, -1):
        for j in lengths:
            numR = j / i
            if type(numR) == float:
                numC = int(numR)
            else:
                numC = numR - 1
            numR = int(numR)

    print(min_size)


def calProfit(tUR, sL, sP, tC, cPC):
    return(tUR * sL * sP - tC * cPC)
