#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            end_idx = min(i+nums[i]+1, len(nums))
            for j in range(i, end_idx):
                if dp[j] == -1:
                    dp[j] = 1 + dp[i]
                else:
                    dp[j] = min(dp[j], 1+dp[i])
        return dp[len(nums)-1]
# @lc code=end

