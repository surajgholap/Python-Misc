def mov_average(st):
    """Function calculates the moving average.

    Arguments:
        st {array of numbers} -- stores numbers

    Returns:
        mumber -- moving average of all the numbers
    """
    return sum(st)/len(st)


if __name__ == "__main__":
    store = []
    while True:
        inp = float(input("Enter the number?"))
        store.append(inp)
        print(mov_average(store))
    else:
        print("Void")
