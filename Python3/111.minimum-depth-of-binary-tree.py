#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # root node is not a leaf node, need to be dealt with alone
        if not root.left or not root.right:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        # else return the minimum of the depth of left and right subtree
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
# @lc code=end

