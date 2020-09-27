def occ_sort(s):
    mao = {}
    for i in s:
        if i not in mao:
            mao[i] = 1
        else:
            mao[i] += 1
    k = (sorted(mao.items(), key=lambda x: x[1], reverse=True))
    ans = ''
    for i in k:
        temp = ''
        temp += "".join([i[0] for _ in range(i[1])])
        ans += temp
    print(ans)
    # return "".join([i[0] for i in k])


print(occ_sort("bloomberg"))
