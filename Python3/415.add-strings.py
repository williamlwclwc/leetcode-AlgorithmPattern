#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         int_num1 = self.str_to_int(num1)
#         int_num2 = self.str_to_int(num2)
#         return str(int_num1 + int_num2)
    

#     def str_to_int(self, str_num):
#         length = len(str_num)
#         result = 0
#         for char_num in str_num:
#             result += (ord(char_num) - ord('0')) * (10 ** (length-1))
#         return result
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0 # carry bit
        i = len(num1) - 1 # point to the last digit of num1
        j = len(num2) - 1 # point to the last digit of num2
        while i >= 0 or j >= 0:
            # use 0 if there is no digit
            if i >= 0:
                n1 = int(num1[i])
            else:
                n1 = 0
            if j >= 0:
                n2 = int(num2[j])
            else:
                n2 = 0
            # current bit sum
            tmp = n1 + n2 + carry
            # calculate carry bit
            carry = tmp // 10
            # insert remainder at the front of result
            result = str(tmp % 10) + result
            i -= 1
            j -= 1
        if carry:
            return "1" + result
        else:
            return result            
# @lc code=end
