#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
# class Solution:
#     def fib(self, n: int) -> int:
#         if n < 2:
#             return 1
#         return self.fib(n-1) + self.fib(n-2)

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a = 1
        b = 1
        for i in range(2, n):
            temp = a
            a = a+b
            b = temp
        return a
# @lc code=end

