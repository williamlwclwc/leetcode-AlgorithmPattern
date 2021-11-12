#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        # a hashmap where keys are original nodes and values are related new nodes
        hash_ori_new = {None:None} # in case random points to None
        new_head = Node(head.val) # copy the first node
        p = head.next
        hash_ori_new.update({head:new_head})
        new = new_head
        # copy the nodes (ignore random pointers for now)
        while p != None:
            new.next = Node(p.val)
            new = new.next
            hash_ori_new.update({p:new})
            p = p.next
        new = new_head
        p = head
        # copy random pointers, p.random -> related new nodes
        # e.g. {1 -> 1'} p.random = 1 hash[p.random] = 1'
        while new != None:
            new.random = hash_ori_new[p.random]
            new = new.next
            p = p.next
        return new_head
# @lc code=end

