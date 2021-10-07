#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        cnt = {}
        for ele in nums:
            if cnt.get(ele) == None:
                cnt.update({ele : 1})
            else:
                cnt[ele] += 1
        nums.sort()
        self.backtrack(nums, result, cnt, [])
        return result

    def backtrack(self, nums, result, cnt, cur_set):
        if len(cur_set) == len(nums):
            result.append(cur_set[:])
            return
        
        for i in range(len(nums)):
            ele = nums[i]
            if cnt.get(ele) == 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            cur_set.append(ele)
            cnt[ele] -= 1
            self.backtrack(nums, result, cnt, cur_set)
            last_ele = cur_set.pop()
            cnt[last_ele] += 1
            
# @lc code=end

