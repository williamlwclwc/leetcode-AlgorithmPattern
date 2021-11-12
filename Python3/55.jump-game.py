#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxDes = nums[0]
        for i in range(1, len(nums)):
            if maxDes < i:
                return False
            else:
                maxDes = max(maxDes, nums[i]+i)
        return True
# @lc code=end

