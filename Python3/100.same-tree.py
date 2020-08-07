#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # compare the tree below two certain node
        def isSameNode(p, q):
            # if at least one of them is None
            if p is None and q is None:
                return True
            elif p is None and q is not None:
                return False
            elif p is not None and q is None:
                return False
            # current node is the same
            if p.val == q.val:
                # continue compare children nodes
                return isSameNode(p.left, q.left) and isSameNode(p.right, q.right)
        
        # compare the value of each node
        return isSameNode(p, q)
# @lc code=end

