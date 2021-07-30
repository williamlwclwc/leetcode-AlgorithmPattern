#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None        
        if root == p or root == q:
            return root
        # divide
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # conquer
        # root is the lowest common ancestor
        if left != None and right != None:
            return root
        # left/right is already the lowest common ancestor, pass it all the way to root
        # the other child is None(cannot find p/q in the other subtree)
        elif left != None:
            return left
        elif right != None:
            return right
        else:
            return None
# @lc code=end

