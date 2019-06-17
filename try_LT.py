def findAnagrams(s: str, p: str):
        ans = []
        p_size = len(p)
        print(p_size)
        for idx, val in enumerate(s):
            if idx == 6:
                print(sorted(s[idx:p_size]))
            if sorted(s[idx:idx+p_size]) == sorted(p):
                # print(idx)
                ans.append(idx)
        return ans

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))
