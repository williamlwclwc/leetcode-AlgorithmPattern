#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from top to bottom
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         def _height(root):
#             if not root:
#                 return 0
#             return 1 + max(_height(root.left), _height(root.right))
            
#         if not root:
#             return True
#         if abs(_height(root.left)-_height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
#             return True
#         else:
#             return False

# from buttom to top
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def _height(root):
            if not root:
                return 0
            left_height = _height(root.left)
            right_height = _height(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height-right_height) > 1:
                return -1
            else:
                return 1+max(_height(root.left), _height(root.right))
        
        if not root:
            return True
        if _height(root) > 0:
            return True
        else:
            return False
# @lc code=end

