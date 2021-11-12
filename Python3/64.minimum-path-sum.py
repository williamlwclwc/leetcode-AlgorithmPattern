#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         hashsum = [[-1 for _ in range(len(grid[i]))] for i in range(len(grid))]
#         return self.minPath(hashsum, grid, 0, 0)

#     def minPath(self, hashsum, grid, i, j):
#         if i == len(grid) or j == len(grid[0]):
#             return 0

#         if hashsum[i][j] != -1:
#             return hashsum[i][j]
        
#         if i < len(grid)-1 and j < len(grid[0])-1:
#             hashsum[i][j] = min(
#                 self.minPath(hashsum, grid, i+1, j) + grid[i][j],
#                 self.minPath(hashsum, grid, i, j+1) + grid[i][j]
#             )
#         elif i == len(grid)-1:
#             hashsum[i][j] = self.minPath(hashsum, grid, i, j+1) + grid[i][j]
#         elif j == len(grid[0])-1:
#             hashsum[i][j] = self.minPath(hashsum, grid, i+1, j) + grid[i][j]
#         return hashsum[i][j]
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        hashsum = [[-1 for _ in range(len(grid[i]))] for i in range(len(grid))]
        # init row 0 col 0
        hashsum[0][0] = grid[0][0]
        for i in range(1, len(grid[0])):
            hashsum[0][i] = hashsum[0][i-1] + grid[0][i]
        for j in range(1, len(grid)):
            hashsum[j][0] = hashsum[j-1][0] + grid[j][0]
        # fill the hashsum row by row
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                hashsum[i][j] = min(hashsum[i][j-1], hashsum[i-1][j]) + grid[i][j]
        
        return hashsum[len(grid)-1][len(grid[0])-1]
# @lc code=end

