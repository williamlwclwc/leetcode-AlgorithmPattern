#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        # create reversed words dict
        reversed_dict = {word: i for i, word in enumerate(words)}
        # iterate list of words
        for i, word in enumerate(words):
            # split substrings
            for j in range(len(word)+1):
                left_sub = word[:j][::-1]
                right_sub = word[j:][::-1]
                # 1. left_sub's reversed string is in the dict
                # 2. the word and left_sub is different (consider left_sub is palindrome)
                # 3. right_sub is a palindrome
                if left_sub in reversed_dict and reversed_dict.get(left_sub) != i and right_sub == right_sub[::-1]:
                    result.append([i, reversed_dict.get(left_sub)])
                # right substring at least start from the second char
                if j>0 and right_sub in reversed_dict and reversed_dict.get(right_sub) != i and left_sub == left_sub[::-1]:
                    result.append([reversed_dict.get(right_sub), i])

        return result
# @lc code=end

