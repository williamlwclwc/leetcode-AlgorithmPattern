#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        # find insert pos
        if target < nums[start]:
            return start
        elif target < nums[end]:
            return end
        elif target > nums[end]:
            return end + 1
        
# @lc code=end

