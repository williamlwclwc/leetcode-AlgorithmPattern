#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # find common prefix of m, n, all other digits would be 0 (1 & 0 = 0)
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift
# @lc code=end

