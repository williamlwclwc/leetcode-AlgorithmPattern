#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, result, [])
        return result
    
    def backtrack(self, nums, result, cur_set):
        if len(cur_set) == len(nums):
            result.append(cur_set[:])
            return
        
        for ele in nums:
            if ele in cur_set:
                continue
            cur_set.append(ele)
            self.backtrack(nums, result, cur_set)
            cur_set.pop()
# @lc code=end

