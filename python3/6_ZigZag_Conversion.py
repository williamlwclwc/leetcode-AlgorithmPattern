class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # categorized discussion: numRows = 1,2 or more
        if numRows == 1:
            return s
        elif numRows == 2:
            lists = [[], []]
            for i in range(len(s)):
                if i % 2 == 0:
                    lists[0].append(s[i])
                else:
                    lists[1].append(s[i])
        else:
            # construct 2-dimensional array(list)
            lists = [[] for i in range(numRows)]
            index = 0
            mode = 0 # mode: 0 normal, 1 zigzag
            for i in range(len(s)):
                if mode == 0:
                    # append normally
                    lists[index].append(s[i])
                    index += 1
                    # switch mode
                    if index == numRows:
                        mode = 1
                        index = numRows - 2
                elif mode == 1:
                    # append 'zigzag'
                    lists[index].append(s[i])
                    index -= 1
                    # switch mode
                    if index == 0:
                        mode = 0
                        index = 0
        # convert 2-dimensional list to string
        result = ""
        for i in range(numRows):
            result += "".join(lists[i])
        return result

    