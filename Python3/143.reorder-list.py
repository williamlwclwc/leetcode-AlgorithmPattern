#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the mid pos of linked list
        fast = head.next
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        # reverse the latter part(i.e. mid)
        p = mid
        prev = None
        while p != None:
            n = p.next
            p.next = prev
            prev = p
            p = n
        # merge the two parts
        p1 = head
        p2 = prev
        while p1 != None and p2 != None:
            n1 = p1.next
            p1.next = p2
            n2 = p2.next
            p2.next = n1
            p1 = n1
            p2 = n2
# @lc code=end

