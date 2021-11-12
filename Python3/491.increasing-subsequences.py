#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []

        def _dfs(nums, tmp):
            # add if sub sequence length >= 2
            if len(tmp) >= 2:
                result.append(tmp)
            # use curDFS to track used nums in current DFS
            curDFS = set()
            for inx, num in enumerate(nums):
                if num in curDFS:
                    continue
                # if tmp is empty or new num is larger
                if not tmp or tmp[-1] <= num:
                    curDFS.add(num)
                    # put new num in tmp and recursion
                    _dfs(nums[inx+1:], tmp+[num])
                # if not do recursion, then regard as give up current num
        _dfs(nums, [])
        return result
# @lc code=end

