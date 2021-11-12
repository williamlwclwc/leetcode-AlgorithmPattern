#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head == None:
            return None
        # dummy node
        dummy = ListNode()
        dummy.next = head
        prev = None
        # go to reverse start pos
        p = dummy
        for i in range(left):
            prev = p
            p = p.next
        # start is the pos before reverse segment
        start = prev
        # end is the first ele in reverse seg, i.e. the last ele in seg after reversal
        end = p
        # reverse seg: left -> right
        for i in range(left, right+1):
            # reverse linked list, see [206]
            n = p.next
            p.next = prev
            prev = p
            p = n
        # put the reverse part back together
        end.next = p
        start.next = prev
        return dummy.next
# @lc code=end

