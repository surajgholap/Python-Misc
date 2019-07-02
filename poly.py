class Polynomial:
    """
    Represents polynomials functions
    """

    def __init__(self, nums):
        self._mao = {}
        self._nums = nums
        for idx, val in enumerate(reversed(self._nums)):
            self._mao[idx] = val

    def __str__(self):
        return " + ".join(reversed([str(v) if i == 0 else "{}x^{}".format(v, i)
                                    for i, v in self._mao.items()]))

    def __add__(self, *other):
        pass


poly1 = Polynomial([2, 3, 4, 2])
poly2 = Polynomial([1, 2, 3])
print("Polynomial 1 is: {}".format(poly1))
print("Polynomial 2 is: {}".format(poly2))
add(poly1, poly2)
