#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        result = []
        stack = []
        while len(stack) != 0 or root != None:
            while root != None:
                stack.append(root)
                root = root.left
            ele = stack.pop()
            result.append(ele.val)
            root = ele.right
        return result
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if root == None:
#             return []
#         result = []
#         self.inOrder(root, result)
#         return result

#     def inOrder(self, root, result):
#         if root == None:
#             return
#         self.inOrder(root.left, result)
#         result.append(root.val)
#         self.inOrder(root.right, result)
#         return

# @lc code=end

