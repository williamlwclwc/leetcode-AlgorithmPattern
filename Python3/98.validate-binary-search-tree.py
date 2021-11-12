#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: in order traverse
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # a valid BST's inorder traverse should be sorted
        inorder_list = self.inOrder(root)
        for i in range(len(inorder_list)-1):
            # left node less than root, right node more than root, no '='
            if inorder_list[i] >= inorder_list[i+1]:
                return False
        return True
    

    def inOrder(self, root):
        result = []
        if root == None:
            return result
        result = self.inOrder(root.left)
        result.append(root.val)
        right = self.inOrder(root.right)
        result.extend(right)
        return result
'''
# solution 2: divide and conquer
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # left max < root < right min
        # result: 0: true/false, 1: left max, 2: right min
        result = self.divideAndConquer(root)
        return result[0]

    def divideAndConquer(self, root):
        if root == None:
            return [True, None, None]
        left = self.divideAndConquer(root.left)
        right = self.divideAndConquer(root.right)
        # any subtree is not BST
        if left[0] == False or right[0] == False:
            return [False, None, None]
        # current root is not BST
        if left[1] != None and left[1] >= root.val:
            return [False, None, None]
        if right[2] != None and right[2] <= root.val:
            return [False, None, None]
        # current root is BST, update left max and right min
        leftMax = None
        rightMin = None
        if right[1] != None:
            leftMax = right[1]
        else:
            leftMax = root.val
        if left[2] != None:
            rightMin = left[2]
        else:
            rightMin = root.val
        return [True, leftMax, rightMin]
'''
# @lc code=end

