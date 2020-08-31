#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # store the visisted rooms
        visited = {}
        def _dfs(n):
            # has already visited, do not need to do it again
            if visited.get(n) != None:
                return
            # visit the new room
            visited.update({n: 1})
            # iterate possible next rooms
            for i in rooms[n]:
                # recursively visit next rooms
                _dfs(i)
        
        # return true if visited all rooms
        _dfs(0)
        if len(visited) == len(rooms):
            return True
        else:
            return False
# @lc code=end

