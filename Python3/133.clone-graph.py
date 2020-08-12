#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start

# Solution 1: DFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # init a hashmap to store visited nodes
    # key: node, value: node
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        # if graph is empty
        if not node:
            return None
        # if already visited
        if node in self.visited:
            return self.visited[node]
        # if haven't visited
        # clone node without neighbors
        clone_node = Node(node.val, [])
        # put it into hashmap
        self.visited[node] = clone_node
        # update neighbors of clone node
        if node.neighbors:
            for neighbor in node.neighbors:
                clone_node.neighbors.append(self.cloneGraph(neighbor))
        
        return clone_node

# Solution 2: BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # init a hashmap to store visited nodes
        # key: node, value: node
        visited = {}
        if not node:
            return None
        
        # init queue
        queue = deque()
        queue.append(node)
        # put first node into the hashmap
        visited[node] = Node(node.val, [])

        # BFS
        while queue:
            # pop out the first one in queue
            cur_node = queue.popleft()
            # traverse all its neighbors
            for neighbor in cur_node.neighbors:
                # if not visited, put it in the hashmap
                # put it into queue and visit it later
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # update clone node's neighbors
                visited[cur_node].neighbors.append(visited[neighbor])
        
        # after BFS
        return visited[node]
# @lc code=end

