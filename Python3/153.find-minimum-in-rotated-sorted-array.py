#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                # mid > end, min is at the right of mid
                start = mid + 1
            else:
                # mid < end, min is mid or the left of mid
                end = mid
        # exit loop: start == end
        return nums[start]

# @lc code=end

