#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        # same as 141, see if there is a cycle
        fast = head.next
        slow = head
        while fast != None and fast.next != None:
            if fast == slow:
                break
            fast = fast.next.next
            slow = slow.next
        # if no cycle
        if fast != slow:
            return None
        # assume entrance pos is a
        # assume meet as pos b
        # assume the rest of a loop distance is c
        # for slow: a+b+m(b+c)
        # for fast: a+b+n(b+c)-1 = 2(a+b)+2m(b+c) => a+b+1 = (n-2m)(b+c)
        p = head
        slow = slow.next
        # when p and slow meet at entrance, p went: a+x(b+c)
        # slow went: a+x(b+c)+b+1 = (n-2m+x)(b+c) will stop at entrance pos
        while p != slow:
            p = p.next
            slow = slow.next
        return p
# @lc code=end

