def suicide_circle(n, k):
    """
    Return the index of the last person alive in a circular array.

    Arguments:
        n {int} -- num of persons
        k {int} -- person with index k dies
    """
    if n == 1:
        return 1
    else:
        return (suicide_circle(n-1, k) + k-1) % n+1


print(suicide_circle(5, 2))
print(suicide_circle(14, 2))
