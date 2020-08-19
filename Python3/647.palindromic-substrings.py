#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for start in range(len(s)):
            for end in range(start+1, len(s)+1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    cnt += 1

        return cnt
# @lc code=end

