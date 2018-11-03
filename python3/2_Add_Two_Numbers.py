"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        # to know which one is longer
        l2_cp = l2
        l1_cp = l1
        while l2_cp != None and l1_cp != None:
            # re: the one go next with the loop
            if l2_cp.next == None:
                re = l1
            if l1_cp.next == None:
                re = l2
            l2_cp = l2_cp.next
            l1_cp = l1_cp.next
        # result: head node of re, for output purpose
        result = re
        while l2 != None or l1 != None:
            # calculate each node
            if l2 == None:
                re.val = l1.val + carry
            elif l1 == None:
                re.val = l2.val + carry
            else:
                re.val = l1.val + l2.val + carry
            # deal with carry issue
            carry = 0
            if re.val >= 10:
                re.val -= 10
                carry = 1
            # if not none, remember to go to next node
            if l2 != None:
                l2 = l2.next
            if l1 != None:
                l1 = l1.next
            # re should be the last node, not none
            if re.next != None:
                re = re.next
        # if there is still carry not done:
        if carry == 1:
            new = ListNode(1)
            re.next = new
        return result