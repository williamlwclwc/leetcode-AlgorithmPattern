#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return False
        # find mid pos
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        # reverse the latter half
        p = mid
        prev = None
        while p != None:
            n = p.next
            p.next = prev
            prev = p
            p = n
        # compare the two parts
        p1 = head
        p2 = prev
        while p1 != None and p2 != None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        if p1 != None and p1.next != None:
            return False
        elif p2 != None and p2.next != None:
            return False
        else:
            return True
# @lc code=end

