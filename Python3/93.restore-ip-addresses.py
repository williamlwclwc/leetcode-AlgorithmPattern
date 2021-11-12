#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result  = []
        # recursively segment the string into (4) segments
        def backtrack(segs, start, strIn):
            # if split into 4 segs and use up all the chars
            if len(segs) == 4 and start == len(strIn):
                result.append('.'.join(segs))
                return
            # if split into 4 segs but remain chars unused
            if len(segs) == 4 and start != len(strIn):
                return
            # try select 1,2,3 chars repectively
            for i in range(1, 4):
                # cannot exceed indices: last index < len(strIn)
                if start + i - 1 >= len(strIn):
                    return 
                # if select more than 1 chars, the first selected char cannot be 0
                if i >= 2 and strIn[start] == '0':
                    return
                # if selected 3 chars, the number should <= 255
                if i == 3 and strIn[start: start+3] > '255':
                    return
                # select i number in this step
                selected = strIn[start: start+i]
                backtrack(segs+[selected], start+i, strIn) 

        backtrack([], 0, s)
        return result

# @lc code=end

