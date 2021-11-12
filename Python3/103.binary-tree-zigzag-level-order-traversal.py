#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        level_num = 0
        result = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            level_len = len(q)
            level_result = []
            for i in range(level_len):
                node = q.popleft()
                level_result.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            if level_num % 2 == 1:
                level_result = level_result[::-1]
            result.append(level_result)
            level_num += 1
        return result
# @lc code=end

