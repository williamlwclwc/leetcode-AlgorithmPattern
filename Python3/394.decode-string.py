#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        if s == None:
            return None
        if s == []:
            return []
        # a stack whose ele is in format [int, str]
        stack = []
        res = ""
        temp = []
        temp_num = ""
        numbers = "1234567890"
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for token in s:
            # for 0-9 add to temp
            if token in numbers:
                temp_num += token
            # for a-z add to res string
            elif token in alpha:
                res += token
            # for [, push previous temp to stack
            elif token == '[':
                temp.append(int(temp_num))
                temp.append(res)
                stack.append(temp)
                res = ""
                temp = []
                temp_num = ""
            # for ], pop stack and calculate res
            # ss is the previous results
            # curent res is what we need to multiply
            # put the result back in res
            elif token == ']':
                multi, ss = stack.pop()
                for i in range(multi):
                    ss += res
                res = ss
        return res
# @lc code=end

