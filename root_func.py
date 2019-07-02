def square_root(n):
    "Calculates square root. O(N**0.5)"

    if n < 0:
        raise ValueError("Square root of negative nums does not exist")
    elif n == 0 or n == 1:
        return n
    else:
        i, ans = 1, 1

        while ans <= n:
            i += 1
            ans = i * i
        return i-1


def square_root_bin(n):
    "Calculates root with help of binary search. O(log N)"
    if n < 0:
        raise ValueError("Square root of negative nums does not exist")
    elif n == 0 or n == 1:
        return n
    else:
        start, ans, stop = 1, 1, n

        while start <= stop:
            mid = start + (stop-start)//2
            if mid <= n / mid:
                start = mid + 1
                ans = mid
            else:
                stop = mid - 1
        return ans


if __name__ == "__main__":
    print(square_root(15))
    print(square_root_bin(15))
    print(root_try(15))
