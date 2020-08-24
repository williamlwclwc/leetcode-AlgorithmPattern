#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            if len(s) % i != 0:
                continue
            sub = s[0:i]
            res = sub * int(len(s) / i)
            if res == s:
                return True
        return False
# @lc code=end

