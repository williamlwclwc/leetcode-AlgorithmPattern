#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse = s[::-1]
        # find the common part of s and reverse
        for i in range(len(s)):
            if s.startswith(reverse[i:]):
                # remove the common part and combine with s
                return reverse[:i] + s
        
        return ""
# @lc code=end

