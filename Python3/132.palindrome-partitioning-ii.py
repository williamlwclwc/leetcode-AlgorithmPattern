#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        # quickly check whether s[0:i+1] is palindrome
        isPalindrome = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)):
                if s[i] == s[j]:
                    if j-i <= 1 or isPalindrome[i+1][j-1]:
                        isPalindrome[i][j] = True
        # dp[i]: s[0:i+1] minimum cuts
        dp = [-1 for _ in range(len(s))]
        for i in range(len(s)):
            if isPalindrome[0][i]:
                dp[i] = 0
                continue
            for j in range(0, i):
                if isPalindrome[j+1][i]:
                    if dp[i] == -1 or dp[i] > dp[j]+1:
                        dp[i] = dp[j]+1
        return dp[len(s)-1]
# @lc code=end

