#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # put 2d matrix into linear sorted list
        allnums = []
        for row in matrix:
            allnums += row
        # then binary search
        start = 0
        end = len(allnums)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if allnums[mid] > target:
                end = mid - 1
            elif allnums[mid] < target:
                start = mid + 1
            else:
                return True
        if allnums[start] == target:
            return True
        if allnums[end] == target:
            return True
        return False
# @lc code=end

