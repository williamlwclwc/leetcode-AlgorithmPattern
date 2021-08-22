#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        # every iteration get the last digit
        # move 31-0 digit each time
        # n >> 1 unitl n is 0
        res = 0
        i = 31
        while n != 0:
            last_digit = n & 1
            res = res ^ (last_digit << i)
            n = n >> 1
            i -= 1
        return res
# @lc code=end

