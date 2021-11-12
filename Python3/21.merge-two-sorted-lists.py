#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        p = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        # if there are l1 or l2 ele left
        while l1 != None:
            p.next = l1
            p = p.next
            l1 = l1.next
        while l2 != None:
            p.next = l2
            p = p.next
            l2 = l2.next
        return dummy.next
# @lc code=end

