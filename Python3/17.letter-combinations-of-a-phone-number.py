#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    combinations = ''
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_dict = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        
        result = []
        def _combine(curIndex):
            if curIndex == len(digits):
                result.append(self.combinations)
            else:
                num = digits[curIndex]
                curList = num_dict[num]
                for letter in curList:
                    temp = self.combinations
                    self.combinations = self.combinations + letter
                    _combine(curIndex+1)
                    self.combinations = temp
        
        _combine(0)
        return result


# @lc code=end

