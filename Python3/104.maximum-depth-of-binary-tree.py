#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1
# @lc code=end

