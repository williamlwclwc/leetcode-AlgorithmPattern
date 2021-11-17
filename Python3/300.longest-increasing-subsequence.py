#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i+1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
                    if dp[i] > res:
                        res = dp[i]
        return res
# @lc code=end

