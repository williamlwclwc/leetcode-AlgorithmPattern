#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        fast = head.next
        slow = head
        while fast != None and fast.next != None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
# @lc code=end

