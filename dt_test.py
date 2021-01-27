# Reconstruct Original Digits from English
# Given a non-empty string containing an out-of-order English representation of digits 0-9,
#  output the digits in ascending order.
# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits.
#  That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"
#
# Output: "012"
# 'zero' -> {z:1, e:1, r:1, o:1}


def resconstruct(inp):
    mao = [(0, 'z'), (2, 'w'), (4, 'u'), (6, 'x'), (8, 'g'),
           (1, 'o'), (3, 'h'), (5, 'f'), (7, 's'), (9, 'n')]


on
three
five
seven
nine
 res1 = []
  res2 = []
   # print(mao_items)
   for i in mao[:5]:
        if i[1] in inp:
            res1.append(i[0])
    for i in mao[5:]:
        if i[1] in inp:
            res2.append(i[0])

    i, j = 0, 0
    res = []
    while i < len(res1) and j < len(res2):
        if res1[i] < res2[j]:
            res.append(str(res1[i]))
            i += 1
        else:
            res.append(str(res2[j]))
            j += 1
    while i < len(res1):
        res.append(str(res1[i]))
        i += 1
    while j < len(res2):
        res.append(str(res2[j]))
        j += 1

    return ''.join(res)


print(resconstruct("owoztneoer"))
print(resconstruct("fviefuro"))
