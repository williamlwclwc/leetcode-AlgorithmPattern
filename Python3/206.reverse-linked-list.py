#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        if head == None:
            return None
        p = head
        while p != None:
            # preserve position: p.next
            n = p.next
            # reverse p.next to previous
            p.next = prev
            # move prev point to current position, i.e. prev position for next iteration
            prev = p
            # move current iteration pointer to preserved next position
            p = n
        return prev
# @lc code=end

