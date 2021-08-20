#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # ith pos's largest area: heights[left_i] < heights[i], heights[right_i] < heights[i]
        # max area = heights[i] * (right_i - left_i -1)
        res = 0
        # we don't know when right_i shows up so we put i into a stack
        # i can be poped when right_i shows up
        stack = []
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                # ele can be poped if it finds heights[i] < itself
                top_ele = stack.pop()
                # cal the max area
                res = max(res, heights[top_ele]*(i - stack[-1] -1))
            stack.append(i)
        return res
# @lc code=end

