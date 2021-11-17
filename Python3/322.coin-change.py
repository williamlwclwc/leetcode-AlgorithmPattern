#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = amount
        n = len(coins)
        dp = [[-1 for _ in range(m+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0
        for i in range(m+1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = sys.maxsize
        for i in range(1, n):
            for j in range(1, m+1):
                if j >= coins[i]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        if dp[n-1][m] != sys.maxsize:
            return dp[n-1][m]
        else:
            return -1
# @lc code=end