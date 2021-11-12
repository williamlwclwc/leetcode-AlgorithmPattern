#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # empty string is valid
        if s == '':
            return True
        stack = []
        # iterate all chars in string
        for ch in s:
            # push ch into stack if stack is empty
            if stack == []:
                if ch == ')' or ch == ']' or ch == '}':
                    return False
                stack.append(ch)
            # if stack is not empty
            # check if the current ch can pair the parentheses at top of the stack
            # if it can pair, pop the top one ch from the stack
            # else we push the current ch into the stack as well
            elif stack[-1] == '(':
                if ch == ')':
                    stack.pop()
                else:
                    stack.append(ch)
            elif stack[-1] == '[':
                if ch == ']':
                    stack.pop()
                else:
                    stack.append(ch)
            elif stack[-1] == '{':
                if ch == '}':
                    stack.pop()
                else:
                    stack.append(ch)
        # if all parentheses are paired up, the stack will be empty
        if stack == []:
            return True
        else:
            return False
# @lc code=end

