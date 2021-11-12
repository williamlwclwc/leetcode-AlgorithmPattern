#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start + 1 < end:
            mid = (start + end) // 2
            if isBadVersion(mid) == False:
                start = mid + 1
            else:
                end = mid - 1
        if isBadVersion(start) == True:
            return start
        if isBadVersion(end) == True:
            return end
        else:
            return end+1
# @lc code=end

