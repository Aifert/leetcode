# Longest Common Prefix (Easy)


def longestCommonPrefix(strs):
    arr_length = len(strs)
    strs = sorted(strs, key=len)
    word = strs[0]
    i = 1
    while i != arr_length:
        if word not in strs[i][: len(word)]:
            word = word[:-1]
            i = 1
        else:
            i += 1
    return word


# leetcode answer
class Solution(object):
    def longestCommonPrefix(self, v):
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans


# when it is sorted lexicographically it becomes["preheat","prehistoric","oven"]
# only need to compare first and last
