def kangarooScore(words, syn, ant):
    syn_map = {}
    ant_map = {}
    for i in syn:
        a = i.split(":")
        syn_map[a[0]] = a[1].split(",")
    for i in ant:
        a = i.split(":")
        ant_map[a[0]] = a[1].split(",")
    count = 0
    for i in words:
        # print(i)
        if i in syn_map:
            for j in syn_map[i]:
                if check_in(i, j):
                    # print("h")
                    count += 1
        if i in ant_map:
            for j in ant_map[i]:
                if check_in(i, j):
                    # print("h")
                    count -= 1
    return count


def check_in(kan, joe):
    if len(kan) <= len(joe):
        # print("f")
        return False
    i, j = 0, 0
    while i < len(kan) and j < len(joe):
        if kan[i] == joe[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(joe) and joe not in kan:
        return True
    else:
        return False


s = ["encourage:urge,boost,inspire", "container:tin,can,bag,bottle",
     "lighted:lit", "illuminated:lit"]
a = ["encourage:discourage", "animosity:amity,like", "lighted:dark"]
words = ["illuminated", "animosity", "deoxyribonucleic",
         "container", "lit", "amity", "encourage", "lighted"]
print(kangarooScore(words, s, a))
