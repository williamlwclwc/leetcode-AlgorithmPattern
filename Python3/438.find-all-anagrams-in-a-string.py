#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windowLength = len(p)
        result = []
        p_chars = {}
        for ele in p:
            if p_chars.get(ele) == None:
                p_chars.update({ele:1})
            else:
                p_chars[ele] += 1
        # first window
        left = 0
        right = windowLength
        cur_win = s[left:right]
        target_len = len(p_chars)
        for ele in cur_win:
            if p_chars.get(ele) != None:
                p_chars[ele] -= 1
                # when char change from >0 to 0, we find all chars of that char
                if p_chars[ele] == 0:
                    target_len -= 1
        if target_len <= 0:
            result.append(left)
        # slide windows
        while right < len(s):
            # remove left, add right
            if p_chars.get(s[left]) != None:
                if p_chars[s[left]] == 0:
                    target_len += 1
                p_chars[s[left]] += 1
            if p_chars.get(s[right]) != None:
                p_chars[s[right]] -= 1
                if p_chars[s[right]] == 0:
                    target_len -= 1
            left += 1
            right += 1
            if target_len <= 0:
                result.append(left)
        return result
# @lc code=end

