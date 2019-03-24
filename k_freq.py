def k_freq(d, k):
    "Returns kth freq elements"
    res = []
    try:
        for i in range(k):
            res.append(d[i][0])
        return res
    except:
        return "K out of range"

if __name__ == "__main__":
    lis = [4, 4, 4, 4, 4, 5]
    dic = {}
    for i in lis:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    new = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(k_freq(new, 3))
