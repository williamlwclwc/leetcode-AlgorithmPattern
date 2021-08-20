#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        queue = deque()
        visited = [[0] * c for _ in range(r)]
        result = [[0] * c for _ in range(r)]
        # multi start point BFS, put all start points in queue
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    queue.append([i, j])
                    visited[i][j] = 1
        
        # same as level order traverse of binary tree
        level = 0
        neighbors = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        while queue:
            size = len(queue)
            # traverse this level
            for _ in range(size):
                x, y = queue.popleft()
                # find a '1' at this level, that '1' to closest 0 is 'level steps'
                if mat[x][y] == 1:
                    result[x][y] = level
                # continue put its neighbors into queue for next level's traverse
                for xx, yy in neighbors:
                    newx, newy = x+xx, y+yy
                    if newx < 0 or newx >= r or newy < 0 or newy >= c:
                        continue
                    elif visited[newx][newy] == 0:
                        queue.append([newx, newy])
                        visited[newx][newy] = 1
            # finished current level
            level += 1
        return result
# @lc code=end

