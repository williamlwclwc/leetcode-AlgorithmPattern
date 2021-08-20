#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = len(grid)
        y = len(grid[0])
        island_cnt = 0
        for i in range(x):
            for j in range(y):
                if grid[i][j] == '1':
                    island_cnt += 1
                    self.dfs(i, j, grid)
        return island_cnt
    
    
    def dfs(self, x, y, grid):
        r = len(grid)
        c = len(grid[0])
        if grid[x][y] == '1':
            grid[x][y] = '0'
            if x+1 < r:
                self.dfs(x+1, y, grid)
            if y+1 < c:
                self.dfs(x, y+1, grid)
            if x-1 >= 0:
                self.dfs(x-1, y, grid)
            if y-1 >= 0:
                self.dfs(x, y-1, grid)
# @lc code=end

