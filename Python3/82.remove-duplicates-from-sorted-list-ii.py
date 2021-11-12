#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        # use dummy node here incase we need to remove head node
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while p.next != None and p.next.next != None:
            rmVal = None
            while p.next.next != None and p.next.val == p.next.next.val:
                rmVal = p.next.val
                p.next = p.next.next
            # e.g. rm 3, p.next=3 p.next.next=4
            # we still need to remove p.next(3)
            if p.next.val == rmVal:
                p.next = p.next.next
            # e.g. p=3 p.next=2 p.next.next=3
            # p moves to the next node
            else:
                p = p.next
        return dummy.next

# @lc code=end

