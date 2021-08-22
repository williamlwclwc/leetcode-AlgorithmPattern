#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # remove last digit -> move right -> until it's 0
        res = 0
        while n != 0:
            # check last digit
            n1 = n
            last_digit = n1 & 1
            if last_digit:
                res += 1
            # move right
            n = n >> 1
        return res
# @lc code=end

