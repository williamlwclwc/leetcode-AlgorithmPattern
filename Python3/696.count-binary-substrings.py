#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        consecutive_list = []
        cnt = 0
        prev = s[0]
        for i in range(len(s)):
            if prev == s[i]:
                cnt += 1
            else:
                prev = s[i]
                consecutive_list.append(cnt)
                cnt = 1
            if i == len(s)-1:
                consecutive_list.append(cnt)
        
        for i in range(len(consecutive_list)-1):
            result += min(consecutive_list[i], consecutive_list[i+1])
        return result
# @lc code=end

