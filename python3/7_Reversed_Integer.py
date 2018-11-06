class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = [] # list to store reversed numbers
        flag = 0 # whether x is >0 or not
        upper_bound = 2**31-1
        lower_bound = -(2**31)
        if x < lower_bound or x > upper_bound:
            return 0
        if x < 0:
            flag = 1
            x = -x
        # decompose x into single numbers
        while x != 0:
            a.append(x % 10)
            x //= 10
        # get list a to be a integer again
        length = len(a) - 1
        result = 0
        for i in a:
            result += i*(10**length)
            length -= 1
        # whether >0 or not
        if flag == 1:
            result = -result
        # check the boundaries for result
        if result < lower_bound or result > upper_bound:
            return 0
        return result
