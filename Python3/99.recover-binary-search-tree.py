#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # traverse the tree in mid order and put the result into this list
        mid_order_list = []
        def mid_order_traverse(root):
            if root:
                mid_order_traverse(root.left)
                mid_order_list.append(root.val)
                mid_order_traverse(root.right)
        
        # find the wrong indices in mid_order_list
        def find_wrong_index(mid_order_list):
            wrong_index_1 = -1
            wrong_index_2 = -1
            count = 0
            for i in range(len(mid_order_list)-1):
                if mid_order_list[i] > mid_order_list[i+1]:
                    count += 1
                    if count == 1:
                        wrong_index_1 = i
                    elif count == 2:
                        wrong_index_2 = i+1
            if count == 1:
                wrong_index_2 = wrong_index_1 + 1
            return wrong_index_1, wrong_index_2
        
        # swap the the nodes with the wrong value in a binary search tree
        def recover_tree(root, target_value_1, target_value_2):
            if root:
                recover_tree(root.left, target_value_1, target_value_2)
                if root.val == target_value_1:
                    root.val = target_value_2
                elif root.val == target_value_2:
                    root.val = target_value_1
                recover_tree(root.right, target_value_1, target_value_2)
        
        # traverse the tree and get mid_order_list 
        mid_order_traverse(root)
        # find wrong indices
        wrong_index_1, wrong_index_2 = find_wrong_index(mid_order_list)
        # recover the tree
        recover_tree(root, mid_order_list[wrong_index_1], mid_order_list[wrong_index_2])
# @lc code=end

