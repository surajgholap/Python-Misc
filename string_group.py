def string_group(s):
    mao = {}
    for i in s:
        if "".join(set(sorted(i.lower()))) in mao.keys():
            # print("".join(sorted(i.lower())))
            mao["".join(set(sorted(i.lower())))].append(i)
        else:
            mao["".join(set(sorted(i.lower())))] = [i]
    # print(mao)
    return list(mao.values())


s = ["Good", "pan", "nap", "dog", "god"]

print(string_group(s))
