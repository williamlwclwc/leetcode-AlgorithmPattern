#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtracking(result, 0, 0, n, "")
        return result


    def backtracking(self, result, left, right, n, string):
        if left == right == n:
            result.append(string)
            return

        if left < n:
            self.backtracking(result, left+1, right, n, string+'(')
        if left > right:
            self.backtracking(result, left, right+1, n, string+')')
        
# @lc code=end

