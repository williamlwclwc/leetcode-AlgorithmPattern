#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        for i in range(1, len(nums)+1):
            self.backtrack(nums, result, 0, i, [])
        return result
    
    def backtrack(self, nums, result, start_idx, length, cur_set):
        if len(cur_set) == length:
            result.append(cur_set[:])
        for i in range(start_idx, len(nums)):
            if i > start_idx and nums[i] == nums[i-1]:
                continue
            cur_set.append(nums[i])
            self.backtrack(nums, result, i+1, length, cur_set)
            cur_set.pop()

# @lc code=end

