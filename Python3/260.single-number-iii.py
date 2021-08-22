#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # res: result of all nums doing ^ operation
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        # divide the two numbers that appear only once
        # find a digit that is not zero (i.e. the two number is different at this digit)
        h = 1
        while res & h == 0:
            h = h << 1
        # xor in different group
        a = 0
        b = 0
        for i in range(len(nums)):
            if h & nums[i]:
                a ^= nums[i]
            else:
                b ^= nums[i]
        return [a, b]
# @lc code=end

