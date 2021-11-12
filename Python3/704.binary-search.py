#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialization
        start = 0
        end = len(nums) - 1
        # loop
        while start + 1 < end:
            # update mid in each loop
            mid = (start+end) // 2
            # compare mid with target, update boundaries
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                return mid
        # compare last 2 items
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1

# @lc code=end

