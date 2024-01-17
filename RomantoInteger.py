# Roman to int (easy)
def romantoInt(s):
    s += "0"
    result = 0
    m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "0": 0}
    if len(s) == 1:
        return m[s[0]]
    for i in range(len(s) - 1):
        if m[s[i]] < m[s[i + 1]]:
            result -= m[s[i]]
        else:
            result += m[s[i]]
    return result


## LEETCODE ANSWER

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         m = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }

#         ans = 0

#         for i in range(len(s)):
#             if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
#                 ans -= m[s[i]]
#             else:
#                 ans += m[s[i]]

#         return ans
