#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        numPaths = [[-1 if obstacleGrid[i][j] == 0 else 0 for j in range(n)] for i in range(m)]
        numPaths[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                numPaths[i][0] = numPaths[i-1][0]
            else:
                numPaths[i][0] = 0
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                numPaths[0][i] = numPaths[0][i-1]
            else:
                numPaths[0][i] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if numPaths[i][j] == 0:
                    continue
                else:
                    numPaths[i][j] = numPaths[i-1][j] + numPaths[i][j-1]
        
        return numPaths[m-1][n-1]
# @lc code=end

