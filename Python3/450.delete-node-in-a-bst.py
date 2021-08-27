#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        if key > root.val:
            # target > root, goto root.right
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # target < root, goto root.left
            root.left = self.deleteNode(root.left, key)
        else:
            # target == root, deleteNode here
            # root only has left/right child, replace with left/right child
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                # root has both left right child
                p = root.right
                # find right subtree's most left child
                while p.left != None:
                    p = p.left
                # put target's left child on the right subtree's most left child's left
                p.left = root.left
                # replace with right child
                return root.right
        return root
# @lc code=end
