#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numPaths = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            numPaths[i][0] = 1
        for i in range(n):
            numPaths[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                numPaths[i][j] = numPaths[i-1][j] + numPaths[i][j-1]
        
        return numPaths[m-1][n-1]
# @lc code=end

