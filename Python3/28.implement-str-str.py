#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        notMatch = 0
        for i in range(len(haystack)-len(needle)+1):
            notMatch = 0
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    notMatch = 1
                    break
            if notMatch == 0:
                return i
        return -1
# @lc code=end

