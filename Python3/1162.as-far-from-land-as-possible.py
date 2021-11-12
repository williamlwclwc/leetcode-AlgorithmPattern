#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#

# @lc code=start
from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        queue = deque()
        visited = [[0] * c for _ in range(r)]
        max_dis = -1
        # multi start points BFS
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    visited[i][j] = 1
        
        # level order traverse with BFS
        level = 0
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            size = len(queue)
            # traverse current level
            for _ in range(size):
                x, y = queue.popleft()
                # if we find '0' compare current dis level with max_dis
                if grid[x][y] == 0:
                    if max_dis < level:
                        max_dis = level
                # put neighbors into queue for next level's traverse
                for xx, yy in neighbors:
                    newx, newy = x + xx, y + yy
                    if newx < 0 or newy < 0 or newx >= r or newy >= c:
                        continue
                    elif visited[newx][newy] == 0:
                        queue.append([newx, newy])
                        visited[newx][newy] = 1
            # finish current level
            level += 1
        return max_dis
# @lc code=end

