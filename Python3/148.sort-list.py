#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # if there is only 1 node, return that node
        if head == None or head.next == None:
            return head
        # find the middle pos of the linked list
        # if fast start with head, then left will always has 2 elements(infinite loop)
        fast = head.next
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None # or the head will not cut into half
        # divide list into 2 parts: left, right
        left = self.sortList(head)
        right = self.sortList(mid)
        # merge sort the two part
        dummy = ListNode()
        p = dummy
        while left != None and right != None:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        # if there is anything left in left/right
        if left != None:
            p.next = left
        if right != None:
            p.next = right
        return dummy.next
# @lc code=end

