#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # stride 2 for fast pointer, stride 1 for slow pointer
        def getMedian(left, right):
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        # recursively build the BST tree
        def buildTree(left, right):
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        
        return buildTree(head, None)
# @lc code=end

