def distribute(n, k):
    """
    Function to distribute n number of items in k parts.

    Arguments:
        n {int} -- Total number of items
        parts {int} -- Number of parts in which to divide
    """

    l = range(n)
    new = []
    for i in range(k):
        new.append(list(l[i::k]))
    return new


print(distribute(10, 2))
print(distribute(10, 4))
print(distribute(10, 8))
