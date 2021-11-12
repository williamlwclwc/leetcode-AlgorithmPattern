#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
import sys
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[sys.maxsize for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        return self.dfs(memo, triangle, 0, 0)
    
    def dfs(self, memo, triangle, i, j):
        if i == len(triangle):
            return 0
        if memo[i][j] != sys.maxsize:
            return memo[i][j]
        memo[i][j] = min(self.dfs(memo, triangle, i+1, j), self.dfs(memo, triangle, i+1, j+1)) + triangle[i][j]
        return memo[i][j]

# @lc code=end

