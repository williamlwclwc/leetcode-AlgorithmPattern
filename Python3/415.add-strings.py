#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        int_num1 = self.str_to_int(num1)
        int_num2 = self.str_to_int(num2)
        return str(int_num1 + int_num2)
    

    def str_to_int(self, str_num):
        length = len(str_num)
        result = 0
        for char_num in str_num:
            result += (ord(char_num) - ord('0')) * (10 ** (length-1))
        return result
# @lc code=end
