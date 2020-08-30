#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(' ')
        for i in range(len(word_list)):
            word_list[i] = word_list[i][::-1]
        
        return " ".join(word_list)
# @lc code=end

