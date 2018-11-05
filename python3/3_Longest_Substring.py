# Given a string, find the length of the longest substring without repeating characters.
class Solution:
    # Solution 1: Using List(array)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = [] # the substring
        maxlength = 0
        for c in s:
            if c in longest:
                maxlength = max(maxlength, len(longest))
                # update substring, start from the previous one's next item
                longest = longest[longest.index(c)+1 :]
            # then add the new one to the substring
            longest.append(c)
        maxlength = max(maxlength, len(longest))
        return maxlength


    # Solution 2: Using Hashmap
    def lengthOfLongestSubstring_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        # hashmap: key = s[i], value: last_appear_index
        char_appr = {}
        length = len(s)
        maxlength = 0 
        start = 0 # substring startpoint's index
        for i in range(length):
            # if item appear in hash and it's in the substring range(after startpoint)
            if s[i] in char_appr and start <= char_appr[s[i]]:
                # update startpoint from the previous one's next item
                start = char_appr[s[i]] + 1
            else:
                maxlength = max(maxlength, i - start + 1)
            char_appr[s[i]] = i # build/update hashmap
        return maxlength
    
