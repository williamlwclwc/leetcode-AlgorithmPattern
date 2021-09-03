#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLength = len(s1)
        # store the chars of target string
        target_dict = {}
        for ele in s1:
            if target_dict.get(ele) == None:
                target_dict.update({ele : 1})
            else:
                target_dict[ele] += 1
        # number of chars in s1 that we not yet found
        target_len = len(target_dict)
        # left, right bound of window
        left = 0
        right = left + windowLength
        cur_win = s2[left:right]
        for ele in cur_win:
            if target_dict.get(ele) != None:
                target_dict[ele] -= 1
                # when char change from >0 to 0, we find all chars of that char
                if target_dict[ele] == 0:
                    target_len -= 1
        if target_len <= 0:
            return True
        # sliding window, each time remove left add right
        while right < len(s2):
            # remove left, add right
            if target_dict.get(s2[left]) != None:
                if target_dict[s2[left]] == 0:
                    target_len += 1
                target_dict[s2[left]] += 1
            if target_dict.get(s2[right]) != None:
                target_dict[s2[right]] -= 1
                if target_dict[s2[right]] == 0:
                    target_len -= 1
            if target_len <= 0:
                return True
            left += 1
            right += 1
        return False
# @lc code=end

