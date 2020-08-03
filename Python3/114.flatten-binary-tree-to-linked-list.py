#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur_node = root
        while cur_node:
            next_node = cur_node.left
            if next_node:
                if next_node.right:
                    pre_node = next_node.right
                else:
                    pre_node = next_node
                while pre_node.right:
                    pre_node = pre_node.right
                pre_node.right = cur_node.right
                cur_node.left = None
                cur_node.right = next_node
            cur_node = cur_node.right
# @lc code=end

