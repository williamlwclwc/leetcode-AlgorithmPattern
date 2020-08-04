#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

# Solution 1: BFS
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init indegrees & adjacency
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        # generate indegrees & adjacency table
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # get all the courses with the indegrees of 0 to start with
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        # BFS
        while queue:
            # visit the node(prerequisites course)
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                # put into queue if the node can be visit (indegree is 0)
                if indegrees[cur] == 0:
                    queue.append(cur)
        # if numCourses is 0 (visit all nodes) then return true
        if numCourses == 0:
            return True
        else:
            return False

# Solution 2: DFS
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # DFS search
#         def dfs(i, adjacency, flags):
#             # ending conditions
#             if flags[i] == -1:
#                 # if the node has been visited from other DFS
#                 return True
#             elif flags[i] == 1:
#                 # if the node has been visited from current DFS
#                 return False
#             # visit current node
#             flags[i] = 1
#             # recursively visit its adjacent nodes
#             for j in adjacency[i]:
#                 if not dfs(j, adjacency, flags):
#                     return False
#             # if no loop in current DFS
#             flags[i] = -1
#             return True
        

#         # init adjacency & flags
#         adjacency = [[] for _ in range(numCourses)]
#         flags = [0 for _ in range(numCourses)]
#         # generate adjacency table
#         for cur, pre in prerequisites:
#             adjacency[pre].append(cur)
#         # start DFS, if loop appears, return false 
#         for i in range(numCourses):
#             if not dfs(i, adjacency, flags):
#                 return False
#         # if there are no loops, return true
#         return True
# @lc code=end

