#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = click[0]
        m = click[1]
        if board[n][m] == 'M':
            board[n][m] = 'X'
            return board
            
        def _update(board, n, m):
            if n < 0 or n > len(board) - 1 or m < 0 or m > len(board[0]) - 1:
                return
            if board[n][m] == 'E':
                cnt = 0
                for x, y in [(n+1, m),(n-1, m),(n, m+1),(n, m-1),(n-1, m-1),(n-1, m+1),(n+1, m-1),(n+1, m+1)]:
                    if not (x < 0 or x > len(board) - 1 or y < 0 or y > len(board[0]) - 1):
                        if board[x][y] == 'M':
                            cnt += 1
                if cnt == 0:
                    board[n][m] = 'B'
                    for x, y in [(n+1, m),(n-1, m),(n, m+1),(n, m-1),(n-1, m-1),(n-1, m+1),(n+1, m-1),(n+1, m+1)]:
                        if not (x < 0 or x > len(board) - 1 or y < 0 or y > len(board[0]) - 1) and board[x][y] != 'B':
                            _update(board, x, y)
                else:
                    board[n][m] = str(cnt)


        _update(board, n, m)
        return board
# @lc code=end

