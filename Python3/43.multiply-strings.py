#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # deal with input "0" otherwise it will return "000..."
        if num1 == "0" or num2 == "0":
            return "0"
        # get the length of num1 and num2
        m = len(num1)
        n = len(num2)
        # use a list to store the final result
        ansList = [0] * (m + n)
        # the multiplication of num1[i] num2[j] are in ansList[i+j]
        for i in range(m-1, -1, -1):
            # get current digit of num1
            n1 = int(num1[i])
            for j in range(n-1, -1, -1):
                # get current digit of num2
                n2 = int(num2[j])
                tmp = n1 * n2
                # multiplication bit
                ansList[i+j+1] += tmp % 10
                # carry bit
                ansList[i+j] += tmp // 10
        # deal with digits that are larger than 0
        for i in range(m+n-1, -1, -1):
            if ansList[i] >= 10:
                ansList[i-1] += ansList[i] // 10
                ansList[i] = ansList[i] % 10
        # get the result str
        index = 0
        if ansList[0] == 0:
            index = 1
        result = "".join(str(x) for x in ansList[index:])
        return result



# @lc code=end

