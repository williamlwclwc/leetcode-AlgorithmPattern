#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(TreeNode):
            # if traversed to the end
            if not TreeNode:
                return 0, 0
            # traverse its children
            w_select_left, w_not_select_left = _rob(TreeNode.left)
            w_select_right, w_not_select_right = _rob(TreeNode.right)
            # if select this node
            w_select = TreeNode.val + w_not_select_left + w_not_select_right
            # if not select this node
            w_not_select = max(w_select_left, w_not_select_left) + max(w_select_right, w_not_select_right)
            return w_select, w_not_select


        # start traverse from the root node
        return max(_rob(root))
# @lc code=end

