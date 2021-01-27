# Given a pattern as the first argument and a string of blobs split by |
# show the number of times the pattern is present in each blob and the
# total number of matches.


def count_func(s, ar):
    count = 0
    for i in range(0, len(s)-len(ar)+1):
        # print(s[i:i+len(ar)])
        if s[i:i+len(ar)] == ar:
            count += 1
    return str(count)


def pat_rec(s):
    arg = s.split(";")
    li = arg[1].split("|")
    res = []
    for i in li:
        res.append(count_func(i, arg[0]))
    return "|".join(res)


a = 'bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32'
b = 'bc;dfad|adfasd|adfa|df'
print(pat_rec(a))
print(pat_rec(b))
