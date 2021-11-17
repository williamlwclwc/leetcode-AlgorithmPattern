#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        for word in wordDict:
            dic[word] = 1
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] == True and dic.get(s[j:i]) != None:
                    dp[i] = True
                    break
        return dp[len(s)]
# @lc code=end

