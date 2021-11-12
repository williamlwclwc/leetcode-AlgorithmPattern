#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt_U = 0
        cnt_D = 0
        cnt_L = 0
        cnt_R = 0
        for move in moves:
            if move == 'U':
                cnt_U += 1
            elif move == 'D':
                cnt_D += 1
            elif move == 'L':
                cnt_L += 1
            elif move == 'R':
                cnt_R += 1
        if cnt_U == cnt_D and cnt_L == cnt_R:
            return True
        else:
            return False
# @lc code=end

