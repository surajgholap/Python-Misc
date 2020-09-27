def meandering_array(arr):
    sorted_arr = sorted(arr)
    res = []
    i = 0
    while i < len(arr)/2:
        res.append(sorted_arr[-(i+1)])
        res.append(sorted_arr[i])
        i += 1
    return res[:len(sorted_arr)]


a = [5, 2, 7, 8, -2, 25, 25]
print(meandering_array(a))
