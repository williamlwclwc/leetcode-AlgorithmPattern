#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a ^ a = 0
        # a ^ 0 = a
        # 0 ^ a = a
        # only the single number will be left
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res
# @lc code=end

