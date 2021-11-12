#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None:
            return None
        p = head
        # dummy1.next is the head of the smaller part
        dummy1 = ListNode()
        p1 = dummy1
        # dummy2.next is the head of the larger part
        dummy2 = ListNode()
        p2 = dummy2
        while p != None:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        # both p1 and p2 should end with None
        p1.next = None
        p2.next = None
        # put two parts together
        p1.next = dummy2.next
        return dummy1.next

# @lc code=end

