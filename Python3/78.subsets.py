#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
import copy
class Solution:
    result = []
    temp = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # clear the list
        del self.result[:]
        del self.temp[:]
        self.backtrack(nums, 0)
        return self.result 
    def backtrack(self, nums, startidx):
        length = len(nums)
        self.result.append(copy.deepcopy(self.temp))
        if startidx >= length:
            return
        
        for i in range(startidx, length):
            # select current value
            self.temp.append(nums[i])
            self.backtrack(nums, i+1)
            # step backwards: not select current value
            self.temp = self.temp[:-1]
# @lc code=end

