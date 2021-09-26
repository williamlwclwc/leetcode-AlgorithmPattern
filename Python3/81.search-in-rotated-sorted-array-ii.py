#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            # it is the same as [33]
            elif nums[mid] > nums[start]:
                # sorted from start to mid
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[mid] < nums[end]:
                # sorted from mid to end
                if nums[end] >= target and target >= nums[mid]:
                    start = mid
                else:
                    end = mid
            # if this happen, we cannot decide which part is sorted
            else:
                if nums[mid] == nums[start]:
                    start += 1
                if nums[mid] == nums[end]:
                    end -= 1
        if nums[start] == target or nums[end] == target:
            return True
        return False
# @lc code=end

