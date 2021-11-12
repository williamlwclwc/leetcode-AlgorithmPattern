#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # result: 0, recursive value
        # result: 1, global maximum
        result = self.maxPath(root)
        return result[1]
    
    def maxPath(self, root):
        result = [0, float('-inf')]
        if root == None:
            return result
        left = self.maxPath(root.left)
        right = self.maxPath(root.right)
        result[0] = max(left[0]+root.val, right[0]+root.val, 0)
        result[1] = max(left[1], right[1], left[0]+right[0]+root.val)
        return result
# @lc code=end

