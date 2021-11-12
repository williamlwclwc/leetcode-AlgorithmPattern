#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count the number of 1 in every byte
        result = 0
        for i in range(0, 64):
            cnt_1 = 0 # number of 1 in this digit
            for j in range(len(nums)):
                cnt_1 += (nums[j] >> i) & 1
            # restore the digits that 1 appears only once
            if i == 63:
                # for python int<0
                result = result - ((cnt_1 % 3) << i)
            else:
                result = result ^ ((cnt_1 % 3) << i)
        return result
# @lc code=end

