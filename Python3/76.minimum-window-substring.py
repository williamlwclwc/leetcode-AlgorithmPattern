#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        left = 0
        right = 0
        occ = {}
        # the min len of the substring that covers all chars in t
        min_len = sys.maxsize
        for ele in t:
            if occ.get(ele) == None:
                occ.update({ele : 1})
            else:
                occ[ele] += 1
        num_notfound = len(occ)
        # when right bound reach the end
        # return "" if cannot find a win cover all chars
        # or return the narrowest win that cover all chars
        while right < len(s):
            # add right until cover all chars in t
            if num_notfound != 0:
                if occ.get(s[right]) != None:
                    if occ[s[right]] == 1:
                        num_notfound -= 1
                    occ[s[right]] -= 1
            else:
                # already cover all chars, narrow scope
                if min_len > len(s[left:right+1]):
                    result = s[left:right+1]
                    min_len = len(result)
                # remove left
                if occ.get(s[left]) != None:
                    if occ[s[left]] == 0:
                        num_notfound += 1
                    occ[s[left]] += 1
                left += 1
            # if cur win cannot cover all chars, move right bound
            if num_notfound != 0:
                right += 1
        return result
# @lc code=end

