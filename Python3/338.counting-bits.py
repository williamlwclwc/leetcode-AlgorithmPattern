#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.hammingWeight(i))
        return ans

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

