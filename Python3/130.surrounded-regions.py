#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
# dfs solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # edge condition, if board is None
        if not board:
            return 
        
        rows, cols = len(board), len(board[0])

        # define dfs recursive process
        def dfs(start_x, start_y):
            # only continue if current node is "O", if violate either condition, return directly
            if not 0 <= start_x < rows or not 0 <= start_y < cols or not board[start_x][start_y] == "O":
                return
            
            # tag the "O" that cannot be converted with "F"
            board[start_x][start_y] = "F"
            # continue dfs process
            dfs(start_x + 1, start_y)
            dfs(start_x - 1, start_y)
            dfs(start_x, start_y + 1)
            dfs(start_x, start_y - 1)
        
        # use dfs to tag all nodes that cannot be converted with "F"
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        for i in range(cols):
            dfs(0, i)
            dfs(rows-1, i)
        
        # convert all "F" with "O" and all "O" with "X"
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "F":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


# bfs solution
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # edge condition, if board is None
        if not board:
            return

        rows, cols = len(board), len(board[0])

        # put all starting points ("O" on the edge)
        que = deque()
        for i in range(rows):
            if board[i][0] == "O":
                que.append((i, 0))
            if board[i][cols-1] == "O":
                que.append((i, cols-1))
        for i in range(cols):
            if board[0][i] == "O":
                que.append((0, i))
            if board[rows-1][i] == "O":
                que.append((rows-1, i))
        
        # bfs
        while que:
            # get one from the queue
            x, y = que.popleft()
            board[x][y] = "F"
            for next_x, next_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                # put the next starting point that not violate either of the rule in queue
                if 0 <= next_x < rows and 0 <= next_y < cols and board[next_x][next_y] == "O":
                    que.append((next_x, next_y))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "F":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

# @lc code=end

