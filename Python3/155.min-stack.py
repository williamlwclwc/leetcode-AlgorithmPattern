#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # use an additional stack
        # everytime we push a value, we save the related min value into minStack
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.getMin() < val:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) == 0:
            return sys.maxsize
        else:
            return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

