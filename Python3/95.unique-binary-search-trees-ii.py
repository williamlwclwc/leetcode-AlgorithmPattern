#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate(1, n)

    def generate(self, left, right):
        if left > right:
            return [None]
        res = []
        for i in range(left, right+1):
            # each loop generate trees whose root is i
            left_bsts = self.generate(left, i-1)
            right_bsts = self.generate(i+1, right)
            # each left_bst right_bst is a subtree, we combine them with the root
            for left_bst in left_bsts:
                for right_bst in right_bsts:
                    root = TreeNode(i)
                    root.left = left_bst
                    root.right = right_bst
                    # this root is a possible bst whose root is i
                    res.append(root)
        # return all subtrees
        return res
# @lc code=end

