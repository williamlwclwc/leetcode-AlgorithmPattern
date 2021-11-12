#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = None
        # put numbers into stack
        # when encounter operations, pop 2 elements
        # do the operation and put the result back into stack
        for token in tokens:
            if token == '+':
                a2 = stack.pop()
                a1 = stack.pop()
                a = a1 + a2
                stack.append(a)
            elif token == '-':
                a2 = stack.pop()
                a1 = stack.pop()
                a = a1 - a2
                stack.append(a)
            elif token == '*':
                a2 = stack.pop()
                a1 = stack.pop()
                a = a1 * a2
                stack.append(a)
            elif token == '/':
                a2 = stack.pop()
                a1 = stack.pop()
                # division should truncate towards 0
                a = int(a1 / a2)
                stack.append(a)
            else:
                stack.append(int(token))
        # final result is the final number in the stack
        result = stack.pop()
        return result
# @lc code=end

