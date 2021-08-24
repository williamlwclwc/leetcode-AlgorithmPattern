#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        dummy = ListNode(next=head)
        p = dummy
        while p != None and p.next != None and p.next.next != None:
            n1 = p.next
            n2 = p.next.next
            p.next = n2
            n1.next = n2.next
            n2.next = n1
            p = p.next.next
        return dummy.next
# @lc code=end

