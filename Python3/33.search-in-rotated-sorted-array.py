#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            # find target, return
            if nums[mid] == target:
                return mid
            # mid > start: sorted from start to mid
            elif nums[mid] > nums[start]:
                # if target is in the sorted part, shrink the latter part, otherwise shrink the first part
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            # mid < end: sorted from mid to end
            elif nums[mid] < nums[end]:
                # if target is in the sorted part, shrink the first part, otherwise shrink the latter part
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
        # compare target with start and end
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        return -1

# @lc code=end

