#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            level = len(queue)
            level_result = []
            for i in range(level):
                # visit the first node in queue
                first_node = queue.popleft()
                level_result.append(first_node.val)
                if first_node.left != None:
                    queue.append(first_node.left)
                if first_node.right != None:
                    queue.append(first_node.right)
            result.append(level_result)
        return result
# @lc code=end

