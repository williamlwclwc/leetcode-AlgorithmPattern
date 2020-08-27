#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adjancent list
        adjList = defaultdict(list)
        for start, end in tickets:
            adjList[start] += [end]
        # sort adjacent list, pop will get the last item (the last should be the smallest one)
        for start in adjList:
            adjList[start].sort(reverse=True)
        # dfs
        result = []
        def _dfs(node):
            while adjList[node]:
                # walk one possible path, then remove the path
                # will end when one node have nowhere to go, then this node is our destination
                _dfs(adjList[node].pop())
            # quit when we find the final node
            # backtrack and put other nodes in the front each time
            result.insert(0, node)
        
        _dfs("JFK")
        return result
# @lc code=end

