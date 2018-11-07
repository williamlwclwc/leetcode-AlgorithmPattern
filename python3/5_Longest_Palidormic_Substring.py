class Solution:
    # dynamic programming: palindromic string
    # expand from center, only compare the new char each time
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.expand(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.expand(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer, expanding
    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1 # left pointer moves left
            r += 1 # right pointer moves right
        return s[l+1:r]


    # brute force algorithm: will work but will not be accepted
    def longestPalindrome_bruteforce(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlength = 0
        len_s = len(s)
        current_str = []
        longest = []
        for k in range(len_s):
            current_str = []
            for i in range(k, len_s):
                current_str.append(s[i])
                len_cur_str = len(current_str)
                flag = 1
                for j in range(len_cur_str):
                    if current_str[j] != current_str[len_cur_str-j-1]:
                        flag = 0
                        break
                if flag == 1:
                    if len(current_str) > maxlength:
                        maxlength = len(current_str)
                        longest = current_str.copy()
        result = "".join(longest)
        return result