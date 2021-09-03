#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        end = -1
        result = 0
        for start in range(n):
            # iterate substring's start point
            if start != 0:
                # remove left
                occ.remove(s[start-1])
            # add right until repeat or reach the end
            while end + 1 < n and s[end+1] not in occ:
                occ.add(s[end+1])
                end += 1
            # calculate the max length
            result = max(result, end - start + 1)
        return result

# @lc code=end

