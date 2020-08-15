#
# @lc app=leetcode id=546 lang=python3
#
# [546] Remove Boxes
#

# @lc code=start
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # a dict that stores max point of a certain segment
        max_memo = {}
        # find the max value from left:l to right:r
        def findMax(l, r, k):
            if l > r:
                return 0
            # if the max points has been calculated
            if (l, r, k) in max_memo:
                return memo[(l, r, k)]
            # remove consecutive boxes
            while r > 1 and boxes[r] == boxes[r-1]:
                k += 1
                r -= 1
            res = findMax(l, r-1, 0) + (k+1) * (k+1)
            # check if get rid of some boxes can get more points
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    max_res = max(res, findMax(i+1, r-1, 0) + findMax(l, i, k+1))
            # store max points into the dict
            max_memo[(l, r, k)] = max_res
            return max_res

        return findMax(0, len(boxes)-1, 0)
# @lc code=end

